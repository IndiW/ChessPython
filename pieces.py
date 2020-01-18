from enum import Enum

#Position is a tuple of the x and y coordinate (number,number)
#Move a piece according to rules


class pawn:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        if self.color == "white":
            if destination[0] == self.position[0] + 1:
                self.position = destination
            else:
                print("That is an invalid move")
        elif self.color == "black":
            if destination[0] == self.position[0] - 1:
                self.position = destination
            else:
                print("That is an invalid move")
    
    def display(self):
        return "p"


class knight:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        if destination[0] == self.position[0] + 1:
            if destination[1] == self.position[1] + 2:
                self.position = destination
            elif destination[1] == self.postion[1] - 2:
                self.position = destination
            else:
                print("That is an invalid move")
        elif destination[0] == self.position[0] - 1:
            if destination[1] == self.position[1] + 2:
                self.position = destination
            elif destination[1] == self.postion[1] - 2:
                self.position = destination
            else:
                print("That is an invalid move")
        elif destination[1] == self.position[1] + 1:
            if destination[0] == self.position[0] + 2:
                self.position = destination
            elif destination[0] == self.postion[0] - 2:
                self.position = destination
            else:
                print("That is an invalid move")
        elif destination[1] == self.position[1] - 1:
            if destination[0] == self.position[0] + 2:
                self.position = destination
            elif destination[0] == self.postion[0] - 2:
                self.position = destination
            else:
                print("That is an invalid move")
        else:
            print("That is an invalid move")

    def display(self):
        return "N"

class rook:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        if destination[0] == self.position[0]:
            self.position = destination
        elif destination[1] == self.position[1]:
            self.position = destination
        else:
            print("That is an invalid move")
    
    def display(self):
        return "R"

class bishop:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        x = abs(destination[0] - self.position[0])
        y = abs(destination[1] - self.position[1])
        print(x)
        print(y)
        if x == y:
            self.position = destination
        else:
            print("That is an invalid move")
    def display(self):
        return "B"

class king:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        if (abs(destination[0] - self.position[0]) <= 1) and (abs(destination[1] - self.position[1]) <= 1):
            self.position = destination
        else:
            print("That is an invalid move")
    def display(self):
        return "K"

class queen:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, destination):
        x = destination[0] - self.position[0]
        y = destination[1] - self.position[1]
        if x == y:
            self.position = destination
        elif destination[0] == self.position[0]:
            self.position = destination
        elif destination[1] == self.position[1]:
            self.position = destination
        else:
            print("That is an invalid move")
    def display(self):
        return "Q"


#newrook = king((0, 0), "white")
#print(newrook.position)
#newrook.move((0,1))
#print(newrook.position)

#8
#7
#6
#5
#4
#3
#2
#1
#  a b c d e f g h
