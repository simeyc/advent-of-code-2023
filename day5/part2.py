# FAILED!

from enum import Enum

lines: list[str] = []
with open("day5/input.txt", "r") as file_in:
    lines = file_in.readlines()

class Section(str, Enum):
    SEED_TO_SOIL = "seed-to-soil map:"
    SOIL_TO_FERTILIZER = "soil-to-fertilizer map:"
    FERTILIZER_TO_WATER = "fertilizer-to-water map:"
    WATER_TO_LIGHT = "water-to-light map:"
    LIGHT_TO_TEMPERATURE = "light-to-temperature map:"
    TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity map:"
    HUMIDITY_TO_LOCATION = "humidity-to-location map:"

maps: dict[Section, list[tuple[int, int, int]]] = {x: [] for x in Section}

seed_ranges: list[tuple[int, int]] = []
current_section: Section | None = None
for line in lines:
    line = line.strip()
    skip = False
    # Parse seeds, determine current section.
    if not line:
        current_section = None
    elif line.startswith("seeds: "):
        seed_values = [int(x) for x in line.split(": ").pop().split()]
        for i in range(0, len(seed_values), 2):
            seed_ranges.append(tuple(seed_values[i:i+2]))
    else:
        for section in Section:
            if line.startswith(section.value):
                current_section = section
                skip = True
                break
    
    # Append values to the appropriate map.
    if current_section and not skip:
        maps[current_section].append(tuple([int(x) for x in line.split()]))

# Generate maps of end index to offset.
offsets: dict[Section, dict[int, int]] = {x: { 0: 0 } for x in Section}
for section in Section:
    # Sort by ascending start index.
    maps[section].sort(key=lambda tup: tup[1])
    for dst, src, length in maps[section]:
        end = src + length
        offsets[section][end] = dst - src
        offsets[section][end + 1] = 0 # may be overwritten in later iteration

# Horrible. Brain melter.
def map_ranges(map_section: Section, input_ranges: list[tuple[int, int]]):
    output_ranges: list[tuple[int, int]] = []
    i = 0
    while i < len(input_ranges):
        start, length = input_ranges[i]
        found = False
        for dst, src, lgt in maps[map_section]:
            range_end = start + length
            map_end = src + lgt
            if start >= src and start < map_end:
                output_start = start - src + dst
                remaining_length = range_end - map_end
                if remaining_length <= 0:
                    output_ranges.append((output_start, length))
                else:
                    output_ranges.append((output_start, output_start - dst + lgt))
                    input_ranges.append((range_end, remaining_length))
                found = True
                break
            elif start < src and range_end > src:
                output_ranges.append((start, src - start))
                output_ranges.append((dst, min(range_end, map_end) - src))
                if range_end > map_end:
                    input_ranges.append((map_end, range_end - map_end))
                found = True
                break
        if not found:
            output_ranges.append((start, length))
        i += 1
    return output_ranges

soil_ranges = map_ranges(Section.SEED_TO_SOIL, seed_ranges)
fertilizer_ranges = map_ranges(Section.SOIL_TO_FERTILIZER, soil_ranges)
water_ranges = map_ranges(Section.FERTILIZER_TO_WATER, fertilizer_ranges)
light_ranges = map_ranges(Section.WATER_TO_LIGHT, water_ranges)
temperature_ranges = map_ranges(Section.LIGHT_TO_TEMPERATURE, light_ranges)
humidity_ranges = map_ranges(Section.TEMPERATURE_TO_HUMIDITY, temperature_ranges)
location_ranges = map_ranges(Section.HUMIDITY_TO_LOCATION, humidity_ranges)

print(min([x[0] for x in location_ranges]))
