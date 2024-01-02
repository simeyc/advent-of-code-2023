# NOT CORRECT!
from functools import cmp_to_key

lines: list[str] = []
with open("day7/input.txt", "r") as file_in:
    lines = file_in.readlines()

hands: list[tuple[str, int]] = []
for line in lines:
    [x, y] = line.split()
    hands.append((x, int(y)))

CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
CARD_RANKS = {x: i for i, x in enumerate(reversed(CARDS))}


def compare_cards(card_a: str, card_b: str):
    return (0 if card_a == card_b
            else 1 if CARD_RANKS[card_a] > CARD_RANKS[card_b]
            else -1)


def compare_same_type(cards_a: str, cards_b: str):
    result = 0
    for card_a, card_b in zip(cards_a, cards_b):
        result = compare_cards(card_a, card_b)
        if result != 0: 
            break
    return result


def get_counts(cards: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for x in cards:
        counts[x] = counts.get(x, 0) + 1
    return counts


def get_highest_ranking(cards: str) -> str:
    for x in CARDS:
        if x in cards:
            return x
    return CARDS[-1]


def convert_jokers(cards: str) -> str:
    if "J" not in cards:
        return cards
    
    if cards == "JJJJJ":
        return "AAAAA"
    
    counts = get_counts(cards.replace("J", ""))
    max_count = max(counts.values())

    if max_count == 1:
        # no duplicate cards, convert jokers to match highest ranking
        return cards.replace("J", get_highest_ranking(cards))

    # convert jokers to highest ranking duplicated card
    most_frequent_cards: str = ""
    for key, value in counts.items():
        if value == max_count:
            most_frequent_cards += key
    return cards.replace("J", get_highest_ranking(most_frequent_cards))


def compare_hands(hand_a: tuple[str, int], hand_b: tuple[str, int]) -> int:
    cards_a = convert_jokers(hand_a[0])
    cards_b = convert_jokers(hand_b[0])

    if cards_a != hand_a[0]:
        print(f"Converted {hand_a[0]} to {cards_a}")
    if cards_b != hand_b[0]:
        print(f"Converted {hand_b[0]} to {cards_b}")

    num_unique_a, num_unique_b = len(set(cards_a)), len(set(cards_b))
    
    if num_unique_a != num_unique_b:
        # one hand definitely has a higher type than the other
        return 1 if num_unique_a < num_unique_b else -1
    
    if num_unique_a in [1, 5]:
        # hands are both of type Five-of-a-kind or High-card; shortcut
        return compare_same_type(cards_a, cards_b)
    
    counts_a, counts_b = get_counts(cards_a), get_counts(cards_b)
    max_count_a, max_count_b = max(counts_a.values()), max(counts_b.values())

    if max_count_a == max_count_b:
        # hands have same type
        return compare_same_type(cards_a, cards_b)

    return 1 if max_count_a > max_count_b else -1


sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

result = 0
for i, (_cards, bid) in enumerate(sorted_hands):
    result += (i + 1) * bid

print(result)
