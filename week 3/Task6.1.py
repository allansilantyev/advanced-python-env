def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))

g = gcd(A, B)
l = lcm(A, B)

print(f"GCD = {g}")
print(f"LCM = {l}")
