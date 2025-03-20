# Task 1: Countdown Timer
start_number = int(input("Enter the starting number: "))

while start_number > 0:
    print(start_number, end=" ")
    start_number -= 1  # Decrement the number by 1

print("Blast off to LightYear! 🚀")

# Task 2: Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Task 3: Find the Factorial
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i  # Multiply the current value of factorial by i

print(f"The factorial of {num} is {factorial}.")

