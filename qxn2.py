# question2.py
def save_and_display_fruits():

    fruits = ["Apple", "Banana", "Orange", "Strawberry", "Mango"]

    # Write fruits to the file
    with open("fruits.txt", "w") as file:
        for fruit in fruits:
            file.write(fruit + "\n")

    # Read and display fruits from the file
    with open("fruits.txt", "r") as file:
        print("\nFruits from file:")
        for line in file:
            print(line.strip())  # strip removes the newline character

# Call the function to run it
if __name__ == "__main__":
    save_and_display_fruits()