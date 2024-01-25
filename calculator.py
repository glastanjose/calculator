# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Main program loop
while True:
    # Display menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'quit' to end the program")

    # User input
    user_input = input(": ")

    # Check if the user wants to quit
    if user_input == "quit":
        break

    # Check for valid operation
    if user_input in ("add", "subtract"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
    else:
        print("Invalid input")