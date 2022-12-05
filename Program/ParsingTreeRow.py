
class ParsingTreeRow:
    def __init__(self, index, info, parent, rightSibling):
        self.index = index
        self.info = info
        self.parent = parent
        self.rightSibling = rightSibling