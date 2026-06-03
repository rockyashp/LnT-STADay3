def calculate(a, op, b):
    return eval(f"{a}{op}{b}")

a = int(input("First number: "))
op = input("Operation: ")
b = float(input("Second number: "))
print(f"Result: {calculate(a, op, b)}")
