number1 = input("Please insert the first number: ")
number2 = input("please insert the second number: ")
operation = input("Please insert your desird operation among: +, -, *, /, **: ")

if operation == "+":
    result = float(number1) + float(number2)
elif operation == "-":
    result = float(number1) - float(number2)
elif operation == "*":
    result = float(number1) * float(number2)
elif operation == "/":
    result = float(number1) / float(number2)
elif operation == "**":
    result = float(number1) ** float(number2)
else:
    result = "The operation inserted by the user is wrong!"

print(result)