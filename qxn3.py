# question3.py

# ============================================================================
# Question 3.i - Student Marks Dictionary
# ============================================================================
def student_marks_demo():

    students = {
        "Nicole": 85,
        "Ashley": 92,
        "Noku": 78,
        "Don": 95,
        "Eve": 88
    }

    # Display all students and their marks
    print("\n=== Student Marks ===")
    for name, mark in students.items():
        print(f"{name}: {mark}")

    # Find the student with the highest mark
    # Using max() on dictionary items with a key that compares marks
    top_student, top_mark = max(students.items(), key=lambda item: item[1])
    print(f"\nStudent with the highest mark: {top_student} with {top_mark} marks")


# ============================================================================
# Question 3.ii - Book Class
# ============================================================================
class Book:


    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        """Displays the book's details."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print()  # Blank line for readability


# ============================================================================
# Main execution to demonstrate both parts
# ============================================================================
if __name__ == "__main__":
    # Part 3.i
    print("=" * 50)
    print("Question 3.i - Student Marks")
    print("=" * 50)
    student_marks_demo()

    # Part 3.ii
    print("\n" + "=" * 50)
    print("Question 3.ii - Book Class")
    print("=" * 50)

    # Create two book objects
    book1 = Book("The Great Rat", "F. Nicole Ncube", 12.99)
    book2 = Book("To Kill a bird", "Ashley Moyo", 10.49)

    # Display book details
    print("\nBook 1 Details:")
    book1.display_details()

    print("Book 2 Details:")
    book2.display_details()