import random
import string

characters = ""

# capsCar = string.ascii_letters
capsCar = string.ascii_uppercase
specialCar = [",", "-", "!", "@", "#", "$", "&"]
numberCar = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

length = int(input("How long would you like your password?: "))

caps = input(
    "Would you like capital letters in your password?: (Enter yes or no): ").lower()


special = input(
    "Would you like special characters in your password?: (Enter yes or no): ").lower()

number = input(
    "Would you like numbers in your password?: (Enter yes or no): ").lower()


if caps == "yes":
    characters = characters + capsCar
elif caps == "no":
    print("No capital letters will be used")
else:
    print("Must type yes or no")


if special == "yes":
    characters = characters + string.punctuation
elif special == "no":
    print("No special characters will be used")
else:
    print("Must type yes or no")


if number == "yes":
    characters = characters + string.digits
elif special == "no":
    print("No numbers will be used")
else:
    print("Must type yes or no")


password = "".join(random.sample(characters, length))

print("Your new password is: " + password)
