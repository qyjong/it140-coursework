
class Room:

    def __init__(self, name, north, south, east, west, item, description):
        self.name = name
        # The following four values are Room objects
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.item = item
        self.description = description

    def go_direction(self, direction):
        if direction == "N":
            print("You walk north.")
            return(self.north)
        elif direction == "S":
            print("You walk south.")
            return(self.south)
        elif direction == "E":
            print("You walk east.")
            return(self.east)
        elif direction == "W":
            print("You walk west.")
            return(self.west)
        print("\n")
    
    def look_around(self):
        print("You are in", self.name)
        print(self.description)
        if self.item != "NULL":
            print("You find", self.item, "in this room.")
        if self.north != "NULL":
            print("To the north:", self.north.name)
        if self.south != "NULL":
            print("To the south:", self.south.name)
        if self.east != "NULL":
            print("To the east:", self.east.name)
        if self.west != "NULL":
            print("To the west:", self.west.name)
        print("\n")

