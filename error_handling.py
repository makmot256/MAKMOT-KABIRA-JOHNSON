# Execrise Five:
# Raise a custom exception that checks for positive number .

def check_positive_number(num):
    if num > 0:
        return num
    else:
        raise ValueError("Number must be positive")
    
try:
    num = int(input("Enter a positive number: "))
    result = check_positive_number(num)
    print(f"Valid input: {result}")
except ValueError as e:
    print(f"Error: {e}")


