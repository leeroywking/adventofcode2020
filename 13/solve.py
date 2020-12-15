import math
with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

time = int(content[0])
buses = content[1].split(",")
# print(buses)

def find_closest_bus(buses, time):
    no_xs = list(buses)
    while "x" in no_xs:
        no_xs.remove("x")
    no_xs = [int(num) for num in no_xs]
    # print(no_xs)
    best_bus = 0
    best_wait_time = 10000
    for num in no_xs:
        wait = num - (time % num)
        if wait < best_wait_time:
            best_bus = num
            best_wait_time = wait
    print(best_wait_time * best_bus)
    
find_closest_bus(buses, time)
    

def check_time(time, buses):
    # print("checking:", time)
    try:
            
        for i in range(len(buses)):
            bus = buses[i]
            if bus == "x":
                pass
            elif (time + i) % int(bus) != 0:
                return False
            else:
                pass
        print("winner!: ", time)
        return True
    except KeyboardInterrupt:
        print("Killed by user checking time:", time)
biggest_bus = 0
biggest_bus_pos = 0
for i in range(len(buses)):
    try:
        bus = int(buses[i])
        if bus > biggest_bus:
            biggest_bus = bus
            biggest_bus_pos = i
    except:
        pass
print(biggest_bus_pos, biggest_bus)

# for i in range(219654121177954,10000000000000000,int(biggest_bus)):
# #                                219654121177954
# for i in range(0,10000000, int(biggest_bus)):
#     i = i - biggest_bus_pos
#     try:
#         check_time(i, buses)
#     except KeyboardInterrupt:
#         print("killed by user before finishing: ", i)

#545990309360
buses_offset = []
for i in range(len(buses)):
    bus = buses[i]
    if bus == "x":
        pass
    else:
        buses_offset.append([int(bus), i])
buses_offset.sort()
buses_offset.reverse()
print(buses_offset)

max_factor = 1

for bus_offset in buses_offset:
    max_factor *= bus_offset[0]
# print(max_factor)
possibilities = [(x - buses_offset[0][1]) for x in range(0,max_factor//2,buses_offset[0][0]) if (x - buses_offset[0][1] + buses_offset[1][1]) % buses_offset[1][0] == 0]
# possibilities.append(1068781)
print(possibilities[0])
print("checking", len(possibilities), "possibilities")
print("min check value", min(possibilities), "max value", max(possibilities))
for bus_offset in buses_offset:
    temp_poss = []
    for poss in possibilities:
        if (poss + bus_offset[1]) % bus_offset[0] == 0:
            # print("adding:", poss)
            temp_poss.append(poss)
    possibilities = temp_poss
    print("length of possibilities after checking bus",bus_offset)

print(len(possibilities), "remaining")
print(1068781 in possibilities)
print(possibilities)

