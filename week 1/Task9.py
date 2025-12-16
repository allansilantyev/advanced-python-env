ticket = input("Enter a 6-digit ticket number: ")

if len(ticket) == 6 and ticket.isdigit():
    first_three = sum(map(int, ticket[:3]))
    last_three = sum(map(int, ticket[3:]))
    print("YES" if first_three == last_three else "NO")
else:
    print("Invalid ticket number")
