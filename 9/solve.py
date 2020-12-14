with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]

# print(content)

def find_naughty_num(content):
    for i in range(25,len(content)):
        valid = False
        for j in range(i - 25, i):
            for k in range(i-25, i):
                if content[j] + content[k] ==  content[i]:
                    valid = True
        if valid == False:
            return content[i]

naughty_num = find_naughty_num(content)
print("answer part 1:", naughty_num)

def find_naughty_range(content, naughty_num):
    for i in range(len(content)):
        running_total = 0
        j = i
        nums = []
        while running_total < naughty_num and j < len(content):
            running_total += content[j]
            nums.append(content[j])
            if running_total == naughty_num:
                new_nums = sorted(nums)
                return (new_nums[0] , new_nums[len(new_nums)-1])
                # return (i,j)
            else: 
                j += 1
naughty_min, naughty_max = find_naughty_range(content, naughty_num)
print("Answer part 2:",naughty_min + naughty_max)