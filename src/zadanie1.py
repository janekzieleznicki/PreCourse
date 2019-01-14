import csv, sys
# import os
# from io import BytesIO
from zipfile import ZipFile
from more_itertools import peekable
from itertools import chain


class Table:
    def __init__(self, path="./rows_easy.txt"):
        with open(path,'rt') as csvfile:
            self.data = []
            rowreader = csv.reader(csvfile, delimiter='\t')
            for row in rowreader:
                print(row)
                self.data.append([int(str) for str in row])

    
    def calc_row(self, row):
        return max(row)-min(row)

    def calc_sheet(self, sheet):
        return sum(
            self.calc_row(row) for row in sheet
        )
    
    def control_sum(self):
        return self.calc_sheet(self.data)

class WordStatistics:
    def __init__(self, path="./words.zip"):
        self.load_from_file(path)

    def load_from_file(self, file_path):
        with open(file_path,'rb') as stream:
            self.zipfile = ZipFile(stream)
            self.files = {name: self.zipfile.read(name).decode('ascii').split()[0].lower() for name in self.zipfile.namelist()}
            
    
    def count_words(self):
        self.characters_stats = {}
        for file_content in self.files.values():
            for char in file_content:
                if(char in self.characters_stats):
                    self.characters_stats[char] = self.characters_stats[char]+1
                else:
                    self.characters_stats[char] = 1
        return self.characters_stats

class Trojkat:
    class Node:
        # self.left_child: Trojkat.Node
        # self.right_child: Trojkat.Node
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left_child = left
            self.right_child = right
        
        def has_children(self):
            return not(self.left_child == None and self.right_child == None)

        def __str__(self):
                return self.value

        def calc_cost_deeper(self):
            sys.setrecursionlimit(1101)
            if not(self.left_child.has_children() and self.right_child.has_children()):
                return [ self.left_child.value+self.value, self.right_child.value+self.value]
            else:
                costs = []
                costs.append([x+self.value for x in self.left_child.calc_cost_deeper()])
                costs.append([x+self.value for x in self.right_child.calc_cost_deeper()])
                return list(chain(*costs))
    class Costs:
        # self.left: list(int)
        # self.right: list(int)
        def __init__(self, vals):
            inits = []
            rvals = peekable(vals)
            for index in range(0 , len(vals)-1):
                inits.extend( [rvals.next(), rvals.peek()])
            self.left = [x for x in inits[0 : int(len(inits)/2)] ]
            self.right = [x for x in inits[int(len(inits)/2) : ]]
        def add(self, vals):
            if len(vals) == 1 :
                self.left = [x + vals[0] for x in self.left]
                self.right = [x + vals[0] for x in self.right] 
            elif len(vals) % 2 == 1:
                middle_index = int( (len(vals)-1) /2)+1 
                middle = vals[ middle_index]
                add_lefts = vals[0: middle_index-1]
                add_rights = vals[middle_index+1 :]
                add_left_iter = peekable(reversed(add_lefts))
                left_iter = reversed(self.left)
                add_right_iter = peekable(add_rights)
                right_iter = self.right.__iter__()
                
                l = next(left_iter)
                l += middle
                r = next(right_iter)
                r += middle

                to_add = 0
                while True:
                    try:
                        val = next(left_iter)
                        to_add = next(add_left_iter, to_add)
                        val = val + to_add
                    except StopIteration:
                        break

                to_add = 0
                while True:
                    try:
                        val = next(right_iter)
                        to_add = next(add_right_iter, to_add)
                        val = val + to_add
                    except StopIteration:
                        break
            else:
                middle_index = int( (len(vals)) /2) 
                add_lefts = vals[0: middle_index]
                add_rights = vals[middle_index :]
                add_left_iter = peekable(reversed(add_lefts))
                left_iter = reversed(self.left)
                add_right_iter = peekable(add_rights)
                right_iter = self.right.__iter__()
                
                to_add = 0
                while True:
                    try:
                        val = next(left_iter)
                        to_add = next(add_left_iter, to_add)
                        val = val + to_add
                    except StopIteration:
                        break

                to_add = 0
                while True:
                    try:
                        val = next(right_iter)
                        to_add = next(add_right_iter, to_add)
                        val = val + to_add
                    except StopIteration:
                        break
        def result(self):
            print(list(chain(*[self.left, self.right])))

    def __init__(self, path="./triangle.txt"):
        self.cost = None
        with open(path, 'rt') as data_file:
            for row in reversed(list(csv.reader(data_file, skipinitialspace=True , delimiter=' '))):
                row = [ int(x) for x in row if x != ' ' and x!='']
                if not self.cost:
                    self.cost = Trojkat.Costs(row);
                    # print(self.cost.left)
                    # print(self.cost.right)
                else:
                    self.cost.add(row)
                # if not self.nodes:
                #     self.nodes.append([Trojkat.Node(int(str)) for str in row])
                # else:
                #     previous_nodes = peekable(self.nodes[-1])
                #     self.nodes.append([
                #         Trojkat.Node(str,  next(previous_nodes) ,  previous_nodes.peek()) for str in row
                #     ])
    def print_values(self):
        for row in self.nodes:
            print( [val.value for val in row])
    def calc_cost(self):
        self.cost.result()
        # print(f'{self.nodes[-1][0].value}')
        # costs = self.nodes[-1][0].calc_cost_deeper()
        # for row in reversed(self.nodes):
        #     print([val.value for val in row])
        # print(f'Highest cost: {max(costs)}\nLowest cost: {min(costs)}')
        # print(costs)

if( __name__ == "__main__"):
    print(Table().control_sum())
    print('\n\n')
    print(Table("./rows.txt").control_sum())
    print('\n\n')
    print(WordStatistics("./zadanie_1_words.zip").count_words())
    print('\n\n')
    Trojkat().calc_cost()
    print('\n\n')
    # Trojkat('./zadanie_4_triangle_big.txt').calc_cost()