class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Error: Division by zero")

    def clear(self):
        self.result = 0


# Usage example
calc = Calculator()

while True:
    print("Current Result:", calc.result)
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number to add: "))
        calc.add(num)
    elif choice == 2:
        num = int(input("Enter a number to subtract: "))
        calc.subtract(num)
    elif choice == 3:
        num = int(input("Enter a number to multiply: "))
        calc.multiply(num)
    elif choice == 4:
        num = int(input("Enter a number to divide: "))
        calc.divide(num)
    elif choice == 5:
        calc.clear()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")

    print()

print("Final Result:", calc.result)
