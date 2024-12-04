import sys
import re

with open(sys.argv[1]) as file:
    lines = file.read().strip()

pattern = r"mul\((\d+),(\d+)\)"
enabled = r"do\(\)([\s\S]*?)(?:don\'t\(\)|$)"

p2_text = re.findall(enabled, "do()" + lines)

p1 = 0
p1_matches = re.findall(pattern, lines)
for match in p1_matches:
    p1 += int(match[0]) * int(match[1])

p2 = 0
for text in p2_text:
    matches = re.findall(pattern, text)
    for match in matches:
        p2 += int(match[0]) * int(match[1])

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
