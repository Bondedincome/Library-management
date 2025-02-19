# Copyright (c) 2025, Daniot and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Book(WebsiteGenerator):
    def is_available_for_loan(self):
        """
        Check if the book is available for loan.
        """
        return self.status == "Available"
    def validate(doc):
        if not doc.status:
            doc.status = "Available"  # Set a default status

