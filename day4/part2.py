lines: list[str] = []
with open("input.txt", "r") as file_in:
    while line := file_in.readline().strip():
        lines.append(line)

total_cards = len(lines)
rounds: list[tuple[int, int]] = [(0, len(lines))]
while rounds:
    start, length = rounds.pop(0)
    #print(f"NEXT ROUND: {start}, {length}")
    for j, line in enumerate(lines[start: start + length]):
        line = line.split(": ")[-1]
        [winning_numbers, card_numbers] = line.split(" | ")
        winning_numbers = [int(x) for x in winning_numbers.split()]
        card_numbers = [int(x) for x in card_numbers.split()]
        num_matches = len([x for x in card_numbers if x in winning_numbers])
        #print(f"winning_numbers: {winning_numbers}, card_numbers: {card_numbers}, num_matches: {num_matches}")
        if num_matches:
            total_cards += num_matches
            print(f"total: {total_cards}")
            rounds.append((start + j + 1, num_matches))

print(total_cards)