# question1.py
def get_valid_age():

    while True:
        try:
            age = int(input("Please enter your age: "))
            print(f"Your age is: {age}")
            break  # Exit loop if valid integer is entered
        except ValueError:
            print("Invalid input. Please enter a valid integer for your age.")

# Call the function to run it
if __name__ == "__main__":
    get_valid_age()