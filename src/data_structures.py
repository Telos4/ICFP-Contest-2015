import string

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

    def move(self, direction):
        """

        :param direction:
        :return:
        """
        pass


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