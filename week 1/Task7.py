a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

print(a + b if op == '+' else
      a - b if op == '-' else
      a * b if op == '*' else
      "Error: Division by zero" if op == '/' and b == 0 else
      a / b if op == '/' else
      "Invalid operation")
