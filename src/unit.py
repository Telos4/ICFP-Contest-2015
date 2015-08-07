import json

class Cell:
    """
    representation of a single cell on the board
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Unit:
    def __init__(self, unit_dict):
        """
        :param unit_dict: dictionary generated from JSON representation for a single unit
        """
        self.members = [Cell(m["x"],m["y"]) for m in unit_dict["members"]]  # members
        self.pivot = Cell(unit_dict["pivot"]["x"], unit_dict["pivot"]["y"]) # pivot cell

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