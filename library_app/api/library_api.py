import frappe

# -------------------------------
# BOOK Endpoints
# -------------------------------

@frappe.whitelist(allow_guest=False)
def create_book(title, author, isbn=None, status="Available"):
    """
    Create a new Book.
    """
    # Create new Book document
    book_doc = frappe.get_doc({
         "doctype": "Book",
         "title": title,
         "author": author,
         "isbn": isbn,
         "status": status
    })
    book_doc.insert()
    frappe.db.commit()
    return {"message": "Book created successfully", "book_id": book_doc.name}

@frappe.whitelist(allow_guest=True)
def get_book(book_id):
    """
    Retrieve a Book by its ID.
    """
    book_doc = frappe.get_doc("Book", book_id)
    return book_doc.as_dict()

@frappe.whitelist(allow_guest=False)
def update_book(book_id, title=None, author=None, isbn=None, status=None):
    """
    Update details of an existing Book.
    """
    book_doc = frappe.get_doc("Book", book_id)
    if title:
         book_doc.title = title
    if author:
         book_doc.author = author
    if isbn:
         book_doc.isbn = isbn
    if status:
         book_doc.status = status
    book_doc.save()
    frappe.db.commit()
    return {"message": "Book updated successfully"}

@frappe.whitelist(allow_guest=False)
def delete_book(book_id):
    """
    Delete a Book.
    """
    frappe.delete_doc("Book", book_id)
    frappe.db.commit()
    return {"message": "Book deleted successfully"}


@frappe.whitelist(allow_guest=True)
def get_book_list():
    available_books = frappe.get_all("Book", filters={"status": "available"}, fields=["name", "title", "author", "book_cover"])
    loaned_books = frappe.get_all("Book", filters={"status": "loaned"}, fields=["name", "title", "author", "book_cover"])
    
    return {
        "available_books": available_books,
        "loaned_books": loaned_books
    }

# -------------------------------
# Function for dashboard populating
# -------------------------------

@frappe.whitelist(allow_guest=True)
def get_dashboard_data():
    available_books_count = frappe.db.count("Book", filters={"status": "available"})
    loaned_books_count = frappe.db.count("Book", filters={"status": "loaned"})
    
    newest_books = frappe.get_all("Book", fields=["title", "author"], order_by="creation desc", limit=5)
    
    return {
        "available_books_count": available_books_count,
        "loaned_books_count": loaned_books_count,
        "newest_books": newest_books
    }


# -------------------------------
# MEMBER Endpoints
# -------------------------------

@frappe.whitelist(allow_guest=False)
def create_member(first_name, last_name, email, phone):
    """
    Create a new Member.
    """
    member_doc = frappe.get_doc({
         "doctype": "Member",
         "first_name": first_name,
         "last_name": last_name,
         "email": email,
         "phone": phone
    })
    member_doc.insert()
    frappe.db.commit()
    return {"message": "Member created successfully", "member_id": member_doc.name}

@frappe.whitelist(allow_guest=True)
def get_member(member_id):
    """
    Retrieve a Member by ID.
    """
    member_doc = frappe.get_doc("Member", member_id)
    return member_doc.as_dict()

@frappe.whitelist(allow_guest=False)
def update_member(member_id, first_name=None, last_name=None, email=None, phone=None):
    """
    Update an existing Member.
    """
    member_doc = frappe.get_doc("Member", member_id)
    if first_name:
         member_doc.first_name = first_name
    if last_name:
         member_doc.last_name = last_name
    if email:
         member_doc.email = email
    if phone:
         member_doc.phone = phone
    member_doc.save()
    frappe.db.commit()
    return {"message": "Member updated successfully"}

@frappe.whitelist(allow_guest=False)
def delete_member(member_id):
    """
    Delete a Member.
    """
    frappe.delete_doc("Member", member_id)
    frappe.db.commit()
    return {"message": "Member deleted successfully"}
