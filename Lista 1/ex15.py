total_bill = float(input("What's the total bill amount? "))

per_person = total_bill / 3
carlos_andre_share = int(per_person)
felipe_share = total_bill - 2 * carlos_andre_share

print(f"Carlos should pay: ${carlos_andre_share:.2f}")
print(f"André should pay: ${carlos_andre_share:.2f}")
print(f"Felipe should pay: ${felipe_share:.2f}")
