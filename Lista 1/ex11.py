import datetime

accident_date_str = input(
    "What was the date of the last accident? (format: YYYY-MM-DD) ")
accidents_of_last_accident = datetime.datetime.strptime(
    accident_date_str, "%Y-%m-%d")
date_now = datetime.datetime.now()

converter = date_now.date() - accidents_of_last_accident.date()

days = converter.days
years, days = divmod(converter.days, 365)
months, days = divmod(days, 30)

print(f"Since {accidents_of_last_accident.date()} there have been {years} years, {months} months, {days} days")