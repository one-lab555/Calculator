def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'q' to quit\n")

    while True:
        op = input("Choose operation (+, -, *, /) or 'q': ").strip()
        if op.lower() == 'q':
            print("Goodbye!")
            break

        if op not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)

        print(f"Result: {result}\n")

if __name__ == "__main__":
    calculator()
