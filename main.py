from Program.Grammar import Grammar
from Program.LR import LR

if __name__ == '__main__':
    grammar = Grammar("resources\input.in")
    print("Non Terminals", grammar.nonTerminals)
    print("Terminals", grammar.terminals)
    print("Starting Symbol:", grammar.startingSymbol)
    print("Production Set", grammar.productionSet.getProductionList())

    lr = LR(grammar)
    cannonicalCollection = lr.cannonicalCollection()
    print("States")
    for i in cannonicalCollection.states.indices:
        print(i + cannonicalCollection.states[i])
    print("State transitions")
    for pair in cannonicalCollection.adjacencyList:
        print(pair.key + ":" + pair.value)
    parseTree = lr.parse(["a", "b", "b", "c"])
    for row in parseTree:
        print(row.index + ":" + row.info + ":" + row.parent + ":" + row.rightSibling)
