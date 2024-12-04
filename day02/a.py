import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

reports = lines.split("\n")


def is_gradually_increasing(levels):
    return all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))


def is_gradually_decreasing(levels):
    return all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))


p1 = 0
p2 = 0

for report in reports:
    levels = [int(level) for level in report.split()]
    if is_gradually_increasing(levels) or is_gradually_decreasing(levels):
        p1 += 1
        p2 += 1
    else:
        for i in range(len(levels)):
            new = levels[:]
            new.pop(i)
            if is_gradually_increasing(new) or is_gradually_decreasing(new):
                p2 += 1
                break


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
