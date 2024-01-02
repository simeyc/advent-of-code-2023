lines = []
with open("input.txt", "r") as file_in:
    while line := file_in.readline().strip():
        lines.append(line)

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def pick_number_positions(
    number_positions: dict[int, str],
    symbol_positions: list[int],
    line_index: int,
    selections: dict[str, list[int]] = {}
):
    for num_pos, num in number_positions.items():
        for sym_pos in symbol_positions:
            if sym_pos >= num_pos - 1 and sym_pos <= num_pos + len(num):
                key = f"{line_index}_{sym_pos}"
                selections[key] = [*selections[key], int(num)] if key in selections else [int(num)]
                break
    return selections


prev_symbol_positions: list[int] = []
prev_number_positions: dict[int, str] = {}
selections: dict[str, list[int]] = {}
for i, line in enumerate(lines):
    curr_symbol_positions: list[int] = []
    curr_number_positions: dict[int, str] = {}
    
    j = 0    
    while j < len(line):
        if line[j] in DIGITS:
            # Read whole number.
            curr_number_positions[j] = ""
            k = j
            while k < len(line) and line[k] in DIGITS:
                curr_number_positions[j] += line[k]
                k += 1
            print(f"found number {curr_number_positions[j]} at line {i} pos {j}")
            j = k
        else:
            if line[j] == "*":
                curr_symbol_positions.append(j)
                print(f"found symbol {line[j]} at line {i} pos {j}")
            j += 1

    selections = pick_number_positions(prev_number_positions, curr_symbol_positions, i, selections)
    selections = pick_number_positions(curr_number_positions, prev_symbol_positions, i - 1, selections)
    selections = pick_number_positions(curr_number_positions, curr_symbol_positions, i, selections)

    prev_number_positions = curr_number_positions
    prev_symbol_positions = curr_symbol_positions

result = 0
for key, vals in selections.items():
    print(f"{key}: {vals}")
    if len(vals) == 2:
        result += vals[0] * vals[1]

print(f"result: {result}")
