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
    possible = True
    for set_result in sets:
        [reds, greens, blues] = get_set_totals(set_result)
        print(set_result)
        print(reds, greens, blues)
        possible = reds <= 12 and greens <= 13 and blues <= 14
        if not possible:
            break
    if possible:
        result += game_id

print(result)