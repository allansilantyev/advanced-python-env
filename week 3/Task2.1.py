import math

def triangle_area(base, height):
    return 0.5 * base * height

a = float(input("Enter side of hexagon: "))

# высота равностороннего треугольника
h = (math.sqrt(3)/2) * a

# площадь одного треугольника
area_tri = triangle_area(a, h)

# площадь шестиугольника = 6 треугольников
area_hex = 6 * area_tri

print("Area of regular hexagon =", area_hex)
