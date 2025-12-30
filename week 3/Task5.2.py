n = int(input("Enter a number: "))

divisors = [str(i) for i in range(1, n + 1) if n % i == 0]

print("Divisors:", ' '.join(divisors))
