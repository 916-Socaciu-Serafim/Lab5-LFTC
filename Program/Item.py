

class Item:
    def __init__(self, lhs, rhs, dotPosition):
        self.lhs = lhs
        self.rhs = rhs
        self.dotPosition = dotPosition

    def sliceUntilDot(self):
        rhs1 = ""
        rhs2 = ""
        for i in range(0, self.dotPosition):
            rhs1 += self.rhs[i]
        for i in range(self.dotPosition, len(self.rhs)):
            rhs2 += self.rhs[i]
        return self.lhs + "->" + rhs1 + "." + rhs2