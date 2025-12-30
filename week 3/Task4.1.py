def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def divide_fractions(A, B, C, D):
    numerator = A * D
    denominator = B * C
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common

# Ввод дробей
A = int(input("Enter numerator A: "))
B = int(input("Enter denominator B: "))
C = int(input("Enter numerator C: "))
D = int(input("Enter denominator D: "))

num, den = divide_fractions(A, B, C, D)
print(f"Result of division = {num}/{den}")
