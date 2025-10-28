 # demo.py
# Demonstration script for Mini Library Management System
# By: Ramatu I. Kargbo

from operations import *  # import all functions from operations.py

# -----------------------------
# 1. ADD BOOKS
# -----------------------------
print(add_book("978123", "Python Basics", "John Doe", "Fiction", 3))
print(add_book("978456", "AI Fundamentals", "Jane Smith", "Non-Fiction", 2))
print(add_book("978789", "Space Journey", "Michael Star", "Sci-Fi", 4))

# -----------------------------
# 2. ADD MEMBERS
# -----------------------------
print(add_member(1, "Ramatu Kargbo"))
print(add_member(2, "Umar Kanu"))

# -----------------------------
# 3. BORROW BOOKS
# -----------------------------
print(borrow_book(1, "978123"))
print(borrow_book(1, "978456"))
print(borrow_book(2, "978789"))

# -----------------------------
# 4. RETURN A BOOK
# -----------------------------
print(return_book(1, "978123"))

# -----------------------------
# 5. UPDATE BOOK DETAILS
# -----------------------------
print(update_book("978456", title="AI Advanced", total_copies=3))

# -----------------------------
# 6. DELETE BOOK AND MEMBER
# -----------------------------
print(delete_book("978789"))
print(delete_member(2))