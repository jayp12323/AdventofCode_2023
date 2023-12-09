import re

with open("scratch.txt", 'r') as file:
    lines = file.read().splitlines()
    rows = []
    for line in lines:
        rows.append(list(line))


# print(rows)

def find_nums(grid):
    nums = {}
    for j in range(len(grid)):
        nums[j] = {}
        row = grid[j]
        i = 0
        while i < len(row):
            if row[i].isnumeric():
                start = i
                while i < len(row) and row[i].isnumeric() :
                    i += 1
                end = i
                i += 1
                num = int("".join(row[start:end]))
                if start == 0:
                    start = 0
                else:
                    start -= 1
                if end == len(row) - 1:
                    end = len(row) - 1
                else:
                    end += 1
                nums[j][(num,start)] = [start, end - 1]
            else:
                i += 1

    return nums


def find_symbols(grid):
    symbols = {}
    for j in range(len(grid)):
        symbol_loc = []
        row = grid[j]
        for i in range(len(row)):
            if re.match("[^0-9.]", row[i]):
                symbol_loc.append(i)
        symbols[j] = symbol_loc

    return symbols

def find_gears(grid):
    symbols = {}
    for j in range(len(grid)):
        symbol_loc = []
        row = grid[j]
        for i in range(len(row)):
            if re.match("\*", row[i]):
                symbol_loc.append(i)
        symbols[j] = symbol_loc

    return symbols


def part1():
    nums = find_nums(rows)
    symbols = find_symbols(rows)
    part_nums = []

    for row in symbols:
        if symbols[row]:
            for symbol_loc in symbols[row]:
                if row == 0:
                    start = row
                else:
                    start = row - 1
                if row == len(rows) - 1:
                    end = len(rows) - 1
                else:
                    end = row + 1
                for i in range(start, end + 1):
                    row_nums = nums[i]
                    for num in row_nums:
                        num_start, num_end = row_nums[num]
                        print(num_start,num_end,num)
                        if num_start <= symbol_loc <= num_end:
                            part_nums.append(num[0])

    print(part_nums)
    return(part_nums)


def part2(grid):
    nums = find_nums(rows)

    gear_nums=[]
    symbols = find_gears(grid)
    for row in symbols:
        if symbols[row]:
            for symbol_loc in symbols[row]:
                touching=[]
                if row == 0:
                    start = row
                else:
                    start = row - 1
                if row == len(rows) - 1:
                    end = len(rows) - 1
                else:
                    end = row + 1
                for i in range(start, end + 1):
                    row_nums = nums[i]
                    for num in row_nums:
                        num_start, num_end = row_nums[num]
                        if num_start <= symbol_loc <= num_end:
                            touching.append(num[0])
                if len(touching)==2:
                    gear_nums.append(touching[0]*touching[1])
    return gear_nums


# sum = part1()
nums = part2(rows)
print(nums)
print(sum(nums))




# import math as m, re
#
# board = list(open('scratch.txt'))
# chars = {(r, c): [] for r in range(140) for c in range(140)
#                     if board[r][c] not in '01234566789.'}
#
# for r, row in enumerate(board):
#     for n in re.finditer(r'\d+', row):
#         edge = {(r, c) for r in (r-1, r, r+1)
#                        for c in range(n.start()-1, n.end()+1)}
#
#         for o in edge & chars.keys():
#             chars[o].append(int(n.group()))
# vals = [j for i in chars.values() for j in i]
# print(vals)