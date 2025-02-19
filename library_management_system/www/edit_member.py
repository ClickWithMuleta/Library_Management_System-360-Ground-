import frappe

def get_context(context):
    member_name = frappe.form_dict.get("name")

    if not member_name:
        frappe.throw("Member name is missing in the URL.")

    member = frappe.get_doc("Member", member_name)

    if not member:
        frappe.throw("Member not found.")

    context.member = member
