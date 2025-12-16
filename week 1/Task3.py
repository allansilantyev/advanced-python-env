A = float(input("Enter a number with 2 decimals: "))
integer_part = int(A)
fraction_part = round((A - integer_part) * 100)
new_number = fraction_part + integer_part / 100
print(f"{new_number:.2f}")
