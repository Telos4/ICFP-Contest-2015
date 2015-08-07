import json
from math import floor
from math import ceil
from copy import deepcopy
import string
import  lcd_generator as lcd

class BoardManager:
    def __init__(self, problem_dict):
        # create the board
        self.initial_board = Board(problem_dict['width'], problem_dict['height'], problem_dict['filled'])

        print self.initial_board

        # create list of units to spawn
        self.unit_indizes = [lcd.generate_random_sequence(seed, problem_dict['sourceLength'],
                                                          len(problem_dict['units'])) for seed in
                             problem_dict['sourceSeeds']]
        print self.unit_indizes

        self.unit_dict = problem_dict['units']

    def simulation(self, game_number):
        assert game_number < len(self.unit_indizes), "error: no such game"

        # create empty board
        board = self.initial_board

        for unit_index in self.unit_indizes[game_number]:
            # spawn unit
            u = Unit(self.unit_dict[unit_index], board.width)
            pass


    def update_board(self, board, unit, sequence):
        pass

class Cell:
    """
    representation of a single cell on the board
    """
    def __init__(self, x, y, full=False):
        self.x = x
        self.y = y
        self.full = full

    def __str__(self):
        if self.full == True:
            return 'X'
        else:
            return ' '

class Board:
    """
    representation of the board
    """
    def __init__(self, width, height, filled):
        self.width = width
        self.height = height
        self.fields = [[Cell(i,j) for j in xrange(self.height)] for i in xrange(self.width)]
        self.filled = [Cell(f["x"], f["y"], full=True) for f in filled]
        for f in self.filled:
            self.fields[f.x][f.y] = f

    def __str__(self):
        """
        basic ascii output for debugging
        :return:
        """
        s = ''.join(['-' for i in xrange(self.width+2)])
        s += '\n'
        for j in xrange(self.height):
            s += '|'
            for i in xrange(self.width):
                s += str(self.fields[i][j])
            s += '|\n'
        s += ''.join(['-' for i in xrange(self.width+2)])
        return s


class Unit:
    def __init__(self, unit_dict):
        """
        :param unit_dict: dictionary generated from JSON representation for a single unit
        """
        self.members = [Cell(m["x"],m["y"]) for m in unit_dict["members"]]  # members
        self.pivot = Cell(unit_dict["pivot"]["x"], unit_dict["pivot"]["y"]) # pivot cell

    def moveToSpawnPosition(self, map_width):
        minX = map_width - 1
        maxX = 0

        for cell in self.members:
            if cell.x < minX:
                minX = cell.x
            if cell.x > maxX:
                maxX = cell.x
        
        unit_width = maxX - minX + 1
        # unit spawns in the middle of the first row
        for i in range( int(floor((map_width - unit_width) / 2)) ):
            self = self.move('E')

        return self

    def move(self, direction):
        movedUnit = deepcopy(self)

        if direction == 'W':
            movedUnit.pivot.x = movedUnit.pivot.x - 1
            for cell in moved.members:
                cell.x = cell.x - 1

        elif direction == 'E':
            movedUnit.pivot.x = movedUnit.pivot.x + 1
            for cell in movedUnit.members:
                cell.x = cell.x + 1

        elif direction == 'SW':
            if movedUnit.pivot.x % 2 == 0:
                movedUnit.pivot.x = movedUnit.pivot.x - 1
            movedUnit.pivot.y = movedUnit.pivot.y + 1

            for cell in movedUnit.members:
                if cell.x % 2 == 0:
                    cell.x = cell.x - 1
                cell.y = cell.y + 1

        elif direction == 'SE':
            if not movedUnit.pivot.x % 2 == 0:
                movedUnit.pivot.x = movedUnit.pivot.x + 1
            movedUnit.pivot.y = movedUnit.pivot.y + 1

            for cell in movedUnit.members:
                if not cell.x % 2 == 0:
                    cell.x = cell.x + 1
                cell.y = cell.y + 1

        elif direction == 'RCC': # rotate conter-clockwise
            for cell in movedUnit.members:
                upRight = movedUnit.pivot.y - cell.y
                right = movedUnit.pivot.x - cell.x
                if movedUnit.pivot.y % 2 == 0:
                    right = right + int(floor(upRight / 2))
                else:
                    right =  right + int(ceil(upRight / 2))

                newY = movedUnit.pivot.y - upRight
                if movedUnit.pivot.y % 2 == 0:
                    newX = movedUnit.pivot.x - int(ceil(upRight / 2))
                else:
                    newX = movedUnit.pivot.x - int(floor(upRight / 2))

                newY = newY + right
                if (newY-right) % 2 == 0:
                    newX = newX + int(floor(right / 2))
                else:
                    newX = newX + int(ceil(right / 2))

                cell.x = newX
                cell.y = newY

        elif direction == 'RC': # rotate clockwise
            for cell in movedUnit.members:
                upRight = movedUnit.pivot.y - cell.y
                right = movedUnit.pivot.x - cell.x
                if movedUnit.pivot.y % 2 == 0:
                    right = right + int(floor(upRight / 2))
                else:
                    right =  right + int(ceil(upRight / 2))

                newX = movedUnit.pivot.x + upRight
                newY = movedUnit.pivot.y + right
                if (newY-right) % 2 == 0:
                    newX = newX + int(floor(right / 2))
                else:
                    newX = newX + int(ceil(right / 2))

                cell.x = newX
                cell.y = newY

        return movedUnit

    # def __str__(self):
    #     mx = max([m.x ])
    #     b = [[" " for i in xrange(size)] for j in xrange(size)]
    #
    #     for m in self.members:
    #         b[m.x][m.y] = 'X'
    #
    #     b[self.pivot.x][self.pivot.y] = '.'
    #
    #
    #     s = ""
    #     for i in xrange(size):
    #         for j in xrange(size):
    #             s += b[i][j]
    #         s += "\n"
    #
    #     return s
