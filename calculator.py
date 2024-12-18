#!/usr/bin/env python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def read_me():
    print("\nThis is a simple Python calculator that supports the following operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("You can perform multiple operations in a loop until you choose to exit.")

def about():
    print("\nAbout this Calculator:")
    print("This calculator was created by GreatyBlue, a passionate developer.")
    print("You can find more of my work on GitHub: https://github.com/GreatyBlue")
    print("I hope you find this calculator useful for your daily tasks!")

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (×)")
        print("4. Divide (÷)")
        print("5. Read Me")
        print("6. About")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice == '5':
            read_me()
            continue
        elif choice == '6':
            about()
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} × {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} ÷ {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()
