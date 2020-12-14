with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
# print(content)
entry_count = 0
for line in content:
    if line == "":
        entry_count += 1
print(entry_count, "entries")
list_of_passports = []
temp = {"all_data":""}
for line_num in range(len(content)):
    if content[line_num] == "":
        list_of_passports.append(dict(temp))
        temp = {"all_data":""}
    else:
        temp["all_data"] = temp["all_data"] + content[line_num] + " "
list_of_passports.append(dict(temp))


total_valid = 0
new_list_passports = []

for item in list_of_passports:
    list_of_data = item["all_data"].split(" ")
    # print(item)
    for pair in list_of_data:
        if pair == "":
            # print(list_of_data)
            list_of_data.remove(pair)
            # print(list_of_data)
    temp_dict = {}
    for subitem in list_of_data:
        pair = subitem.split(":")
        temp_dict[pair[0]] = pair[1]
    new_list_passports.append(temp_dict)


failures = 0
for item in new_list_passports:
    if len(item) == 8:
        # print("success 8 items",item)
        total_valid += 1
    elif len(item) == 7 and "cid" not in item:
        total_valid += 1
        # print("success 7 items and no CID", item)
        pass
    else:
        # print("failure:", item)
        failures += 1
        pass
print(len(new_list_passports), "total passports")
print(total_valid, "valid")
print(failures, "failures")
print(new_list_passports[len(new_list_passports) -1])
# for item in new_list_passports:
#     print(item)

# part 2 validator
def part2_validator(entry):
    if len(entry) == 8:
        pass
    elif len(entry) == 7 and "cid" not in item:
        pass
    else:
        return False
    byr = int(entry["byr"]) >= 1920 and int(entry["byr"]) <= 2002
    iyr = int(entry["iyr"]) >= 2010 and int(entry["iyr"]) <= 2020
    eyr = int(entry["eyr"]) >= 2020 and int(entry["eyr"]) <= 2030
    hgt_unit = entry["hgt"][-2:]
    hgt = True
    try:
        hgt_val = int(entry["hgt"][:-2])
    except:
        print(entry["hgt"])
        hgt = False
    
    if hgt_unit == "cm":
        hgt = hgt_val >=150 and hgt_val <= 193
    elif hgt_unit == "in":
        hgt = hgt_val >= 59 and hgt_val <= 76
    hcl = True
    hcl_val = entry["hcl"]
    if hcl_val[0] != "#":
        hcl = False
    for char in hcl_val[1:]:
        if char not in "0123456789abcdef":
            hcl = False
    ecl = entry["ecl"] in ["amb", "blu","brn","gry","grn","hzl","oth"]
    pid = True
    try:
        if len(entry["pid"]) != 9:
            pid = False
        pid = int(entry["pid"])
    except:
        pid = False
    return byr and iyr and eyr and hgt and hcl and ecl and pid


part2_validator(new_list_passports[3])

part2_valid_count = 0
for item in new_list_passports:
    if part2_validator(item):
        part2_valid_count += 1
print(part2_valid_count, "part2 valid count")