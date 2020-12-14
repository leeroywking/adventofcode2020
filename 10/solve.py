with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]
# print(content)

sorted_input = sorted(content)

def count_1s_and_3s(sorted_input):
    counter = {1:0,2:0,3:0}
    last_val = 0
    for i in range(len(sorted_input)):
        curr = sorted_input[i]
        diff = curr - last_val
        counter[diff] += 1
        last_val = curr
    counter[3] += 1
    return counter

counter = count_1s_and_3s(sorted_input)
print("answer part1:", counter[1] * counter[3])

def find_valid_arrangements(sorted_input):
    count_valid_arrangements = 0
    iterations = 0
    def spawn(idx):
        nonlocal iterations
        nonlocal count_valid_arrangements
        nonlocal sorted_input
        iterations += 1
        curr = sorted_input[idx]
        maxi = len(sorted_input) - 1
        if curr == sorted_input[maxi]:
            count_valid_arrangements += 1
        else:
            if maxi - idx >= 3:
                next_item1 = sorted_input[idx + 1]
                next_item2 = sorted_input[idx + 2]
                next_item3 = sorted_input[idx + 3]
                if next_item1 - curr <= 3:
                    spawn(idx + 1)
                if next_item2 - curr <= 3:
                    spawn(idx + 2)
                if next_item3 - curr <= 3:
                    spawn(idx +3)
            elif maxi - idx == 2:
                next_item1 = sorted_input[idx + 1]
                next_item2 = sorted_input[idx + 2]
                if next_item1 - curr <= 3:
                    spawn(idx + 1)
                if next_item2 - curr <= 3:
                    spawn(idx + 2)
            elif maxi - idx == 1:
                next_item1 = sorted_input[idx + 1]
                if next_item1 - curr <= 3:
                    spawn(idx + 1)
            else:
                print("you fucked the dog")
    try:
        spawn(0)
    except KeyboardInterrupt:
        print()
        print(iterations, "iterations", count_valid_arrangements, "valid arrangements found")
    print(iterations, "iterations", count_valid_arrangements, "valid arrangements found")

    return count_valid_arrangements


# find_valid_arrangements(sorted_input)

def math_solve_valid_arrangements(sorted_input):
    count = 1
    def check_next_x_vals(curr, num, i):
        nonlocal sorted_input, count
        multiplier = 0
        for j in range (1, num +1):
            if sorted_input[i + j] - curr <= 3:
                multiplier += 1
        count *= multiplier
    
    for i in range(len(sorted_input) -4):
        check_next_x_vals(sorted_input[i], 3, i)
    
    # check_next_x_vals(sorted_input[len(sorted_input) - 4], 3, len(sorted_input) - 4)
    # check_next_x_vals(sorted_input[len(sorted_input) - 3], 3, len(sorted_input) - 3)
    # check_next_x_vals(sorted_input[len(sorted_input) - 2], 3, len(sorted_input) - 2)
    return count
    
# final_count = math_solve_valid_arrangements(sorted_input)
# print(final_count)

def find_paths(sorted_input):
    count = 0
    last_idx = len(sorted_input) -1
    idxs_to_walk = [0]
    def walk(idx):
        nonlocal count
        if idx == last_idx:
            # print("hit base case")
            count += 1
        check_idx = idx + 1
        while check_idx <= last_idx and sorted_input[check_idx] <= sorted_input[idx] + 3 :
            # walk(check_idx)
            idxs_to_walk.append(check_idx)
            check_idx += 1

    while idxs_to_walk:
        curr = idxs_to_walk.pop(len(idxs_to_walk) -1)
        walk(curr)
        # if count % 100000 == 0:
        #     print(count)

    return count

# path_count = find_paths([0] + sorted_input)
# print(path_count)


print(sorted_input)


consecutive_multipliers = {
    1:1,
    2:1,
    3:2,
    4:4,
    5:7
}

def find_streaks(sorted_input):
    streaks = []
    count = 1
    i = 0
    while i < len(sorted_input)-1:
        if sorted_input[i]+1 == sorted_input[i+1]:
            count += 1
            i += 1
        else:
            streaks.append(count)
            count = 1
            i += 1
    streaks.append(count)
    return streaks

streaks = find_streaks([0] + sorted_input)

for i in range(len(streaks)):
    if streaks[i] == 0:
        streaks[i] = 1

print(streaks)

total = 1
for item in streaks:
    total *= consecutive_multipliers[item]

print(total)
# 4147200000000 too low
# 1511207993344 someone elses answer