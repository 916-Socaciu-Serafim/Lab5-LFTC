
class ProductionSet:

    def __init__(self):
        self.productions = {}

    def getProductionList(self):
        return self.productions

    def addProduction(self, key, value):
        if key not in self.productions.keys():
            self.productions[key] = value
        else:
            self.productions[key].extend(value)

    def getOrderedProducts(self):
        # to do
        productList = []
        for key in self.productions.keys():
            for value in self.productions.get(key):
                productList.append((self.productions.get(key)[0], value))
