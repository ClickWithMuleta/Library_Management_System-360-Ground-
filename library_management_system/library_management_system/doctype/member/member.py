# Copyright (c) 2025, muletasisay and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
class Member(WebsiteGenerator):
    
    def get_context(self, context):
        context.member = frappe.get_all("Member", fields=["name", "first_name", "last_name", "email", "phone_number"])

    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
        
        # Generate a unique membership_id if not already set
        if not self.membership_id:
            self.membership_id = self.generate_membership_id()

    def generate_membership_id(self):
        # Example format: LIB-20250214-0001
        from datetime import datetime
        import frappe

        today = datetime.today().strftime('%Y%m%d')
        last_member = frappe.db.get_value("Member", {"membership_id": ("like", f"LIB-{today}-%")}, "membership_id", order_by="creation desc")

        if last_member:
            last_number = int(last_member.split("-")[-1]) + 1
        else:
            last_number = 1

        return f'LIB-{today}-{last_number:04d}'



