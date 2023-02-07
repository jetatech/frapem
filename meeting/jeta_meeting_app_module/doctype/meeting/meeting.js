// Copyright (c) 2023, jetatech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Meeting', {
//	alert("Inside meeting email function");
	send_emails_btn: function(frm){
		if(frm.doc.status==="Planned"){
			frappe.call({
				method: "meeting.api.send_invitation_emails",
				args: {
					meeting:frm.doc.name
				}
			})
		}
	},
});
frappe.ui.form.on('Meeting Attendee', {
	attendee: function(frm, cdt, cdn) {
		var attendee = frappe.model.get_doc(cdt, cdn);
		if (attendee.attendee) {
			// if attendee, get full name
			frappe.call({
				method: "meeting.jeta_meeting_app_module.doctype.meeting.meeting.get_full_name",
				args: {
					attendee: attendee.attendee
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "full_name", r.message);
				}
			});
		} else {
			// if no attendee, clear full name
			frappe.model.set_value(cdt, cdn, "full_name", null);
		}
	},
});
