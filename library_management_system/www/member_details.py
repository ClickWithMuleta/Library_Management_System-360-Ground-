import frappe

def get_context(context):
    # Get the member name from the URL (book name will be passed as part of the URL)
    member_name = frappe.form_dict.get('name')
    
    if not member_name:
        frappe.throw("member name is missing in the URL.")
    
    # Fetch the member document using its name
    try:
        member = frappe.get_doc("Member", member_name)
    except frappe.DoesNotExistError:
        frappe.throw(f"Member with name '{member_name}' does not exist.")
    
    # Pass the member document to the context
    context.doc = member
    return context
