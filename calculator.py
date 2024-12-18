#!/usr/bin/env python
from termcolor import colored

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
    print(colored("\nThis is a simple Python calculator that supports the following operations:", 'green'))
    print(colored("1. Addition (+)", 'cyan'))
    print(colored("2. Subtraction (-)", 'cyan'))
    print(colored("3. Multiplication (×)", 'cyan'))
    print(colored("4. Division (÷)", 'cyan'))
    print(colored("You can perform multiple operations in a loop until you choose to exit.", 'green'))

def about():
    print(colored("\nAbout this Calculator:", 'yellow'))
    print(colored("This calculator was created by GreatyBlue, a passionate developer.", 'yellow'))
    print(colored("You can find more of my work on GitHub: https://github.com/GreatyBlue", 'yellow'))
    print(colored("I hope you find this calculator useful for your daily tasks!", 'yellow'))

def calculator():
    while True:
        print("\n" + colored("Select operation:", 'magenta'))
        print(colored("1. Add (+)", 'blue'))
        print(colored("2. Subtract (-)", 'blue'))
        print(colored("3. Multiply (×)", 'blue'))
        print(colored("4. Divide (÷)", 'blue'))
        print(colored("5. Read Me", 'green'))
        print(colored("6. About", 'green'))
        print(colored("7. Exit", 'red'))

        choice = input(colored("Enter choice (1/2/3/4/5/6/7): ", 'white'))

        if choice == '7':
            print(colored("Exiting the calculator. Goodbye!", 'red'))
            break
        elif choice == '5':
            read_me()
            continue
        elif choice == '6':
            about()
            continue

        num1 = float(input(colored("Enter first number: ", 'yellow')))
        num2 = float(input(colored("Enter second number: ", 'yellow')))

        if choice == '1':
            print(colored(f"{num1} + {num2} = {add(num1, num2)}", 'green'))
        elif choice == '2':
            print(colored(f"{num1} - {num2} = {subtract(num1, num2)}", 'green'))
        elif choice == '3':
            print(colored(f"{num1} × {num2} = {multiply(num1, num2)}", 'green'))
        elif choice == '4':
            result = divide(num1, num2)
            print(colored(f"{num1} ÷ {num2} = {result}", 'green'))
        else:
            print(colored("Invalid input. Please try again.", 'red'))

if __name__ == "__main__":
    calculator()
