for i in range(1, 4):
    print(f"\nArray {i}")
    n = int(input("Enter size (<= 15): "))

    arr = []
    print("Enter elements:")
    for j in range(n):
        arr.append(int(input()))

    total = sum(arr)
    average = total / n

    print("Sum =", total)
    print("Average =", average)
