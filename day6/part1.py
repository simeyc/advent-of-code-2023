from functools import reduce

lines: list[str] = []
with open("day6/input.txt", "r") as file_in:
    lines = file_in.readlines()

times = [int(x) for x in lines[0].split(':')[1].split()]
distance = [int(x) for x in lines[1].split(':')[1].split()]

# race distance increases with increased hold time to a certain point,
# then decreases in a symmetrical pattern
# example for 7ms race (hold_time * remaining_time):
# 1*6 = 6
# 2*5 = 10
# 3*4 = 12
# 4*3 = 12
# 5*2 = 10
# 6*1 = 6
# example for 6ms race:
# 1*5 = 5
# 2*4 = 8
# 3*3 = 9
# 4*2 = 8
# 5*1 = 5

num_methods: list[int] = []
for time, distance in zip(times, distance):
    # find lower hold time to beat record
    i = 1
    while i * (time - i) < distance:
        i += 1
    lower_hold_limit = i
    upper_hold_limit = time - i
    num_methods.append(upper_hold_limit - lower_hold_limit + 1)

print(reduce(lambda acc, curr: acc * curr, num_methods))
