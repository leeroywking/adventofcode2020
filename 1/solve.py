with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content] 

def main():
    for item in content:
        for item2 in content:
            for item3 in content:
                if item + item2 + item3 == 2020:
                    print(item * item2 * item3)
                    return True

main()


def main_o_1():
    big_map = {}
    for item in content:
        big_map[item] = {}
    for item in content
        big_map[item]