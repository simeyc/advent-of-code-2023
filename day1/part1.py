with open("input.txt", "r") as file_in:
    lines = file_in.readlines()

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

result = 0
for line in lines:
    digits = [char for char in line if char in DIGITS]
    result += int(digits[0] + digits[-1])

print(result)
