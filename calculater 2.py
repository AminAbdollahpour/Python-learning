num1 = float(input("Enter your first number:"))
op = input("Enter your operater:")
num2 = float(input("Enter your second number:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operater")
