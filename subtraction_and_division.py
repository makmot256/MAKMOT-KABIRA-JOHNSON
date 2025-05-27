# Subtraction and Division of two numbers

# Input from the user
num1 = float(input("Enter first number: "))
num3 = float(input("Enter second number: "))

# Subtract the numbers
difference = num1 - num3

# Divide the numbers, with a check to avoid division by zero
if num3 != 0:
    quotient = num1 / num3
else:
    quotient = "Undefined (division by zero)"

# Display the results
print("The difference is:", difference)
print("The quotient is:", quotient)
