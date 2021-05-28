#!/usr/bin/env python # -*- coding: UTF-8 -*-
print('Content-type: text/html\r\n\r')

length = int(input("How long would you like your password?: "))

# print(length)


characters = string.ascii_letters + string.punctuation + string.digits

# password = "".join(choice(characters)
#                    for x in range(randint(characters, length)))

password = "".join(random.sample(characters, length))

print(password)
