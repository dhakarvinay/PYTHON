from calculater import calculate


num1=input("value 1:")
num2=input("value 2:")
x=input("enter the arithmetic operation(+,-,*,/)")  
if x =="+":
    print("sum of two values:",int(num1)+int(num2))
elif x=="-":
    print("substraction of two values:",int(num1)-int(num2))
elif x=="*":
    print("multiplication of two values: ",int(num1)*int(num2))
elif x=="/":
    print("devision of two values:",int(num1)/int(num2))
else:
    print("Wrong Input")
while True:
    # Get the two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get the operator from the user
    operator = input("Enter the operator (+, -, *, /): ")

    # Calculate the result
    result = calculate(num1, num2, operator)

    # Print the result
    print(result)

    # Ask the user if they want to continue
    continue_calculating = input("Do you want to continue calculating? (y/n): ")

    # If the user says no, break out of the loop
    if continue_calculating != "y":
        break
