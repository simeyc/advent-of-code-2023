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

# Assume every path includes only one Z endpoint, and after reaching the Z, eventually loops back.
# Find the steps to first Z, and number of steps in the loop. Maybe there'll be a shortcut to the answer...
positions = [key for key in nodes if key.endswith("A")]
steps_to_first_z = [0] * len(positions)
steps_in_loop = [0] * len(positions)
i = 0
while not all(steps_in_loop):
    for j, pos in enumerate(positions):
        if not steps_in_loop[j] and pos.endswith("Z"):
            if steps_to_first_z[j]:
                steps_in_loop[j] = i - steps_to_first_z[j]
            else:
                steps_to_first_z[j] = i

    # take next step
    direction = instructions[i % len(instructions)]
    k = 0 if direction == "L" else 1
    positions = [nodes[pos][k] for pos in positions]
    i += 1

# Turns out steps_in_loop == steps_to_first_z. Increment steps by the smallest loop until we land on a
# product of all loop sizes.
min_steps = min(steps_in_loop)
i = 0
num_steps = min_steps
while not all(num_steps % n == 0 for n in steps_in_loop):
    num_steps += min_steps

print(num_steps)
