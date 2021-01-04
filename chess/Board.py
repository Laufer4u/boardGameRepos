from Square import Square
from Piece import Piece
class Board(Piece):
    def __init__(self, sq):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.square = Square(str(sq))
        self.piece = Piece(sq, 'pawn', 'white')
        self.game = self.game()        # [square] matrix
        #self.pieces = self.PiBoard()         # [square, piece] matrix
    def game(self):
        squares = []
        pieces = []
        colors = []
        for i in range(8):
            recent1 = []
            recent2 = []
            recent3 = []
            for j in range(8):      # board of squares
                g = str(self.letters[i])+str(j+1)
                sq = str(g)
                if (self.piece.square).isEqual(Square(sq)) == True:
                    piece = self.piece
                    ##
                    recent1.append(piece.square.sq)
                    recent2.append(piece.name)
                    recent3.append(piece.color)
                elif (self.piece.square).isEqual(Square(sq)) == False:
                    piece = Piece(sq, '_', ' ').clone()
                    ##
                    recent1.append(piece.square.sq)
                    recent2.append(piece.name)
                    recent3.append(piece.color)      
                    ##     
            squares.append(recent1)
            pieces.append(recent2)
            colors.append(recent3)
        for s in squares:
            print(*s)
        print('#####################')
        for s in pieces:
            print(*s)
        print('#####################')
        for s in colors:
            print(*s)
        return [squares, pieces, colors]
