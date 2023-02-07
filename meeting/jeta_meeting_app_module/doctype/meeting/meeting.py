# Copyright (c) 2023, jetatech and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):
    def validate(self):
        self.validate_attendees()
        self.sync_todos()

    def validate_attendees(self):
        """Set missing names and warn if duplicate"""
        found = []
        for attendee in self.attendees:
            if not attendee.full_name:
                attendee.full_name = get_full_name(attendee.attendee)

            if attendee.attendee in found:
                frappe.throw(_("Attendee {0} entered twice").format(attendee.attendee))
            found.append(attendee.attendee)

    def on_update(self):
        self.sync_todos()

    def sync_todos(self):
        """Sync ToDos for assignments"""
        todos_added = [minute.todo for minute in self.minutes if minute.todo]

        for minute in self.minutes:
            if minute.assigned_to:
                if not minute.todo:
                    todo = frappe.get_doc({
                        "doctype":"ToDo",
                        "description": minute.description,
                        "reference_type": self.doctype,
                        "reference_name": self.name
                    })
                    todo.insert()
                    minute.todo = todo.name


# Marking a python method as whitelisted, allows it to be called from the web i.e. frontend in order to receive a return value within the logic of frontend Javascript
@frappe.whitelist()
def get_full_name(attendee):
    user = frappe.get_doc("User", attendee)
    # concatenate the name parts by space if it has value
    return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))
