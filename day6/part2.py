from functools import reduce

lines: list[str] = []
with open("day6/input.txt", "r") as file_in:
    lines = file_in.readlines()

def parse_line(line: str) -> int:
    return int(reduce(lambda acc, curr: acc + curr, line.split(':')[1].split()))

time = parse_line(lines[0])
distance = parse_line(lines[1])

# taken from part 1
i = 1
while i * (time - i) < distance:
    i += 1
lower_hold_limit = i
upper_hold_limit = time - i
num_methods = upper_hold_limit - lower_hold_limit + 1

print(num_methods)
