from enum import Enum

#Position is a tuple of the x and y coordinate (number,number)
#Move a piece according to rules


class pawn:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.move_count = 0

    def move(self, destination):
        if self.color == "white":
            if self.move_count == 0:
                if destination[0] == self.position[0] + 2:
                    self.position = destination
                    self.move_count += 1
                    return True 
            if destination[0] == self.position[0] + 1:
                self.position = destination
                self.move_count += 1
                return True
            else:
                print("That is an invalid move")
                return False
        elif self.color == "black":
            if self.move_count == 0:
                if destination[0] == self.position[0] - 2:
                    self.position = destination
                    self.move_count += 1
                    return True 
            if destination[0] == self.position[0] - 1:
                self.position = destination
                self.move_count += 1
                return True
            else:
                print("That is an invalid move")
                return False
    
    def display(self):
        if self.color == "white":
            return "wp"
        else:
            return "bp"


class knight:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        if destination[0] == self.position[0] + 1:
            if destination[1] == self.position[1] + 2:
                self.position = destination
                return True
            elif destination[1] == self.postion[1] - 2:
                self.position = destination
                return True
            else:
                print("That is an invalid move")
                return False
        elif destination[0] == self.position[0] - 1:
            if destination[1] == self.position[1] + 2:
                self.position = destination
                return True
            elif destination[1] == self.postion[1] - 2:
                self.position = destination
                return True
            else:
                print("That is an invalid move")
                return False
        elif destination[1] == self.position[1] + 1:
            if destination[0] == self.position[0] + 2:
                self.position = destination
                return True
            elif destination[0] == self.postion[0] - 2:
                self.position = destination
                return True
            else:
                print("That is an invalid move")
                return False
        elif destination[1] == self.position[1] - 1:
            if destination[0] == self.position[0] + 2:
                self.position = destination
                return True
            elif destination[0] == self.postion[0] - 2:
                self.position = destination
                return True
            else:
                print("That is an invalid move")
                return False
        else:
            print("That is an invalid move")
            return False

    def display(self):
        if self.color == "white":
            return "wN"
        else:
            return "bN"

class rook:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        if destination[0] == self.position[0]:
            self.position = destination
            return True
        elif destination[1] == self.position[1]:
            self.position = destination
            return True
        else:
            print("That is an invalid move")
            return False
    
    def display(self):
        if self.color == "white":
            return "wR"
        else:
            return "bR"

class bishop:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        x = abs(destination[0] - self.position[0])
        y = abs(destination[1] - self.position[1])
        if x == y:
            self.position = destination
            return True
        else:
            print("That is an invalid move")
            return False
    def display(self):
        if self.color == "white":
            return "wB"
        else:
            return "bB"

class king:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        if (abs(destination[0] - self.position[0]) <= 1) and (abs(destination[1] - self.position[1]) <= 1):
            self.position = destination
            return True
        else:
            print("That is an invalid move")
            return False
    def display(self):
        if self.color == "white":
            return "wK"
        else:
            return "bK"

class queen:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        x = destination[0] - self.position[0]
        y = destination[1] - self.position[1]
        if x == y:
            self.position = destination
            return True
        elif destination[0] == self.position[0]:
            self.position = destination
            return True
        elif destination[1] == self.position[1]:
            self.position = destination
            return True
        else:
            print("That is an invalid move")
            return False
    def display(self):
        if self.color == "white":
            return "wQ"
        else:
            return "bQ"


