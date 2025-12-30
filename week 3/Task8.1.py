n = int(input("Enter n: "))

result = []

for i in range(1, n + 1):
    divisible = True
    for digit in str(i):
        if digit == '0' or i % int(digit) != 0:
            divisible = False
            break
    if divisible:
        result.append(i)

print("Numbers divisible by all their digits:", result)
