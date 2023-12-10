from collections import Counter

with open("scratch.txt", 'r') as file:
    lines = file.read().splitlines()

cards="A,K,Q,J,T,9,8,7,6,5,4,3,2".split(",")
cards.reverse()

cards_j="A,K,Q,T,9,8,7,6,5,4,3,2,J".split(",")
cards_j.reverse()


def find_type(hand):
    if hand.most_common()[0][1] ==5:
        return 7
    if hand.most_common()[0][1] ==4:
        return 6
    if hand.most_common()[0][1] ==3:
        if hand.most_common()[1][1] ==2:
            return 5
        else:
            return 4
    if hand.most_common()[0][1] ==2:
        if hand.most_common()[1][1] ==2:
            return 3
        else:
            return 2
    return 1

def find_type_j(hand):

    joker_count = hand["J"]
    hand = dict(hand)
    try:
        del hand["J"]
    except:
        pass
    hand = Counter(hand)
    if not hand:
        return 7
    if hand.most_common()[0][1] +joker_count ==5:
        return 7
    if hand.most_common()[0][1]+joker_count ==4:
        return 6
    if hand.most_common()[0][1] +joker_count==3:
        if hand.most_common()[1][1] ==2:
            return 5
        else:
            return 4
    if hand.most_common()[0][1] +joker_count ==2:
        if hand.most_common()[1][1] ==2:
            return 3
        else:
            return 2
    return 1

def part1():
    ranks = {i:[] for i in range(1,8)}
    for line in lines:
        hand,bid = line.split(" ")
        bid=int(bid)
        hand_counts = Counter(hand)
        type = find_type(hand_counts)
        ranks[type].append([list(hand),bid])
    order = []
    for rank,hands in ranks.items():
        if ranks[rank]:
            sorted_list = sorted(hands,key=lambda x:(cards.index(x[0][0]),cards.index(x[0][1]),cards.index(x[0][2]),cards.index(x[0][3]),cards.index(x[0][4])))
            order.extend(sorted_list)
    print(order)
    total=0
    for place,hand in enumerate(order):
        print(hand)
        bid = hand[1]
        total+=(place+1)*bid
    print(total)
def part2():

    ranks = {i:[] for i in range(1,8)}
    for line in lines:
        hand,bid = line.split(" ")
        bid=int(bid)
        hand_counts = Counter(hand)
        type = find_type_j(hand_counts)
        ranks[type].append([list(hand),bid])
    print(ranks)
    order = []
    for rank,hands in ranks.items():
        if ranks[rank]:
            sorted_list = sorted(hands,key=lambda x:(cards_j.index(x[0][0]),cards_j.index(x[0][1]),cards_j.index(x[0][2]),cards_j.index(x[0][3]),cards_j.index(x[0][4])))
            order.extend(sorted_list)
    print(order)
    total=0
    for place,hand in enumerate(order):
        print(hand)
        bid = hand[1]
        total+=(place+1)*bid
    print(total)


val = part2()
