allowed = set("ABCEHKMOPTXY")
n = int(input())

for _ in range(n):
    plate = input().strip()

    ok = (
        len(plate) == 6 and
        plate[0] in allowed and
        plate[1:4].isdigit() and
        plate[4] in allowed and
        plate[5] in allowed
    )

    print("Yes" if ok else "No")
