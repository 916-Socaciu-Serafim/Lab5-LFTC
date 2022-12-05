from Program.CannonicalCollection import CannonicalCollection
from Program.Item import Item
from Program.ParsingTreeRow import ParsingTreeRow
from Program.State import State
from Program.Table import TableRow
from Program.Row import Row


class LR:

    def __init__(self, grammar):
        self.grammar = grammar
        if grammar.isEnriched:
            self.workingGrammar = grammar
        else:
            self.workingGrammar = grammar.getEnrichedGrammar()
        self.orderedProductions = self.workingGrammar.productionSet.getOrderedProducts()

    def getDotPrecededNonTerminal(self, item):
        term = item.rhs.get(item.dotPosition)
        if term not in self.grammar.nonTerminals:
            return None
        return term

    def closure(self, item):
        oldClosure = []
        currentClosure = [item]
        while oldClosure != currentClosure:
            newClosure = currentClosure
            oldClosure = currentClosure
            for it in currentClosure:
                nonTerminal = self.getDotPrecededNonTerminal(it)
                for production in self.grammar.productionSet.get(nonTerminal):
                    currentItem = Item(nonTerminal, production, 0)
                    newClosure.append(currentItem)
            currentClosure = newClosure
        return State(currentClosure)

    def goTo(self, state, element):
        result = []
        for item in state.itemList:
            nonTerminal = item.rhs.get(item.dotPosition)
            if nonTerminal == element:
                nextItem = Item(item.lhs, item.rhs, item.dotPosition + 1)
                result.append(self.closure(nextItem).itemList)
        return State(result)

    def cannonicalCollection(self):
        canonicalCollection = CannonicalCollection()
        canonicalCollection.states.append(
            self.closure(
                Item(
                    self.workingGrammar.startingSymbol,
                    self.workingGrammar.productionSet.getProductionList()[self.workingGrammar.startingSymbol][0],
                    0
                )
            )
        )
        i = 0
        while i < len(canonicalCollection.states):
            for symbol in canonicalCollection.states[i].getSymbolsSucceding():
                newState = self.goTo(canonicalCollection.states[i], symbol)
                indexInStates = canonicalCollection.states.index(newState)
                if indexInStates == -1:
                    canonicalCollection.states.append(newState)
                    indexInStates = canonicalCollection.states[-1]
                canonicalCollection.connectState(i, symbol, indexInStates)

    def getParsingtable(self):
        cannonicalCollection = CannonicalCollection()
        table = TableRow([])
        for i in cannonicalCollection.adjacencyList:
            state = cannonicalCollection.states[i.first]
            if i.first not in table:
                table.tableRow[i.first] = Row(state.stateType, [], None)

        for (index, state) in cannonicalCollection.states:
            if state.stateType == "REDUCE":
                table.tableRow[index] = Row(state.stateType, None, None)
            if state.stateType == "ACCEPT":
                table.tableRow[index] = Row(state.stateType, None, None)
        return table

    def parse(self, word):
        workingStack = []
        remainingStack = []
        productionStack = []
        parsingTable = self.getParsingtable()
        #        workingStack.append(("$", 0))
        parsingTree = []
        treeStack = []
        currentIndex = 0
        while len(remainingStack) != 0 or len(workingStack) != 0:
            tableValue = parsingTable.tableRow[workingStack[-1]].second
            if tableValue.action == "SHIFT":
                token = remainingStack[0]
                goTo = tableValue.goTo
                value = goTo[token]
                workingStack.append((token, value))
                remainingStack.pop(0)
                currentIndex += 1
                treeStack.append((token, currentIndex))
            elif tableValue.action == "ACCEPT":
                lastElement = treeStack.pop(-1)
                parsingTree.append(ParsingTreeRow(lastElement.second, lastElement.first, -1, -1))
                return parsingTree
            elif tableValue.action == "REDUCE":
                productionIndexToReduceTo = self.orderedProductions[tableValue.reductionIndex]
                parentIndex = currentIndex + 1
                lastIndex = -1
                for j in range(0, len(productionIndexToReduceTo.second)):
                    workingStack.pop(-1)
                    lastElement = treeStack.pop(-1)
                    parsingTree.append(ParsingTreeRow(lastElement.second, lastElement.first, parentIndex, lastIndex))
                    lastIndex = lastElement.second
                treeStack.append((productionIndexToReduceTo.first, parentIndex))
                previous = workingStack.pop(-1)
                workingStack.append((productionIndexToReduceTo.first,
                                     parsingTable.tableRow[previous.second].goTo[productionIndexToReduceTo.first]))
