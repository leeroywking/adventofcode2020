import re
with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# print(content[0])
# print(content[10])
# print(content[100])

def parse_text_into_entry(text):
    color = text.split("bags")[0].strip()
    # print(color)
    bag_contents = text[len(color) + 13:].split(",")
    # print(bag_contents)
    sub_bags = []
    for item in bag_contents:
        try:
            subbag = re.search(r'\d (.*?) bag', item).group(1)
            # print(subbag)
            sub_bags.append(subbag)
        except:
            # print(item)
            # this catches "No other bags"
            pass
    entry = {color:sub_bags}
    return entry


# entry = parse_text_into_entry(content[0])
# print(entry)

def build_big_reference(content):
    big_dict = {}
    for item in content:
        entry = parse_text_into_entry(item)
        big_dict.update(entry)
    return big_dict

big_dict = build_big_reference(content)
# print(big_dict)

def check_big_dict_for_bag_type(big_dict, input_bag, search_bag = "shiny gold"):
    bags_to_check = [input_bag]
    while bags_to_check:
        current = bags_to_check.pop(0)
        sub_bags = big_dict[current]
        for bag in sub_bags:
            if bag == "shiny gold":
                return True
            bags_to_check.append(bag)
    return False


# bool_bag_exits = check_big_dict_for_bag_type(big_dict, "light gold", "shiny gold")
# print(bool_bag_exits)

def build_total(big_dict, search_bag = "shiny gold"):
    total = 0
    for item in big_dict:
        if check_big_dict_for_bag_type(big_dict, item, search_bag):
            total += 1
    return total

# print("answer part 1:", build_total(big_dict))

def parse_text_into_entry2(text):
    color = text.split("bags")[0].strip()
    # print(color)
    bag_contents = text[len(color) + 13:].split(",")
    # print(bag_contents)
    sub_bags = []
    for item in bag_contents:
        try:
            sub_color = re.search(r'\d (.*?) bag', item).group(1).strip()
            num = item.strip()[0]
            # print(color, num)
            sub_bags.append({sub_color:num})
        except:
            # print(item)
            # this catches "No other bags"
            pass
    entry = {color:sub_bags}
    return entry

# print(parse_text_into_entry2(content[0]))

def build_big_reference2(content):
    big_dict = {}
    for item in content:
        entry = parse_text_into_entry2(item)
        big_dict.update(entry)
    return big_dict

big_reference2 = build_big_reference2(content)
# print(big_reference2["light gold"])

def count_bags_required(big_reference2, search_color = "shiny gold"):
    count = 0
    def walk(color, multiplier):
        nonlocal count
        sub_colors = big_reference2[color]
        for sub_color in sub_colors:
            for key in sub_color:
                color_name = key
                bag_multiplier = int(sub_color[key])
            count += (multiplier * bag_multiplier)
            print("Added", multiplier * bag_multiplier ,color_name)
            walk(color_name, bag_multiplier * multiplier)
    walk("shiny gold", 1)
    return count


sub_bag_count = count_bags_required(big_reference2)
print(sub_bag_count)
# print(big_reference2["shiny gold"])
#2230 too low
#18903 too low
#54802 too low
# print(big_reference2["dark chartreuse"])