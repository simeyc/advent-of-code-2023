with open("input.txt", "r") as file_in:
    lines = file_in.readlines()


def get_set_totals(set_result):
    result = [0, 0, 0]
    for count in set_result.split(", "):
        for i, color in enumerate(["red", "green", "blue"]):
            if count.endswith(color):
                result[i] = int(count[:-(len(color) + 1)])
    return result

result = 0
for i, line in enumerate(lines):
    game_id = i + 1
    sets = line[len(f"Game {game_id}: "):-1].split("; ")
    min_reds, min_greens, min_blues = 0, 0, 0
    for set_result in sets:
        [reds, greens, blues] = get_set_totals(set_result)
        min_reds = max(reds, min_reds)
        min_greens = max(greens, min_greens)
        min_blues = max(blues, min_blues)
    result += min_reds * min_greens * min_blues

print(result)