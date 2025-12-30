def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def subtract_fractions(A, B, C, D):
    numerator = A * D - B * C
    denominator = B * D
    common = gcd(abs(numerator), denominator)
    return numerator // common, denominator // common

# Ввод дробей
A = int(input("Enter numerator A: "))
B = int(input("Enter denominator B: "))
C = int(input("Enter numerator C: "))
D = int(input("Enter denominator D: "))

num, den = subtract_fractions(A, B, C, D)
print(f"Result of subtraction = {num}/{den}")

