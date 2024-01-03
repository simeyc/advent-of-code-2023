# Should work in theory, but waaayy too slow!

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

positions = [key for key in nodes if key.endswith("A")]
i = 0
while not all(pos.endswith("Z") for pos in positions):
    direction = instructions[i % len(instructions)]
    j = 0 if direction == "L" else 1
    positions = [nodes[pos][j] for pos in positions]
    i += 1

print(i)
