def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

# Ввод массива
m = int(input("Enter length of array: "))
A = []
print("Enter elements:")
for _ in range(m):
    A.append(int(input()))

print("Original array:", A)

swap_first_last(A)

print("Array after swap:", A)
