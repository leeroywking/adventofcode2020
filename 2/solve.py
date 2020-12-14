with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

split_content = []
for item in content:
    split_line = item.split(" ")
    rule = split_line[0]
    letter = split_line[1][0]
    password = split_line[2]
    new_item = {"rule": rule, "letter": letter, "password": password}
    split_content.append(new_item)

def check_entry(entry):
    split_rule = entry["rule"].split("-")
    minimum = int(split_rule[0])
    maximum = int(split_rule[1])
    count_letters = entry["password"].count(entry["letter"])
    result =  count_letters >= minimum and count_letters <= maximum
    return result

def check_entry2(entry):
    split_rule = entry["rule"].split("-")
    low = int(split_rule[0]) - 1
    high = int(split_rule[1]) - 1
    try:
        if entry["password"][low] == entry["letter"]:
            if entry["password"][high] != entry["letter"]:
                return True
        elif entry["password"][high] == entry["letter"]:
            if entry["password"][low] != entry["letter"]:
                return True
        else:
            return False
    except IndexError:
        print(entry)
        return False

count_valid = 0
for item in split_content:
    if check_entry(item):
        count_valid += 1

count_valid2 = 0
for item in split_content:
    if check_entry2(item):
        count_valid2 += 1

print(count_valid)
print(count_valid2)