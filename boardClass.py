#basic structure is to make the board then make an algorithm that finds and places possible canditates, then make our 
#backtracking algorithm 
import random
import copy

class Board:
    
    def __init__(self, nums):
        self.nums = nums #should be a 2-d list including blanks
        
    
    def __repr__(self):
        board = ''
        for x in range(9):
            for y in range(9):
                board += '|' 
                board += str(self.nums[x][y])
                board += '|'
            board += '\n'
        return board 
    
    #find the possible options for a given square 
    
    def find_options(self):
        options_list = []
        for x in range(9):
            for y in range(9):
                if self.nums[x][y] == 0:
                    row_options = self.row_options(x)
                    col_options = self.col_options(y)
                    box_options = self.box_options(x, y)
                    final_options = [x for x in row_options if x in col_options and x in box_options]
                    string_rep = str(x) + str(y)
                    final_options.insert(0, string_rep)
                    options_list.append(final_options)
        return options_list
                
    def row_options(self, row):
        row_options = [x for x in range(1,10) if x not in self.nums[row]]
        return row_options
    
        
    #if num is already in row or column return false
    def col_options(self, col):
        already_there = []
        for x in range(9):
            if self.nums[x][col] != 0:
                already_there.append(self.nums[x][col])
        col_options = [x for x in range(1,10) if x not in already_there]
        return col_options
                
    
    def box_options(self, row, col):
        ranges = box_ids(row, col)
        already_there = []
        for x in range(ranges[0], ranges[1]):
            for y in range(ranges[2], ranges[3]):
                if self.nums[x][y] != 0:
                    already_there.append(self.nums[x][y])
        box_options = [x for x in range(1,10) if x not in already_there] 
        return box_options         
    
    def is_win(self):
        for x in range(9):
            for y in range(9):
                if self.nums[x][y] == 0:
                    return False 
        return True 
    def next_empty(self):
        for x in range(9):
            for y in range(9):
                if self.nums[x][y] == 0:
                    return [x,y]
    
    def check_row(self, row, num):
        """Check if a given row already contains a number"""
        if num not in self.nums[row]:
            return True 
        else:
            return False 
        
    def check_col(self, col, num):
        for x in range(9): 
            if self.nums[x][col] == num:
                return False 
        return True 

    def check_box(self, row, col, num):
        ranges = box_ids(row, col)
        for x in range(ranges[0], ranges[1]):
            for y in range(ranges[2], ranges[3]):
                if self.nums[x][y] == num:
                    return False 
        return True 

    def check_placement(self, row, col, num):
        if self.check_row(row, num) == True and self.check_col(col, num) == True and self.check_box(row, col, num) == True :
            return True 
        return False
    
    def generate_random(self):
        copy_list = copy.deepcopy(self.nums)
        for x in range(9):
            for y in range(9):
                if copy_list[x][y] == 0:
                    copy_list[x][y] = random.randint(1, 9)
        return copy_list 
                
                


def box_ids(row, col):
    string = str(row) + str(col)
    ids = {'00':[0,3,0,3], '01': [0,3,0,3], '02': [0,3,0,3], '10': [0,3,0,3], 
           '11': [0,3,0,3], '12': [0,3,0,3], '20': [0,3,0,3], '21': [0,3,0,3], 
           '22': [0,3,0,3], '30': [3,6,0,3], '31':[3,6,0,3], '32':[3,6,0,3],
           '40': [3,6,0,3], '41': [3,6,0,3], '42':[3,6,0,3], '50': [3,6,0,3], 
           '51':[3,6,0,3], '52': [3,6,0,3], '60': [6,9,0,3], '61': [6,9,0,3], 
           '62': [6,9,0,3], '70': [6,9,0,3], '71': [6,9,0,3], '72': [6,9,0,3],
           '80': [6,9,0,3], '81': [6,9,0,3], '82': [6,9,0,3], '03': [0,3,3,6],
           '04': [0,3,3,6], '05': [0,3,3,6], '13':[0,3,3,6], '14': [0,3,3,6], 
           '15': [0,3,3,6], '23':[0,3,3,6], '24':[0,3,3,6], '25':[0,3,3,6],
           '33':[3,6,3,6], '34': [3,6,3,6], '35': [3,6,3,6], '43': [3,6,3,6], 
           '44': [3,6,3,6], '45':[3,6,3,6], '53': [3,6,3,6], '54':[3,6,3,6], 
           '55':[3,6,3,6], '63': [6,9,3,6], '64':[6,9,3,6], '65':[6,9,3,6], 
           '73':[6,9,3,6], '74':[6,9,3,6], '75':[6,9,3,6], '83':[6,9,3,6],
           '84':[6,9,3,6], '85':[6,9,3,6], '06':[0,3,6,9], '07':[0,3,6,9],
           '08':[0,3,6,9], '16':[0,3,6,9], '17':[0,3,6,9], '18':[0,3,6,9],
           '26':[0,3,6,9], '27':[0,3,6,9], '28':[0,3,6,9], '36': [3,6,6,9], 
           '37':[3,6,6,9], '38':[3,6,6,9], '46':[3,6,6,9], '47':[3,6,6,9],
           '48':[3,6,6,9], '56':[3,6,6,9], '57':[3,6,6,9], '58':[3,6,6,9], 
           '66':[6,9,6,9], '67':[6,9,6,9], '68':[6,9,6,9], '76':[6,9,6,9],
           '77':[6,9,6,9], '78':[6,9,6,9], '86':[6,9,6,9], '87':[6,9,6,9],
           '88':[6,9,6,9]}
    return ids[string]
    
