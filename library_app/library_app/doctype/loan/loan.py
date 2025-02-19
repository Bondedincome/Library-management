# Copyright (c) 2025, Daniot and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Loan(Document):
    website = frappe._dict(
        condition_field="is_published",  # Replace with a field that determines visibility
        page_title="Loan Details",
        template="templates/loan.html",  # Optional: specify a custom template
        no_cache=1
    )

    def validate(self):
        self.check_book_availability()

    def check_book_availability(self):
        # Fetch the book document
        book = frappe.get_doc("Book", self.book)

        # Check if the book is already loaned out
        if book.status == "Loaned":
            frappe.throw(f"Book '{book.title}' is currently on loan and cannot be borrowed.")

        # Mark the book as loaned
        book.status = "Loaned"
        book.save()

    def on_cancel(self):
        book = frappe.get_doc("Book", self.book)
        book.status = "Available"
        book.save()
        
    def on_trash(doc, method):
        """Reset book status to 'Available' when a loan is deleted"""
        book = frappe.get_doc("Book", doc.book)
        book.status = "Available"
        book.save()
