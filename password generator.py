import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz()[]/\+=@#$%&:{}"
length_of_password=int(input("Enter the length of the password: "))
n="".join(random.sample(password,length_of_password))
print(f"Your password is {n}")
