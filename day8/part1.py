import re

lines: list[str] = []
with open("day8/input.txt", "r") as file_in:
    lines = file_in.readlines()

instructions = lines[0].strip()

nodes: dict[str, tuple[str, str]] = {}
for line in lines[2:]:
    m = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line.strip())
    if m:
        nodes[m.group(1)] = (m.group(2), m.group(3))

position = "AAA"
i = 0
while position != "ZZZ":
    direction = instructions[i % len(instructions)]
    position = nodes[position][0 if direction == "L" else 1]
    i += 1

print(i)
