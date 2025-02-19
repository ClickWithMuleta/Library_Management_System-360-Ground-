
import frappe
from frappe.model.document import Document


class Loan(Document):
    def before_submit(self):
        if self.type == "Loan":
            self.validate_loan()
            # set the book status to be Loaned
            book = frappe.get_doc("Book", self.book)
            book.status = "Loaned"
            book.save()

        elif self.type == "Return":
            self.validate_return()
            # set the book status to be Available
            book = frappe.get_doc("Book", self.book)
            book.status = "Available"
            book.save()

    def validate_loan(self):
        self.validate_membership()
        book = frappe.get_doc("Book", self.book)
        # book cannot be loaned if it is already loaned
        if book.status == "Loaned":
            frappe.throw("Book is already loaned by another member")

    def validate_return(self):
        book = frappe.get_doc("Book", self.book)
        # book cannot be returned if it is not loaned first
        if book.status == "Available":
            frappe.throw("Book cannot be returned without being loaned first")


    def validate_membership(self):
        # Check if the member exists
        member = frappe.db.get_value("Member", self.member, ["name", "full_name"], as_dict=True)

        if not member:
            frappe.throw("Member doesn't exist")
        
        # Check if the full name is set
        if not member.get("full_name"):
            frappe.throw("Member exists but Full Name is missing")
        
