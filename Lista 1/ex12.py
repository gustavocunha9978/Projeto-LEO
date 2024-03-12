salary = float(input("What's your salary? "))

salary_with_increase = salary + 15/100

discounted_salary = salary_with_increase - 8/100


print(f"Starting salary is R$ {salary:.3f}")
print(f"Salary with 15% is R$ {salary_with_increase:.3f}")
print(f"Salary with 8% less is R$ {discounted_salary:.3f}") 