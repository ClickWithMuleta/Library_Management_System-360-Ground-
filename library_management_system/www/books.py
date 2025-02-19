import frappe

def get_context(context):
    # Fetch all books
    context.books = frappe.get_all("Book", fields=["name", "title", "image", "author", "publish_date", "isbn", "status"])

