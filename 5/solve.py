with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# print(content)

def split_rows_columns(entry):
    row = entry[:7]
    column = entry[7:]
    # print(row, column)
    return row, column

def calculate_num(row_string, upper, lower, maximum):
    # 0-127
    top = maximum
    bottom = 0
    middle = (top + bottom) // 2
    # print(middle)
    row_list = list(row_string)
    #F is lower 
    #B is upper
    # print(bottom, middle, top)
    while len(row_list):
        current = row_list.pop(0)
        if current == lower:
            if bottom + 1 == middle:
                # print(bottom, middle, top)
                bottom = middle
                return middle
            top = middle
            middle = (top + bottom) // 2
        elif current == upper:
            if middle + 1 == top:
                # print(bottom,middle, top)
                middle = top
                return middle
            bottom = middle
            middle = (top + bottom) // 2 
        # print(current)
        # print(bottom, middle, top)
    return middle

def find_row_column(entry):
    row, column = split_rows_columns(entry)
    row_int = calculate_num(row, "B", "F", 127)
    column_int = calculate_num(column, "R","L", 7)
    return row_int, column_int

def calc_seat_id(row,column):
    # multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357
    return (row * 8) + column

# row, column = find_row_column("BFFFBBFRRR")
# seat_id = calc_seat_id(row,column)
# print(seat_id)

highest_id = 0
list_of_ids = []
for entry in content:
    row, column = find_row_column(entry)
    seat_id = calc_seat_id(row, column)
    if seat_id > highest_id:
        highest_id = seat_id
    list_of_ids.append(seat_id)
print(highest_id, "solution part 1")



sorted_ids = sorted(list_of_ids)

full_seat_ids = []
rows = range(1, 126)
columns = range(7)
for row in rows:
    for column in columns:
        full_seat_ids.append((row*8) + column)

for item in list_of_ids:
    try:
        full_seat_ids.remove(item)
    except:
        pass
# print(full_seat_ids)

for idx in range(len(list_of_ids)):
    try:
        current = list_of_ids[idx]
        next_item = list_of_ids[idx +1]
        next_next_item = list_of_ids[idx +2]
        if current + 1 != next_item and current +2 == next_next_item:
            print(current + 1)
    except:
        pass

# print(sorted_ids)
for item in sorted_ids:
    # print(item)
    pass

print("the answer to part two is 717, I got that by comparing some of these lists by eye since there was a repeat on an interval of 8 (0/7) I saw the one in the leftover list I made that was not a multiple of 8 in this case it was 717")