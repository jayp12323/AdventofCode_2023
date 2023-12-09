import re

with open("scratch.txt", 'r') as file:
    lines = file.read().splitlines()


def part1():
    balls = {}
    balls["red"] = 12
    balls["green"] = 13
    balls["blue"] = 14

    sum = 0
    for i in lines:
        unpossible = 0
        game_num = i.split(" ")[1][0:-1]
        sets = i.split(":")[1].split(";")
        for set in sets:
            balls_in_set = set.split(",")
            for ball in balls_in_set:
                num, color = ball.strip().split(" ")
                if int(num) > balls[color]:
                    unpossible = 1
        if not unpossible:
            print(game_num)
            sum += int(game_num)

def part2():
    balls = {}

    sum=0
    for i in lines:
        balls["red"] = 0
        balls["green"] = 0
        balls["blue"] = 0
        sets = i.split(":")[1].split(";")
        for set in sets:
            balls_in_set = set.split(",")
            for ball in balls_in_set:
                num, color = ball.strip().split(" ")
                if int(num) > balls[color]:
                    balls[color] = int(num)
        sum+=balls["red"]* balls["green"]*balls["blue"]
    return sum

# sum = part1()
sum = part2()
print(sum)
