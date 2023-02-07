# Copyright (c) 2023, jetatech and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestMeeting(FrappeTestCase):
    def test_sync_todos(self):
        meeting - frappe.get_doc({
            "doctype":"Meeting",
            "title": "Test Meeting",
            "status": "Planned",
            "date": "2023-02-15",
            "from_time": "09:00",
            "to_time": "10:00",
            "minutes": [
                {
                    "description": "Test Minute 1",
                    "status": "Open",
                    "assigned_to": "test@example.com"
                }
            ]
        })    
        meeting.insert()

        todo = frappe.get_all("ToDo", filters={
            "reference_type": meeting.doctype, 
            "reference_name": meeting.name, 
            "owner": "test@example.com"
            })

        self.assertEquals(todo[0].name, meeting.minutes[0].todo)
        self.assertEquals(todo[0].description, meeting.minutes[0].description)
