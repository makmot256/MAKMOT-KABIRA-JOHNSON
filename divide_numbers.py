# Assignment Two:
# Write a program to handle errors, the program should ask for two number using input and then divides them. Use an infinite loop to keep asking until a valid input is provide.

def divide_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero number.")

divide_numbers()