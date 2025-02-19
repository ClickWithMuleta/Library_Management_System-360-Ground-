# Copyright (c) 2025, muletasisay and contributors
# For license information, please see license.txt
from frappe.website.website_generator import WebsiteGenerator

class Book(WebsiteGenerator):
    def get_context(self, context):
        context.base_template_path = "frappe/templates/web.html"

