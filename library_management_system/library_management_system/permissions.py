# permissions.py
import frappe

def get_permission_query(user):
    # Define your permission logic here
    if "Librarian" in frappe.get_roles(user) or "System Manager" in frappe.get_roles(user):
        return ""  # Allow access
    return "1=0"  # Deny access to non-authorized users
