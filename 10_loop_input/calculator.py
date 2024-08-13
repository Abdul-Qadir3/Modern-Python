import sys  # Import the sys module, which provides access to command-line arguments and other system-related functions.

def calculator():
    # Check if the number of arguments passed to the script is exactly 4 (script name, number1, operation, number2).
    # If not, print usage instructions and return (exit the function).
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <number1> <operation> <number2>")
        print("Example: python calculator.py 5 + 3")
        return
    
    # Attempt to convert the first and third arguments to floats and store them as num1 and num2.
    # Also, store the second argument as the operation.
    # If conversion fails (e.g., if the user didn't enter numbers), catch the ValueError and print an error message.
    try:
        num1 = float(sys.argv[1])  # Convert the first argument (number1) to a float.
        operation = sys.argv[2]    # Store the second argument (operation, e.g., +, -, *, /).
        num2 = float(sys.argv[3])  # Convert the third argument (number2) to a float.
    except ValueError:
        print("Please provide valid numbers.")  # If conversion fails, print this error message.
        return  # Exit the function.
    
    # Perform the calculation based on the operation provided.
    # Check which operation was passed (+, -, *, or /), and perform the corresponding arithmetic operation.
    if operation == '+':
        result = num1 + num2  # Addition
    elif operation == '-':
        result = num1 - num2  # Subtraction
    elif operation == '*':
        result = num1 * num2  # Multiplication
    elif operation == '/':
        if num2 != 0:  # Check if the divisor (num2) is not zero to avoid division by zero error.
            result = num1 / num2  # Division
        else:
            print("Error: Division by zero is not allowed.")  # Print error message if division by zero is attempted.
            return  # Exit the function.
    else:
        print("Invalid operation. Use one of the following: +, -, *, /")  # If an unsupported operation is provided, print this error.
        return  # Exit the function.
    
    # If the operation was successful, print the result of the calculation.
    print(f"The result of {num1} {operation} {num2} is: {result}")

# This block ensures that the calculator function only runs if the script is executed directly (not imported as a module).
if __name__ == "__main__":
    calculator()  # Call the calculator function to perform the calculation based on user input.