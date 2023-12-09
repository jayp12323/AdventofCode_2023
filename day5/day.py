import math
import re
import multiprocessing

def set_dict(mappings,lists,names):
    names = names.split(",")
    for i in range(len(lists)):
        list=lists[i]
        # print(list.splitlines()[1:])
        name = names[i]
        mappings[name] =[]
        for i in list.splitlines()[1:]:
            dest, start, length = i.split(" ")
            mappings[name].append([int(dest), int(start), int(length)])

    return mappings



with open("scratch.txt", 'r') as file:
    seed,soil,fert,water,light,temp,hum,location = re.split("\n\n",file.read())
    mappings={}
    mappings = set_dict(mappings,[soil,fert,water,light,temp,hum,location],"soil,fert,water,light,temp,hum,location")
    seed_line = seed.split(" ")[1:]
    seeds = [seed_line[2*i:2*i+2] for i in range(int(math.ceil(len(seed_line))/2))]

def g(dict,val):
    lines = mappings[dict]
    for dest, start, length in lines:
        if start <= val <= start+length-1:
            return dest+(val-start)
    return val
    # try:
    #     return mappings[dict][val]
    # except:
    #     return val

def part1():
    positions=[]
    for seed in seeds:
        seed_num=int(seed)
        soil=g("soil",seed_num)
        fert=g("fert",soil)
        water=g("water",fert)
        light=g("light",water)
        temp=g("temp",light)
        hum=g("hum",temp)
        location=g("location",hum)
    #
        positions.append(location)
    return(min(positions))
def part2(start,ran):
    positions=[]
    print("start",start,ran)
    for i in range(int(start),int(start)+int(ran)+1):
        seed_num=int(i)
        soil=g("soil",seed_num)
        fert=g("fert",soil)
        water=g("water",fert)
        light=g("light",water)
        temp=g("temp",light)
        hum=g("hum",temp)
        location=g("location",hum)
        # print(seed_num,location)
        positions.append(location)
    print(start,min(positions))


# val = part1()
# print(val)#
if __name__ == '__main__':
    procs = []
    q = multiprocessing.Queue()
    for seed in seeds:
        start,ran=seed
        proc = multiprocessing.Process(target=part2, args=(start,ran))
        procs.append(proc)
        proc.start()
    proc.join()

    # val = part2()
    # print(val)
