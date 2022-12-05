

class CannonicalCollection:

    def __init__(self):
        self.adjacencyList = {}
        self.states = []

    def connectState(self, indexFirstState, symbol, indexSecondState):
        self.adjacencyList[(indexFirstState, symbol)] = indexSecondState