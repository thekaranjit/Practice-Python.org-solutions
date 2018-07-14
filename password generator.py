import string
import random

symbols  = string.punctuation
letters = string.ascii_letters
small_lettrs = string.ascii_lowercase
capital_letter = string.ascii_uppercase
num_digit = string.digits
letter_digit = string.hexdigits

length_password = int(input("Please input the length of password you need"))

gen_pass  = random.sample(range(letter_digit), length_password)

print(gen_pass)

