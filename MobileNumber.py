import random

def generate_mobile_number():
    mobile_number = str(random.choice([7, 8, 9]))  # start with 7, 8, or 9
    while True:
        digits = ''.join(random.choices('0123456789', k=9))
        if max(digits.count(digit) for digit in digits) <= 6:  # check if no digit occurs more than 6 times
            return mobile_number + digits

mobile_numbers = [generate_mobile_number() for i in range(1048575)]
mobile_numbers.sort()
k=6291450
with open("Table/MobileNumber9.txt", "w") as f:
    for i, number in enumerate(mobile_numbers, start=1):
        number_str = str(number)
        f.write(f"{str(i+k).ljust(4)}{number_str.rjust(15)}\n")
        # print(f"{str(i).ljust(4)}{number_str.rjust(15)}")
print("Done")
print(i+k)