

class Row:
    def __init__(self, action, goTo, reductionIndex):
        self.action = action
        self.goTo = goTo
        self.reductionIndex = reductionIndex

    def toString(self):
        if self.action == "REDUCE":
            return "REDUCE" + self.reductionIndex
        elif self.action == "ACCEPT":
            return "ACCEPT"
        elif self.action == "SHIFT":
            return "SHIFT" + self.goTo
