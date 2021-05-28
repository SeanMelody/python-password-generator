import random
import string

length = int(input("How long would you like your password?: "))

# print(length)

characters = string.ascii_letters + string.punctuation + string.digits


password = "".join(random.sample(characters, length))

print(password)
