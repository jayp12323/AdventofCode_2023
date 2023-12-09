import math
import re
import multiprocessing

with open("scratch.txt", 'r') as file:
    lines = file.read().splitlines()

def part1():
    times=re.sub("\s+"," ",lines[0]).split(":")[1].strip().split(" ")
    distances=re.sub("\s+"," ",lines[1]).split(":")[1].strip().split(" ")
    win_combo=1
    for i,time in enumerate(times):
        distance = int(distances[i])
        time=int(time)
        wins=0
        for j in range(int(time)):
            total = (j)*(time-j)
            if total > distance:
                wins+=1
        win_combo = wins * win_combo
    return win_combo

def part2():
    wins=0
    time=int(re.sub("\s+","",lines[0]).split(":")[1].strip())
    distance=int(re.sub("\s+","",lines[1]).split(":")[1].strip())

    for j in range(int(time)):
        total = (j)*(time-j)
        if total > distance:
            wins+=1
    return wins

val = part2()
print(val)#