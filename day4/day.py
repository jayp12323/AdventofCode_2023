import re

with open("scratch.txt", 'r') as file:
    lines = file.read().splitlines()
    cards = {}
    for i in range(len(lines)):
        line = re.sub("\s+", " ", lines[i]).split(" ")
        winning = set(line[2:12])
        numbers = set(line[13:])
        cards[i + 1] = {}
        cards[i + 1]["winning"] = winning
        cards[i + 1]["numbers"] = numbers


def part1():
    import math
    points = 0
    for card in cards:
        numbers = cards[card]["numbers"]
        winning = cards[card]["winning"]
        matched = numbers.intersection(winning)
        if matched:
            points += int(math.pow(2, len(matched) - 1))

    return points


def part2():
    import math
    points = 0
    card_dupes = {}
    for card in cards:
        card_dupes[card] = 1
    for card in cards:
        dupes = card_dupes[card]
        numbers = cards[card]["numbers"]
        winning = cards[card]["winning"]
        matched = numbers.intersection(winning)
        if matched:
            num_matches = len(matched)
            start=min(card+1,len(cards)-1)
            end = min(card+num_matches,len(cards)-1)
            for j in range(start,end+1):
                card_dupes[j]+=dupes

    card_counts = [card_dupes[i] for i in card_dupes]
    return sum(card_counts)

# val = part1()
# print(val)#
val = part2()
print(val)
