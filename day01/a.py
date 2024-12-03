from collections import Counter
import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

lines = lines.split("\n")
lines = [line.split() for line in lines]
left, right = list(zip(*lines))

sorted_left = sorted(left)
sorted_right = sorted(right)

p1 = 0
for i in range(len(left)):
    p1 += abs(int(sorted_left[i]) - int(sorted_right[i]))


counter = Counter(right)

p2 = 0
for i in range(len(left)):
    item = int(left[i])
    freq = counter[left[i]]
    p2 += item * freq


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
