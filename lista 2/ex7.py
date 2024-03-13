
height = float(input("Tell us your height: "))
sex = input("What's your sex? (male or female): ")


if sex.lower() == 'male':
    weight_male = (72.7 * height) - 58
    print (f"Your ideal weight according to your height {weight_male:.2f}")

elif sex.lower() == 'female':
    weight_fem = (62.1 * height) - 44.7
    print (f"Your ideal weight according to your height {weight_fem:.2f}")