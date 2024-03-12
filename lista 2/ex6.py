num1 = int(input("Put a number: "))
num2 = int(input("Put a number: "))
num3 = int(input("Put a number: "))

if num1 < num2:
    num1, num2 = num2, num1
if num1 < num3:
    num1, num3 = num3, num1
if num2 < num3:
    num2, num3 = num3, num2

print("Numbers in descending order:", num1, ",", num2, ",", num3)