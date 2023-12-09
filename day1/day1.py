import re

with open("scratch.txt", 'r') as file:
    lines = file.read().splitlines()

result = 0
for line in lines:
    line_array = [l for l in line]
    i=0
    match=0
    ints=[]
    for i in range(len(line_array)):
        if line_array[i].isnumeric():
            ints.append(line_array[i])
            continue
        # print(line_array[i])
        three = "".join(line_array[i:i + 3])
        if re.match("one", three):
            ints.append("1")
            match=1
        elif re.match("two", three):
            ints.append("2")
            match=1
        elif re.match("six", three):
            ints.append("6")
            match=1
        if not match:
            four = "".join(line_array[i:i + 4])
            if re.match("four", four):
                ints.append("4")
                match=1
            elif re.match("five", four):
                ints.append("5")
                match=1
            elif re.match("nine", four):
                ints.append("9")
                match=1

            if not match:
                five = "".join(line_array[i:i + 5])
                if re.match("three", five):
                    ints.append("3")
                    match=1
                elif re.match("seven", five):
                    ints.append("7")
                    match=1
                elif re.match("eight", five):
                    ints.append("8")
                    match=1
        match=0
        i+=1
    # print(line)
    # line = re.m("one", "1", line)
    # ints.append("two", "2", line)
    # ints.append("three", "3", line)
    # ints.append("four", "4", line)
    # ints.append("five", "5", line)
    # ints.append("seven", "7", line)
    # ints.append("eight", "8", line)
    # ints.append("nine", "9", line)
    # print(line)
    nums = re.sub("[^0-9]", "", line)
    first=ints[0]
    last=ints[-1]
    num_value = int(first+last)
    print(num_value)
    result+=int(num_value)

print(result)




# p1 = 0
# p2 = 0
# for line in lines:
#   p1_digits = []
#   p2_digits = []
#   for i,c in enumerate(line):
#     if c.isdigit():
#       p1_digits.append(c)
#       p2_digits.append(c)
#     for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
#       if line[i:].startswith(val):
#         p2_digits.append(str(d+1))
#   p1 += int(p1_digits[0]+p1_digits[-1])
#   p2 += int(p2_digits[0]+p2_digits[-1])
#
#   print(int(p2_digits[0]+p2_digits[-1]))
# print(p1)
# print(p2)