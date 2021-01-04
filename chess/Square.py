
class Square:
    def __init__(self, sq):
        self.sq = sq
        self.color = self.SqColor()
    def SqColor(self):
        color = 'Invalid square coordinates'
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        x = str(self.sq)
        k = 0
        if x[0] in letters:
            if int(x[1]) in range(len(letters)):
                for i in range(len(letters)):
                    for j in range(len(letters)):
                        if letters[i] == x[0] and str(j) == str(x[1]):
                            k = int(i)
                            break
                        else:
                            continue
        if k >= 0 and k <= 7 and int(x[1]) >= 0 and int(x[1]) <= 8:
            if (k + int(x[1]) - 1)%2 == 0:
                color = 'Black'
            else:
                color = 'White'
            return color   
        else:
            return color
    def isEqual(self, other):
        if self.sq == other.sq:
            return True
        else:
            return False
    def print(self):
        print(self.sq)