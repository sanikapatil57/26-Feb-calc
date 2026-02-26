# Simple Calculator using Python

while True:
    print("\n----- Simple Calculator -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == '5':
        print("Calculator Closed")
        break

    # Taking numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Conditional statements
    if choice == '1':
        print("Result =", num1 + num2)

    elif choice == '2':
        print("Result =", num1 - num2)

    elif choice == '3':
        print("Result =", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error! Division by zero not allowed.")

    else:
        print("Invalid choice! Please select correct option.")