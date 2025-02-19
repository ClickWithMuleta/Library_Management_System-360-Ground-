import frappe
from frappe import _
import html


# book releated api

@frappe.whitelist()  # Removed allow_guest=True
def create_book(title, author, publish_date, isbn, image=None):
    """Creates a new Book document. Only Librarians and System Managers can create books."""
    
    # Ensure user is logged in
    if frappe.session.user == "Guest":
        frappe.throw(_("You must be logged in to add a book."), frappe.AuthenticationError)

    # Ensure user has the correct role
    allowed_roles = ["Librarian", "System Manager"]
    user_roles = frappe.get_roles(frappe.session.user)
    
    if not any(role in user_roles for role in allowed_roles):
        frappe.throw(_("You do not have permission to add books."), frappe.PermissionError)

    # Create book record
    book = frappe.get_doc({
        "doctype": "Book",
        "title": title,
        "author": author,
        "publish_date": publish_date,
        "isbn": isbn,
        "image": image
    })
    book.insert()
    frappe.db.commit()  # Explicitly commit the transaction
    
    return {"message": "Book Created Successfully"}


# fetch all books
@frappe.whitelist()
def get_books():
    """Fetch all books"""
    books = frappe.get_all("Book", fields=["name", "title", "image", "author", "publish_date", "isbn", "status", "route", "is_published"])
    return books

#fetch specific book
@frappe.whitelist()
def get_book(title):
    """Fetch a single book by title"""
    book = frappe.get_all("Book", filters={"title": title}, fields=["*"])
    if not book:
        frappe.throw(_("Book not found"), frappe.DoesNotExistError)
    return book[0]

#update books
@frappe.whitelist()
def update_book(name, title, author, publish_date, isbn, status):
    if not frappe.session.user:
        frappe.throw("Unauthorized", frappe.PermissionError)

    if not frappe.has_permission("Book", "write"):
        frappe.throw("You do not have permission to edit books.", frappe.PermissionError)

    try:
        book = frappe.get_doc("Book", name)
        book.title = html.escape(title)  # Sanitize input
        book.author = html.escape(author)
        book.publish_date = publish_date
        book.isbn = html.escape(isbn)
        book.status = status
        book.save()
        frappe.db.commit()
        return {"message": "Book Updated Successfully"}
    except Exception as e:
        frappe.log_error(f"Update Book Error: {str(e)}", "Update Book API Error")
        return {"error": str(e)}


# Delete books
@frappe.whitelist()
def delete_book(name):
    # Ensure user is logged in
    if not frappe.session.user:
        frappe.throw("Unauthorized", frappe.PermissionError)

    # Check if user has permission to delete Book
    if not frappe.has_permission("Book", "delete"):
        frappe.throw("You do not have permission to delete books.", frappe.PermissionError)

    # Check if the book exists before deleting
    if not frappe.db.exists("Book", name):
        return {"error": f"Book {name} does not exist."}

    try:
        frappe.delete_doc("Book", name)
        frappe.db.commit()
        return {"message": "Book Deleted Successfully"}
    except frappe.LinkExistsError:
        return {"error": f"Cannot delete book {name} because it is linked to other records."}



# member releated api

@frappe.whitelist()  # Removed allow_guest=True
def create_member(first_name, last_name, email, phone, phone_country="ET"):
    """Creates a new member document. Only Librarians and System Managers can create members."""
    
    # Ensure user is logged in
    if frappe.session.user == "Guest":
        frappe.throw(_("You must be logged in to add a members."), frappe.AuthenticationError)

    # Ensure user has the correct role
    allowed_roles = ["Librarian", "System Manager"]
    user_roles = frappe.get_roles(frappe.session.user)
    
    if not any(role in user_roles for role in allowed_roles):
        frappe.throw(_("You do not have permission to add members."), frappe.PermissionError)
    
    # Ensure phone number starts with +251
    if not phone.startswith("+251"):
        phone = "+251" + phone.lstrip("0")  # Remove leading 0 if present

    # Create member record
    member = frappe.get_doc({
        "doctype": "Member",
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    })
    member.insert()
    frappe.db.commit()  # Explicitly commit the transaction
    
    return {"message": "Member Created Successfully"}



#fetch specific member
@frappe.whitelist()
def get_member(first_name):
    """Fetch a single member by first_name"""
    member = frappe.get_all("Member", filters={"first_name": first_name}, fields=["*"])
    if not member:
        frappe.throw(_("member not found"), frappe.DoesNotExistError)
    return member[0]

#update member
@frappe.whitelist()
def update_member(name, first_name, last_name, email, phone):
    if not frappe.session.user:
        frappe.throw("Unauthorized", frappe.PermissionError)

    if not frappe.has_permission("Member", "write"):
        frappe.throw("You do not have permission to edit members.", frappe.PermissionError)

    try:
        member = frappe.get_doc("Member", name)
        member.first_name = html.escape(first_name)  # Sanitize input
        member.last_name = html.escape(last_name)
        member.email = email
        member.phone = html.escape(phone)
        member.save()
        frappe.db.commit()
        return {"message": "Member Updated Successfully"}
    except Exception as e:
        frappe.log_error(f"Update member Error: {str(e)}", "Update member API Error")
        return {"error": str(e)}


# Delete member
@frappe.whitelist()
def delete_member(name):
    # Ensure user is logged in
    if not frappe.session.user:
        frappe.throw("Unauthorized", frappe.PermissionError)

    # Check if user has permission to delete Member
    if not frappe.has_permission("Member", "delete"):
        frappe.throw("You do not have permission to delete members.", frappe.PermissionError)

    # Check if the member exists before deleting
    if not frappe.db.exists("Member", name):
        return {"error": f"Member {name} does not exist."}

    try:
        frappe.delete_doc("Member", name)
        frappe.db.commit()
        return {"message": "Member Deleted Successfully"}
    except frappe.LinkExistsError:
        return {"error": f"Cannot delete member {name} because it is linked to other records."}


@frappe.whitelist()
def get_dashboard_stats():
    total_books = frappe.db.count("Book")
    available_books = frappe.db.count("Book", {"status": "Available"})
    loaned_books = frappe.db.count("Book", {"status": "Loaned"})
    active_loans = frappe.db.count("Loan")

    return {
        "total_books": total_books,
        "available_books": available_books,
        "loaned_books": loaned_books,
        "active_loans": active_loans
    }

@frappe.whitelist()
def get_loan_trends():
    loans = frappe.db.sql("""
        SELECT DATE(creation) as loan_date, COUNT(name) as count
        FROM `tabLoan`
        GROUP BY loan_date
        ORDER BY loan_date ASC
    """, as_dict=True)

    dates = [loan['loan_date'] for loan in loans]
    counts = [loan['count'] for loan in loans]

    return {"dates": dates, "counts": counts}
