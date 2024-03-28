one = int(input("How many 1 cent coins do you have? "))
five = int(input("How many 5 cent coins do you have? "))
ten = int(input("How many 10 cent coins do you have? "))
twenty_five = int(input("How many 25 cent coins do you have? "))
fifty = int(input("How many 50 cent coins do you have? "))
one_dollar =  int(input("How many $1 coins do you have? "))

total = (one * 1) + (five * 5) + (ten * 10) + (twenty_five * 25) + (fifty * 50)  + (one_dollar * 100)
Total_dollar = total / 100

print(("$"),Total_dollar)