# Mini Library Management System
# Author: Ramatu I. Kargbo
# University: Limkokwing University of Creative Technology

# -------------------------------
# 1. DATA STRUCTURES
# -------------------------------

# Tuples for valid genres
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Romance", "History")

# Dictionary for books
# Each book identified by its ISBN
books = {}

# List for members
members = []


# -------------------------------
# 2. CORE FUNCTIONS
# -------------------------------

# Add a book if ISBN is unique and genre is valid
def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book with this ISBN already exists."
    if genre not in genres:
        return "Invalid genre."

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "borrowed": 0
    }
    return f"Book '{title}' added successfully."


# Add a member if ID is unique
def add_member(member_id, name):
    for m in members:
        if m["id"] == member_id:
            return "Member ID already exists."
    members.append({"id": member_id, "name": name, "borrowed_books": []})
    return f"Member '{name}' added successfully."


# Update a book by ISBN
def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found."

    if genre and genre not in genres:
        return "Invalid genre."

    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies is not None:
        books[isbn]["total_copies"] = total_copies

    return f"Book '{isbn}' updated successfully."


# Delete a book by ISBN
def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    del books[isbn]
    return f"Book '{isbn}' deleted successfully."


# Delete a member only if no borrowed books
def delete_member(member_id):
    for m in members:
        if m["id"] == member_id:
            if m["borrowed_books"]:
                return "Cannot delete member with borrowed books."
            members.remove(m)
            return f"Member '{m['name']}' deleted successfully."
    return "Member not found."


# Borrow a book (max 3 per member)
def borrow_book(member_id, isbn):
    for m in members:
        if m["id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return "Cannot borrow more than 3 books."
            if isbn not in books:
                return "Book not found."
            if books[isbn]["borrowed"] >= books[isbn]["total_copies"]:
                return "No copies available."

            books[isbn]["borrowed"] += 1
            m["borrowed_books"].append(isbn)
            return f"Book '{books[isbn]['title']}' borrowed by {m['name']}."
    return "Member not found."


# Return a borrowed book
def return_book(member_id, isbn):
    for m in members:
        if m["id"] == member_id:
            if isbn not in m["borrowed_books"]:
                return "Book not borrowed by this member."

            m["borrowed_books"].remove(isbn)
            books[isbn]["borrowed"] -= 1
            return f"Book '{books[isbn]['title']}' returned by {m['name']}."
    return "Member not found."



# Test data
print(add_book("978123", "Python Basics", "John Doe", "Fiction", 3))
print(add_book("978456", "AI Fundamentals", "Jane Smith", "Non-Fiction", 2))

print(add_member(1, "Ramatu Kargbo"))
print(add_member(2, "Umar Kanu"))

print(borrow_book(1, "978123"))
print(borrow_book(1, "978456"))

print(return_book(1, "978123"))

print(update_book("978456", title="AI Advanced"))
print(delete_book("978123"))


