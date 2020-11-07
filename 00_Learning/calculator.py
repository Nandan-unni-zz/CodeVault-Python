a = float(input("Enter first number: "))
op = input("Enter the operator: ")
b = float(input("Enter second number: "))
isValid = True
if op == '+':
    c = a + b
elif op == '-':
    c = a - b
elif op == '*':
    c = a * b
elif op == '/':
    if b == 0:
        print("\ndivision by 0 is not possible !")
        isValid = False
    else:
        c = a / b
elif op == '^':
    c = a ** b
elif op == '%':
    c = a % b
else:
    print("\nInvalid Operator !")
    isValid = False
if isValid:
    print("\n", a, op, b, "=", c)
