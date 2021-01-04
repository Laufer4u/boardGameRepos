from Square import Square
class Piece(Square):
    def __init__(self, coord, Type, color):
        self.coord = coord
        self.type = Type
        self.color = color
        self.square = Square(self.coord)
        self.name = self.name()
        self.value = self.createValue()
    def name(self):
        k = str(self.type[0])
        j = str(self.color[0])
        return str(j+k)
    def createValue(self):
        if self.type == 'None':
            return float(0)
        elif self.type == 'pawn':
            return float(1)
        elif self.type == 'knight':
            return float(2.9)
        elif self.type == 'bishop':
            return float(3)
        elif self.type == 'rook':
            return float(5)
        elif self.type == 'queen':
            return float(9)
        elif self.type == 'King':
            return float(60)
        else:
            return 'Invalid piece name'
    def clone(self):
        other = Piece(self.coord, self.type, self.color)
        return other
    def print(self):
        print([self.coord, self.type, self.color, self.square.color, self.value])

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
squaresUsingWhite = []
squaresUsingBlack = []
#######
whitePawns = []
blackPawns = []
for i in range(8):
    s = Square(str(letters[i])+str(2))
    s_ = Square(str(letters[6])+str(i + 1))
    p = Piece(s.sq, 'pawn', 'white')
    p_ = Piece(s_.sq, 'pawn', 'black')
    whitePawns.append(p)
    blackPawns.append(p_)
    squaresUsingWhite.append(s)
    squaresUsingBlack.append(s_)
piecesUsingWhite = whitePawns
piecesUsingBlack = blackPawns
#######
s1 = Square('B1')
s2 = Square('G1')
s3 = Square('G8')
s4 = Square('B8')
p1 = Piece(s1.sq, 'knight', 'white')
p2 = Piece(s2.sq, 'knight', 'white')
p3 = Piece(s3.sq, 'knight', 'black')
p4 = Piece(s4.sq, 'knight', 'black')

whiteKnights = [p1, p2]
blackKnights = [p3, p4]
squaresUsingWhite += [s1, s2]
squaresUsingBlack += [s3, s4]
piecesUsingWhite += [p1, p2]
piecesUsingBlack += [p3, p4]
#######
s1 = Square('C1')
s2 = Square('F1')
s3 = Square('F8')
s4 = Square('C8')
p1 = Piece(s1.sq, 'bishop', 'white')
p2 = Piece(s2.sq, 'bishop', 'white')
p3 = Piece(s3.sq, 'bishop', 'black')
p4 = Piece(s4.sq, 'bishop', 'black')

whiteBishops = [p1, p2]
blackBishops = [p3, p4]
squaresUsingWhite += [s1, s2]
squaresUsingBlack += [s3, s4]
piecesUsingWhite += [p1, p2]
piecesUsingBlack += [p3, p4]
#######
s1 = Square('A1')
s2 = Square('H1')
s3 = Square('H8')
s4 = Square('A8')
p1 = Piece(s1.sq, 'rook', 'white')
p2 = Piece(s2.sq, 'rook', 'white')
p3 = Piece(s3.sq, 'rook', 'black')
p4 = Piece(s4.sq, 'rook', 'black')

whiteRooks = [p1, p2]
blackRooks = [p3, p4]
squaresUsingWhite += [s1, s2]
squaresUsingBlack += [s3, s4]
piecesUsingWhite += [p1, p2]
piecesUsingBlack += [p3, p4]
#######
s1 = Square('D1')
s2 = Square('E1')
s3 = Square('E8')
s4 = Square('D8')
p1 = Piece(s1.sq, 'queen', 'white')
p2 = Piece(s2.sq, 'King', 'white')
p3 = Piece(s3.sq, 'King', 'black')
p4 = Piece(s4.sq, 'queen', 'black')

whiteRoyals = [p1, p2]
blackRooks = [p3, p4]
squaresUsingWhite += [s1, s2]
squaresUsingBlack += [s3, s4]
piecesUsingWhite += [p1, p2]
piecesUsingBlack += [p3, p4]
#######
for piece in piecesUsingWhite:
    piece.print()
for square in squaresUsingWhite:
    square.print()


for piece in whiteRoyals:
    piece.print()
