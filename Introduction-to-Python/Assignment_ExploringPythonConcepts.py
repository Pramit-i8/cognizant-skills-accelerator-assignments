#Task 1: Variables - Your First Python Intro python

# Defining variables
name = "Guarav"      # Name of the person
age = 35           # Age of the person
height = 5.9       # Height in feet

# Printing a friendly message
print(f"Hey there, my name is {name}! I’m {age} years old and {height} feet tall.")


#Task 2: Operators - Playing with Numbers

# Pick two numbers
num1 = 10
num2 = 3

# Performing operations
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

# Displaying results with friendly messages
print(f"The sum of {num1} and {num2} is {sum_result}.")
print(f"The difference when you subtract {num2} from {num1} is {sub_result}.")
print(f"The product of {num1} and {num2} is {mul_result}.")
print(f"The division of {num1} by {num2} is {div_result}. (Don't worry, no division by zero here!)")


#Task 3: Conditional Statements - The Number Checker

# Asking the user to enter a number
number = float(input("Enter a number: "))

# Checking if the number is positive, negative, or zero
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")