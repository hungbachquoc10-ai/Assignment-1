import random
code_3_digit = ""
for i in range(3):
    number = random.randint(0, 9)
    code_3_digit += str(number)
code_4_digit = ""
for i in range(4):
    number = random.randint(1, 6)
    code_4_digit += str(number)
print(f"3-digit code (0-9): {code_3_digit}")
print(f"4-digit code (1-6): {code_4_digit}")
