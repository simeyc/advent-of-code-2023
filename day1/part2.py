with open("input.txt", "r") as file_in:
    lines = file_in.readlines()

DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

result = 0
for line in lines:
    digits = []
    for i in range(len(line)):
        if line[i] in DIGITS:
            digits.append(line[i])
        else:
            for j, word in enumerate(WORDS):
                if line[i:].startswith(word):
                    digits.append(DIGITS[j])
                    break
        if len(digits):
            break

    for i in reversed(range(len(line))):
        if line[i] in DIGITS:
            digits.append(line[i])
        else:
            for j, word in enumerate(WORDS):
                if line[:i+1].endswith(word):
                    digits.append(DIGITS[j])
                    break
        if len(digits) > 1:
            break
    
    result += int(digits[0] + digits[1])

print(result)
