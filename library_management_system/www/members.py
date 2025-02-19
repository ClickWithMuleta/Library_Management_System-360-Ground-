import frappe

def get_context(context):
    # Fetch all members
    context.members = frappe.get_all("Member", fields=["name", "membership_id", "first_name", "last_name", "full_name", "email", "phone"])

