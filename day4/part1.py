lines = []
with open("input.txt", "r") as file_in:
    while line := file_in.readline().strip():
        lines.append(line)

result = 0
for line in lines:
    line = line.split(": ")[-1]
    [winning_numbers, card_numbers] = line.split(" | ")
    winning_numbers = [int(x) for x in winning_numbers.split()]
    card_numbers = [int(x) for x in card_numbers.split()]
    num_matches = len([x for x in card_numbers if x in winning_numbers])
    points = pow(2, num_matches - 1) if num_matches >= 1 else 0
    result += points

print(result)