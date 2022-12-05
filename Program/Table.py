

class TableRow:

    def __init__(self, tableRow):
        self.tableRow = tableRow

    def toString(self):
        string = ""
        for (rowIndex, row) in self.tableRow.keys():
            string += rowIndex
            string += row
            string += "\n"
        return string