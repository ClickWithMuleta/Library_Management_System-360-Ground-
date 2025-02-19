// Copyright (c) 2025, muletasisay and contributors
// For license information, please see license.txt

frappe.ui.form.on('Member', {
    refresh: function(frm) {
    frm.add_custom_button('Create Membership', () => {
    frappe.new_doc('Member', {
    member: frm.doc.name
    })
    })
    frm.add_custom_button('Create Loan', () => {
    frappe.new_doc('Loan', {
    member: frm.doc.name
    })
    })
    }
   });
   