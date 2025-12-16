salaries = list(map(int, input("Enter salaries separated by spaces: ").split()))
print(max(salaries) - min(salaries))
