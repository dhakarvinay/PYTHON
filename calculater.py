def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

# Get the two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operator from the user
operator = input("Enter the operator (+, -, *, /): ")

# Calculate the result
result = calculate(num1, num2, operator)

# Print the result
print(result)
