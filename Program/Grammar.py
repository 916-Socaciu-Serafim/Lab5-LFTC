from Program.ProductionSet import ProductionSet

class Grammar:

    def __init__(self, fileName):
        self.nonTerminals = []
        self.terminals = []
        self.startingSymbol = ""
        self.productionSet = ProductionSet()
        self.fileName = fileName
        self.isEnriched = False
        self.readFile()

    def readFile(self):
        fileContent = open(self.fileName, "r").readlines()
        self.nonTerminals = fileContent[0].split(" ")
        self.nonTerminals[len(self.nonTerminals) - 1] = self.nonTerminals[len(self.nonTerminals) - 1].strip()
        self.terminals = fileContent[1].split(" ")
        self.terminals[len(self.terminals) - 1] = self.terminals[len(self.terminals) - 1].strip()
        self.startingSymbol = fileContent[2].strip()
        for line in range(3, len(fileContent)):
            components = fileContent[line].split("->")
            components[len(components) - 1] = components[len(components) - 1].strip()
            leftHandSide = components[0]
            rightHandSide = components[1].split(" ")
            self.productionSet.addProduction(leftHandSide, rightHandSide)
        self.isEnriched = False


    def getEnrichedGrammar(self):
        if not self.isEnriched:
            newGrammar = Grammar(self.fileName)
            newGrammar.nonTerminals = self.nonTerminals
            newGrammar.terminals = self.terminals
            newGrammar.isEnriched = True
            newGrammar.startingSymbol = "S'"
            newGrammar.productionSet = self.productionSet
            newGrammar.nonTerminals.append("S'")
            newGrammar.productionSet.addProduction("S'", list(self.startingSymbol))
            return newGrammar