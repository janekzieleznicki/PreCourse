import csv

class Table():
    def __init__(self, csvfile=open('./rows.txt','rt')):
        self.data = []
        rowreader = csv.reader(csvfile, delimiter=' ')
        for row in rowreader:
            self.data.append([int(str) for str in row])

    
    def calc_row(self, row):
        return max(row)-min(row)

    def calc_sheet(self, sheet):
        return sum(
            self.calc_row(row) for row in sheet
        )
    
    def control_sum(self):
        return self.calc_sheet(self.data)