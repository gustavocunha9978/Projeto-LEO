ham = 50
cheese = 50
burgers = 100

quantity_of_burgers = float(input("How many burgers are you going to make? "))

quantity_of_cheese_kg = quantity_of_burgers * cheese
quantity_of_ham_kg = quantity_of_burgers * ham
quantity_of_burgers_kg = quantity_of_burgers * burgers

quantity_of_burgers_kg = quantity_of_burgers_kg / 1000
quantity_of_cheese_kg = quantity_of_cheese_kg / 1000
quantity_of_ham_kg = quantity_of_ham_kg /1000


print("The amount needed to make", quantity_of_burgers,"burgers: ")
print("Ham: ", quantity_of_ham_kg, "Kg")
print("Cheese:", quantity_of_cheese_kg, "Kg")
print("Burgers: ", quantity_of_burgers_kg, "Kg")