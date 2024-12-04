import sys
import re

with open(sys.argv[1]) as file:
    text = file.read().strip()

p1_pattern = r"mul\((\d+),(\d+)\)"
p2_pattern = r"do\(\).*?(?:don\'t\(\))"

p1_matches = re.findall(p1_pattern, text)

p2_text = re.findall(p2_pattern, "do()" + text)

p1 = 0

for match in p1_matches:
    p1 += int(match[0]) * int(match[1])

p2 = 0

for text in p2_text:
    print(text)
    # matches = re.findall(p1_pattern, p2_match)
    # for match in matches:
    #     p2 += int(match[0]) * int(match[1])

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
