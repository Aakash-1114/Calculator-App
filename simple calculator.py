print("Simple Calculator App")
print("Type 'exit' anytime to quit.\n")

while True:
    num1 = input("Enter first number: ")
    if num1.lower() == "exit":
        print("Exiting calculator... Goodbye!")
        break

    num2 = input("Enter second number: ")
    if num2.lower() == "exit":
        print("Exiting calculator... Goodbye!")
        break

    op = input("Enter operation (+, -, *, /): ")
    if op.lower() == "exit":
        print("Exiting calculator... Goodbye!")
        break

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid number input! Please enter numbers only.\n")
        continue

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero!\n")
            continue
        result = num1 / num2
    else:
        print("Invalid operation! Use +, -, *, or /.\n")
        continue

    print(f"Result: {num1} {op} {num2} = {result}\n")



