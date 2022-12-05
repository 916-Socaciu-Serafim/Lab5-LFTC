

class State:
    def __init__(self, itemList):
        self.itemList = itemList
        self.stateType = ""
        self.getType()

    def getType(self):
        if len(self.itemList) == 1 and len(self.itemList[0].rhs) == self.itemList[0].dotPosition and self.itemList[0].lhs == "S'":
            self.stateType = "ACCEPT"
        elif len(self.itemList) == 1 and len(self.itemList[0].rhs) == self.itemList[0].dotPosition:
            self.stateType = "REDUCE"
        else:
            ok = True
            for i in self.itemList:
                if len(i.rhs) <= i.dotPosition:
                    ok = False
            if ok and len(self.itemList) != 0:
                self.stateType = "SHIFT"
            else:
                ok = True
                for i in self.itemList:
                    if len(i.rhs) != i.dotPosition:
                        ok = False
                if ok and len(self.itemList) > 1:
                    self.stateType = "REDUCE_REDUCE_CONFLICT"
                else:
                    self.stateType = "SHIFT_REDUCE_CONFLICT"

    def getSymbolsSucceding(self):
        symbols = []
        for item in self.itemList:
            if item.dotPosition in item.rhs.indices:
                symbols.append(item.rhs[item.dotPosition])
        return symbols

    def toString(self):
        return self.stateType + "-" + self.itemList