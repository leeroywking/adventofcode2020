with open("./input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]


class Boat:
    def __init__(self, moves_list):
        self.x, self.y = (0, 0)
        self.moves_list = moves_list
        self.facing = "E"
        self.degree_map = {0: "N", 90: "E", 180: "S", 270: "W", "N":0, "E":90, "S":180, "W":270}
        self.waypoint_x = 10
        self.waypoint_y = 1

    def make_moves(self):
        for move in self.moves_list:
            direction = move[0]
            impulse = int(move[1:])

            if direction in "RL":
                self.handle_turn(direction, impulse)
            elif direction in "NSEW":
                self.handle_cardinal(direction, impulse)
            elif direction == "F":
                self.handle_cardinal(self.facing, impulse)
            else:
                print("you're spare parts bub")
    
    def make_moves_waypoint(self):
        for move in self.moves_list:
            direction = move[0]
            impulse = int(move[1:])
            # print("moving:", move)
            # print("from:", self.x, self.y)
            # print("waypoint:", self.waypoint_x, self.waypoint_y)
            if direction in "RL":
                self.handle_turn_waypoint(direction, impulse)
            elif direction in "NSEW":
                self.handle_cardinal_waypoint(direction, impulse)
            elif direction == "F":
                self.handle_waypoint_forward(impulse)
            else:
                print("you're spare parts bub")
            # print("new position:", self.x, self.y)
            # print("new waypoint:", self.waypoint_x, self.waypoint_y)
            # print("")

    def handle_turn(self, direction, impulse):
        if direction == "R":
            current_heading = self.degree_map[self.facing]
            current_heading += impulse
            current_heading = current_heading % 360
            self.facing = self.degree_map[current_heading]
        elif direction == "L":
            current_heading = self.degree_map[self.facing]
            current_heading -= impulse
            current_heading = current_heading % 360
            self.facing = self.degree_map[current_heading]
        else:
            print("you're spare parts")

    def handle_turn_waypoint(self, direction, impulse):
        if direction == "R":
            if impulse == 90:
                self.waypoint_y, self.waypoint_x = self.waypoint_x * -1, self.waypoint_y
            elif impulse == 180:
                self.waypoint_y = self.waypoint_y * -1
                self.waypoint_x = self.waypoint_x * -1
            elif impulse == 270:
                self.waypoint_y, self.waypoint_x = self.waypoint_x, self.waypoint_y * -1
            else:
                print("spare parts")
        elif direction == "L":
            if impulse == 270:
                self.waypoint_y, self.waypoint_x = self.waypoint_x * -1, self.waypoint_y
            elif impulse == 180:
                self.waypoint_y = self.waypoint_y * -1
                self.waypoint_x = self.waypoint_x * -1
            elif impulse == 90:
                self.waypoint_y, self.waypoint_x = self.waypoint_x, self.waypoint_y * -1
            else:
                print("spare parts")
        else:
            print("you're spare parts")

    def handle_cardinal(self, direction, impulse):
        if direction == "N":
            self.y += impulse
        elif direction == "S":
            self.y -= impulse
        elif direction == "E":
            self.x += impulse
        elif direction == "W":
            self.x -= impulse
    
    def handle_cardinal_waypoint(self, direction, impulse):
        if direction == "N":
            self.waypoint_y += impulse
        elif direction == "S":
            self.waypoint_y -= impulse
        elif direction == "E":
            self.waypoint_x += impulse
        elif direction == "W":
            self.waypoint_x -= impulse

    def handle_waypoint_forward(self, impulse):
        self.x += self.waypoint_x * impulse
        self.y += self.waypoint_y * impulse
        
    def find_manhat_distance(self):
        self.make_moves()
        return abs(self.x) + abs(self.y)

    def find_manhat_distance_waypoint(self):
        self.make_moves_waypoint()
        return abs(self.x) + abs(self.y)


boat = Boat(content)
print("answer part 1:", boat.find_manhat_distance())

boat_waypoint = Boat(content)
print("answer part 2:",boat_waypoint.find_manhat_distance_waypoint())
