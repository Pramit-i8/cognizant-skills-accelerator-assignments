import logging

# Set up logging to log errors to a file named error_log.txt
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Oops! Division by zero is not allowed.")
        return x / y
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError occurred: {e}")
        return str(e)
    except ValueError:
        logging.error(f"ValueError occurred: Invalid input.")
        return "Invalid input! Please enter a valid number."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

def calculator():
    print("Welcome to the Error-Free Calculator!")
    
    while True:
        # Display menu
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Get the user's choice
        choice = input("> ")

        if choice == '1':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid operation (1-5).")

if __name__ == "__main__":
    calculator()
