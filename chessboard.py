import numpy as np
from pieces import *

class chessboard:
    def __init__(self):
        self.board = np.zeros((8,8))
        self.board_pieces = {}
        for i in range(8):
            for j in range(8):
                self.board_pieces[(i,j)] = None
        self.populate_board()
        self.moves_translate = "abcdefgh"
        self.move_number = 0
    def populate_board(self):
        for i in range(8):
            self.board[0][i] = 1
            self.board[1][i] = 1
            self.board_pieces[(1,i)] = pawn((1,i),"white")
            self.board[6][i] = 1
            self.board[7][i] = 1
            self.board_pieces[(6,i)] = pawn((6,i),"black")

        self.board_pieces[(0,0)] = rook((0,0),"white")
        self.board_pieces[(0,7)] = rook((0,7),"white")

        self.board_pieces[(7,0)] = rook((7,0),"black")
        self.board_pieces[(7,7)] = rook((7,7),"black")

        self.board_pieces[(0,1)] = knight((0,1),"white")
        self.board_pieces[(0,6)] = knight((0,6),"white")

        self.board_pieces[(7,1)] = knight((0,1),"black")
        self.board_pieces[(7,6)] = knight((7,6),"black")

        self.board_pieces[(0,2)] = bishop((0,2),"white")
        self.board_pieces[(0,5)] = bishop((0,5),"white")
        
        self.board_pieces[(7,2)] = bishop((7,2),"black")
        self.board_pieces[(7,5)] = bishop((7,5),"black")
        
        self.board_pieces[(0,3)] = queen((0,3),"white")
        self.board_pieces[(7,3)] = queen((7,3),"black")

        self.board_pieces[(0,4)] = king((0,4),"white")
        self.board_pieces[(7,4)] = king((7,4),"black")

    def showboard(self):
        board_display = [[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                board_display[i].append("_ _")
        board_display = np.array(board_display)
        for key,val in self.board_pieces.items():
            if val != None:
                board_display[key[0]][key[1]] = "_" + val.display() + "_"
        #print(self.board)
        print(board_display)
        
    def get_move(self):
        error_msg = "Invalid Move"
        turn = "white"
        if self.move_number % 2 == 0:
            turn = "white"
            move = input("White to move: ")
            
        else:
            turn = "black"
            move = input("Black to move: ")
        
        if move == "f":
            if turn == "black":
                print("Resign. White is victorious.")
            else:
                print("Resign. Black is victorious.")
            return 0
        if len(move) != 4:
            print(error_msg)
            return
        
       
        col1 = self.moves_translate.index(move[0])
        row1 = int(move[1]) - 1
        
        col2 = self.moves_translate.index(move[2])
        row2 = int(move[3]) - 1
    

        if self.board_pieces[(row1,col1)] != None:
            if self.board_pieces[(row1,col1)].color == turn:
                piece = self.board_pieces[(row1,col1)]
                self.board_pieces[(row1,col1)] = None
                piece.move((row2,col2))
                self.board_pieces[(row2,col2)] = piece
            else:
                print(error_msg)
                return
        else:
            print(error_msg)
            return
        self.move_number += 1
        return 1

        


b = chessboard()
b.showboard()
while(b.get_move()):
    b.showboard()
    