with open("./stats.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

days = []

for line in content:
    split_line = line.split(" ")
    while "" in split_line:
        split_line.remove("")
    day, golds, silvers, stars  = split_line[0] , split_line[1] ,split_line[2], split_line[3]
    # print(stars)
    days.append({"day":day,"golds":golds,"silvers":silvers,"stars":stars})

def print_vertical_stars(days):
    days.reverse()
    max_len = 0
    for day in days:
        if len(day["stars"]) > max_len:
            max_len = len(day["stars"])
    output_array = []
    for i in range(max_len):
        row = []
        for day in days:
            try:
                row.append(day["stars"][i])
            except IndexError:
                row.append(" ")
        output_array.insert(0,row)
    for line in output_array:
        print(" ".join(line))
        

print_vertical_stars(days)

# for stat in stats:
#     day = stats[stat]
#     total = day["gold"] + day["silver_only"]
#     fail_percent = (day["silver_only"] / total) * 100
#     print(day["stars"])


