# Step 1: Ask the user for their age
age = int(input("How old are you? "))  # Convert input to an integer

# Step 2: Decide the eligibility
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    years_to_wait = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {years_to_wait} more years to go!")