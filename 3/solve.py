with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
# print(content)

def build_path(right,down):
    output = ""
    current_y = 0
    current_x = 0
    height = len(content)
    width = len(content[0])
    while current_y < height:
        output += content[current_y][current_x]
        current_x = (current_x + right) % width
        current_y = current_y + down

    return output

#part 1 answer
print(build_path(3,1).count("#"))

#part 2 answer
first = build_path(1,1).count("#")
second = build_path(3,1).count("#")
third = build_path(5,1).count("#")
fourth = build_path(7,1).count("#")
fifth = build_path(1,2).count("#")
print (first * second * third * fourth * fifth)