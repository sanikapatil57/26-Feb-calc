# Calculator using OOPS

class Calculator:

    def __init__(self, first_number, operation, second_number):
        self.first_number = first_number
        self.operation = operation
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number

    def multiply(self):
        return self.first_number * self.second_number

    def divide(self):
        if self.second_number == 0:
            raise ValueError("Cannot divide by zero")
        return self.first_number / self.second_number


def main():
     while True:
        print("\n---- Simple OOPS Calculator ----")
        print("Enter 'exit' to stop the calculator")

        first_input = input("Enter first number: ")
        if first_input.lower() == "exit":
            print("Calculator Closed")
            break

        first_number = float(first_input)
        operation = input("Enter the operation (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        calculator = Calculator(first_number, operation, second_number)

        if calculator.operation == '+':
            result = calculator.add()

        elif calculator.operation == '-':
            result = calculator.subtract()

        elif calculator.operation == '*':
            result = calculator.multiply()

        elif calculator.operation == '/':
            try:
                result = calculator.divide()
            except ValueError as e:
                print(e)
                continue

        else:
            result = "Error: Invalid operation"

        print(f"Result: {result}")


if __name__ == "__main__":
    main()