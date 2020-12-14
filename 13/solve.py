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

for i in range(168820080614,100000000000000,int(biggest_bus)):
#                              168820080614
# for i in range(0,10000000, int(biggest_bus)):
    i = i - biggest_bus_pos
    try:
        check_time(i, buses)
    except KeyboardInterrupt:
        print("killed by user before finishing: ", i)
