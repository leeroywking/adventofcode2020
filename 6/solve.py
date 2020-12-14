with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# print(content)

def make_groups(content):
    groups = []
    entry = ""
    for item in content:
        if item == "":
            groups.append(entry)
            entry = ""
        else:
            entry += item
    groups.append(entry)
    return groups

groups = make_groups(content)
# print(groups[0])

def count_group_entries(group):
    set_letts = set(group)
    # print(len(et_letts)
    return len(set_letts)

group_sum = 0
for group in groups:
    group_sum += count_group_entries(group)

print("answer part 1:", group_sum)

def make_group_with_individuals(content):
    groups = []
    group = []
    for line in content:
        if line == "":
            groups.append(group)
            group = []
        else:
            group.append(set(line))
    groups.append(group)
    return groups

groups_with_individuals = make_group_with_individuals(content)
# print(groups_with_individuals[8])

def check_intersection_for_group(group):
    inter = group[0].intersection(*group)
    return inter

total_intersect_count = 0
for group in groups_with_individuals:
    count = len(check_intersection_for_group(group))
    total_intersect_count += count

print("answer to part 2:",total_intersect_count)