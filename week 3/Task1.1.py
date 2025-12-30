print("Choose a shape:")
print("1 - Circle")
print("2 - Rectangle")
print("3 - Triangle")

choice = int(input("Enter choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = 3.14159 * r * r
    print("Area of circle =", area)

elif choice == 2:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    area = a * b
    print("Area of rectangle =", area)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of triangle =", area)

else:
    print("Invalid choice")
