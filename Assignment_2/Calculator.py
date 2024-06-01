# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to find the power of a number
def power(x, y):
    return x ** y

# Function to find the modulus of two numbers
def modulus(x, y):
    return x % y

# Main function to run the calculator
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    
    while True:
        # Take input from the user for operation
        choice = input("Enter choice (1/2/3/4/5/6) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                # Take input from the user for numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of division is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result of power is: {power(num1, num2)}")
            elif choice == '6':
                print(f"The result of modulus is: {modulus(num1, num2)}")
        else:
            print("Invalid input! Please select a valid operation.")

# Run the calculator function
if __name__ == "__main__":
    calculator()
