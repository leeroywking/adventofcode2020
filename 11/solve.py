with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
# print(content)


def count_empty_seats(diagram):
    count = 0
    for row in diagram:
        for space in row:
            if space == "L":
                count += 1
    return count


def count_occupied_seats(diagram):
    count = 0
    for row in diagram:
        for space in row:
            if space == "#":
                count += 1
    return count


# empty_seats_at_start = count_empty_seats(content)
# print("empty seats at start:",empty_seats_at_start)


def collect_neighbors(y, x, diagram):
    # x, y = y,x
    neighbors = [
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (0, -1),
        (+1, -1),
        (+1, 0),
        (+1, +1),
    ]
    empty_count = 0
    occ_count = 0
    for neighbor in neighbors:
        x_shift, y_shift = neighbor
        neigh_x, neigh_y = x + x_shift, y + y_shift
        if (
            neigh_y >= 0
            and neigh_y < len(diagram)
            and neigh_x >= 0
            and neigh_x < len(diagram[0])
        ):
            # print("Position", (neigh_x, neigh_y), "being checked")
            if diagram[neigh_y][neigh_x] == "L":
                empty_count += 1
                # print("found an empty seat")
            elif diagram[neigh_y][neigh_x] == "#":
                occ_count += 1
    return empty_count, occ_count


def collect_long_neighbors(y, x, diagram):
    occ_count = 0
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (0, -1),
        (+1, -1),
        (+1, 0),
        (+1, +1),
    ]
    for direction in directions:
        x_shift, y_shift = direction
        curr_x, curr_y = x + x_shift, y + y_shift
        neighbor = "."
        iteration_count = 0
        while (
            neighbor not in "L#"
            and curr_y >= 0
            and curr_y < len(diagram)
            and curr_x >= 0
            and curr_x < len(diagram[0])
        ):
            iteration_count += 1
            if diagram[curr_y][curr_x] == "L":
                neighbor = "L"
            elif diagram[curr_y][curr_x] == "#":
                neighbor = "#"
            else:
                curr_x, curr_y = curr_x + x_shift, curr_y + y_shift
        if neighbor == "#":
            occ_count += 1
    # print(occ_count)
    return occ_count


# empty_count, occ_count = collect_neighbors((0,0), content)
# print(empty_count, occ_count)


def make_new_char(y, x, content):
    empty_count, occ_count = collect_neighbors(y, x, content)
    if content[y][x] == ".":
        return "."
    elif content[y][x] == "L" and occ_count == 0:
        return "#"
    elif content[y][x] == "#" and occ_count >= 4:
        return "L"
    else:
        return content[y][x]


def make_new_char_long_look(y, x, content):
    occ_count = collect_long_neighbors(y, x, content)
    if content[y][x] == ".":
        return "."
    elif content[y][x] == "L" and occ_count == 0:
        return "#"
    elif content[y][x] == "#" and occ_count >= 5:
        return "L"
    else:
        return content[y][x]


# new_char = make_new_char((0,0), content)
# print(new_char)


def make_iteration_board(board):
    new_board = []
    for y in range(len(board)):
        new_line = ""
        for x in range(len(board[y])):
            # print("checking:", x,y)
            new_line += make_new_char(y, x, board)
        new_board.append(new_line)
    return new_board


def make_iteration_board_long(board):
    new_board = []
    for y in range(len(board)):
        new_line = ""
        for x in range(len(board[y])):
            # print("checking:", x,y)
            new_line += make_new_char_long_look(y, x, board)
        new_board.append(new_line)
    return new_board


# new_board = make_iteration_board(content)
# for line in new_board:
#     print(line)


def compute_stable_arrangement(content):
    last_board = list(content)
    current_board = make_iteration_board(last_board)
    current_board = make_iteration_board(current_board)
    while last_board != current_board:
        last_board = current_board
        current_board = make_iteration_board(last_board)
    return current_board


def compute_stable_arrangement_long_look(content):
    last_board = list(content)
    current_board = make_iteration_board_long(last_board)
    current_board = make_iteration_board_long(current_board)
    while last_board != current_board:
        last_board = current_board
        current_board = make_iteration_board_long(last_board)
    return current_board


last_board = compute_stable_arrangement(content)
occ_seats_at_end = count_occupied_seats(last_board)


last_board_long_look = compute_stable_arrangement_long_look(content)
occ_seats_at_end_long = count_occupied_seats(last_board_long_look)

# for line in last_board_long_look:
#     print(line)

print("occupied seats at end part 1:", occ_seats_at_end)
print("occupied seats at end part 2:", occ_seats_at_end_long)