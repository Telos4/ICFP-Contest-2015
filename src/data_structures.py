import json
from math import floor
from math import ceil
from copy import deepcopy

class Cell:
    """
    representation of a single cell on the board
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.full = False

class Map:
    """
    representation of the map
    """
    def __init__(self, map_dict):
        pass


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
