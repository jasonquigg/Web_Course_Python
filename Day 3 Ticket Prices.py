print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    bill = 0

    if age < 12:
        bill = 5
        print(f"${bill}")
    elif age <= 18:
        bill = 7
        print(f"${bill}")
    else:
        bill = 12
        print(f"${bill}")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"You final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
