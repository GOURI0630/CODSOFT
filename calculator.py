print("Welcome to Calculator")
print("Operations: +, -, *, /")

while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero not allowed")
    else:
        print("Invalid operator")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Calculator closed.")
        break
