lines: list[str] = []
with open("input.txt", "r") as file_in:
    while line := file_in.readline().strip():
        lines.append(line)

# Start with one of every card.
card_counts = [1] * len(lines)
for i, line in enumerate(lines):
    line = line.split(": ")[-1]
    [winning_numbers, card_numbers] = line.split(" | ")
    winning_numbers = [int(x) for x in winning_numbers.split()]
    card_numbers = [int(x) for x in card_numbers.split()]
    num_matches = len([x for x in card_numbers if x in winning_numbers])
    # Add the number of instances we have of this card to the totals for
    # the next `num_matches` cards.
    for j in range(num_matches):
        card_counts[i + j + 1] += card_counts[i]

total_cards = sum(card_counts)
print(total_cards)
