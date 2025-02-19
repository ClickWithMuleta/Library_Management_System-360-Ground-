import frappe

def get_context(context):
    book_name = frappe.form_dict.get("name")

    if not book_name:
        frappe.throw("Book name is missing in the URL.")

    book = frappe.get_doc("Book", book_name)

    if not book:
        frappe.throw("Book not found.")

    context.book = book
