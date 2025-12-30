def is_inside_circle(x, y, R):
    return x**2 + y**2 < R**2

# Ввод радиуса круга
R = float(input("Enter radius of circle: "))

# Ввод координат точек
points = []
points.append((float(input("Enter p1: ")), float(input("Enter p2: "))))
points.append((float(input("Enter f1: ")), float(input("Enter f2: "))))
points.append((float(input("Enter l1: ")), float(input("Enter l2: "))))

count = 0
for x, y in points:
    if is_inside_circle(x, y, R):
        count += 1

print(f"Number of points inside the circle: {count}")
