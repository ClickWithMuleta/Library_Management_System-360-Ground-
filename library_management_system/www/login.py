import frappe

def get_context(context):
    if frappe.request.method == "POST":
        email = frappe.form_dict.get("email")
        password = frappe.form_dict.get("password")

        try:
            frappe.local.login_manager.login(email, password)
            frappe.local.response["type"] = "redirect"
            frappe.local.response["location"] = "/library-books"
        except frappe.AuthenticationError:
            frappe.msgprint("Invalid credentials. Please try again.", alert=True)
