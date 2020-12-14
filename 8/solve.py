with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# print(content)

def parse_command(command):
    type_cmd = command.split(" ")[0]
    value = int(command.split(" ")[1])
    return type_cmd, value

def run_input(content):
    current_idx = 0
    acc = 0
    run_commands = []
    executed_last_command = False
    try:
        while content[current_idx] and current_idx not in run_commands:
            # print(current_idx)
            if current_idx == len(content) -1:
                # print("last item")
                executed_last_command = True
                return acc, executed_last_command
            run_commands.append(current_idx)
            type_cmd, value = parse_command(content[current_idx])
            if type_cmd == "nop":
                current_idx += 1
            elif type_cmd == "jmp":
                current_idx += value
            elif type_cmd == "acc":
                acc += value
                current_idx += 1
    except IndexError:
        return 0, False
    return acc, executed_last_command

last_acc = run_input(content)
print("answer part 1:",last_acc)


new_contents = []
for i in range(len(content)):
    temp_content = list(content)
    current = content[i]
    type_cmd, value = parse_command(current)
    if type_cmd == "jmp":
        temp_content[i] = f"nop {value}"
        new_contents.append(temp_content)
    elif type_cmd == "nop":
        temp_content[i] = f"jmp {value}"
        new_contents.append(temp_content)

for content in new_contents:
    acc, executed_last_command = run_input(content)
    if executed_last_command:
        print(acc)