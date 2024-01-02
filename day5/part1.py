from enum import Enum

lines: list[str] = []
with open("input.txt", "r") as file_in:
    lines = file_in.readlines()

class Section(str, Enum):
    SEED_TO_SOIL = "seed-to-soil map:"
    SOIL_TO_FERTILIZER = "soil-to-fertilizer map:"
    FERTILIZER_TO_WATER = "fertilizer-to-water map:"
    WATER_TO_LIGHT = "water-to-light map:"
    LIGHT_TO_TEMPERATURE = "light-to-temperature map:"
    TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity map:"
    HUMIDITY_TO_LOCATION = "humidity-to-location map:"

maps: dict[Section, list[list[int]]] = {x: [] for x in Section}

seeds: list[int] = []
current_section: Section | None = None
for line in lines:
    line = line.strip()
    skip = False
    # Parse seeds, determine current section.
    if not line:
        current_section = None
    elif line.startswith("seeds: "):
        seeds = [int(x) for x in line.split(": ").pop().split()]
    else:
        for section in Section:
            if line.startswith(section.value):
                current_section = section
                skip = True
                break
    
    # Append values to the appropriate map.
    if current_section and not skip:
        maps[current_section].append([int(x) for x in line.split()])


def lookup(section: Section, vals: list[int]):
    result: list[int] = []
    for val in vals:
        result.append(val)
        for (dest, src, length) in maps[section]:
            if val >= src and val < src + length:
                result[-1] += dest - src
    return result

soils = lookup(Section.SEED_TO_SOIL, seeds)
fertilizers = lookup(Section.SOIL_TO_FERTILIZER, soils)
waters = lookup(Section.FERTILIZER_TO_WATER, fertilizers)
lights = lookup(Section.WATER_TO_LIGHT, waters)
temperatures = lookup(Section.LIGHT_TO_TEMPERATURE, lights)
humidities = lookup(Section.TEMPERATURE_TO_HUMIDITY, temperatures)
locations = lookup(Section.HUMIDITY_TO_LOCATION, humidities)

print(min(locations))
