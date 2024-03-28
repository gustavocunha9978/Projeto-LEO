normal_time = 10
extra_time = 15
tax = 0.10

normal_time_input = float(input("Enter the number of normal hours worked: "))
overtime = float(input("Enter the number of overtime hours worked: "))

gross_salary = (normal_time_input * normal_time ) + (overtime + extra_time)

value_tax = tax * gross_salary

net_salary = gross_salary - value_tax

print(gross_salary)
print(net_salary)