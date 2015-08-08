import json
from math import floor
from math import ceil
from copy import deepcopy
import string
import lcd_generator as lcd
import draw
import cv2

class BoardManager:
    def __init__(self, problem_dict):
        # create the board
        self.initial_board = Board(problem_dict['width'], problem_dict['height'], problem_dict['filled'])

        print self.initial_board

        # create list of units to spawn
        self.queued_units = [lcd.generate_random_sequence(seed, problem_dict['sourceLength'],
                                                          len(problem_dict['units'])) for seed in
                             problem_dict['sourceSeeds']]
        print self.queued_units

        self.unit_dict = problem_dict['units']

        self.l = 10  # prediction length

    def simulation(self, game_number):
        assert game_number < len(self.queued_units), "error: no such game"

        # create empty board
        board = self.initial_board

        movement_sequence = ['E', 'SE', 'SW', 'RC', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW',
                             'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE',
                             'SW', 'SE', 'SW', 'SE', 'SW', 'W', 'SE', 'SW', 'RC', 'RC', 'W', 'RCC']
        queued_units = self.queued_units[game_number]

        board = self.apply_sequence(board, None, queued_units, movement_sequence)


        # for unit_index in self.queued_units[game_number]:
        #     # spawn unit
        #     u = Unit(self.unit_dict[unit_index])
        #     u = u.moveToSpawnPosition(board.width)
        #     self.update_board(board, u)
        #
        #     print board
        #     pass

    def apply_sequence(self, board, active_unit, queued_units, movement_sequence):
        """
        Simulate the game starting with the current board state and apply the movement sequence
        for the active unit. If the unit becomes stuck the next unit in queued_units runs the
        movement sequence, and so on
        """
        if active_unit is None:
            # if there is currently no active unit we create a new unit
            active_unit = self.get_new_unit(board, queued_units)

        for m in movement_sequence:
            if active_unit is not None:
                # if there is an active unit, try moving it to new location
                moved_unit = active_unit.move(m)  # get location of unit after move

                if self.at_valid_location(board, moved_unit):
                    # move was valid -> unit is moved
                    active_unit = moved_unit
                else:
                    # move was invalid -> unit gets locked
                    self.lock_fields(board, active_unit)

                    # get new active unit
                    active_unit = self.get_new_unit(board, queued_units)

            if active_unit is not None:
                print board.plot(active_unit)
                board.plotcv(active_unit)

            if active_unit is None:
                # there are no more active units -> stop
                print "no more units in queue!"
                break

        return board

    def get_new_unit(self, board, queued_units):
        if len(queued_units) > 0:
            # when there are still units in the queue we create the next unit
            unit = Unit(self.unit_dict[queued_units.pop()])
            unit = unit.moveToSpawnPosition(board.width)
            if not self.at_valid_location(board, unit):
                print "spawn location was already occupied! -> Game over"
                unit = None
        else:
            # when there are no more units we return None
            unit = None
        return unit

    def at_valid_location(self, board, unit):
        for m in unit.members:
            # check whether field is already occupied
            if board.fields[m.x][m.y].full == True:
                print "moved unit to occupied space -> invalid location"
                return False
        return True

    def lock_fields(self, board, unit):
        """
        lock the fields of the given board for the members of the unit
        """
        for m in unit.members:
            if board.fields[m.x][m.y].full == True:
                print "error: field was already locked! this should not have happend!"
                raise
            board.fields[m.x][m.y].full = True
            board.filled.append(board.fields[m.x][m.y])


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
        self.fields = [[Cell(i, j) for j in xrange(self.height)] for i in xrange(self.width)]
        self.filled = [Cell(f["x"], f["y"], full=True) for f in filled]
        for f in self.filled:
            self.fields[f.x][f.y] = f

    def plot(self, unit):
        s = ''.join(['-' for i in xrange(self.width + 2)])
        s += '\n'
        for j in xrange(self.height):
            s += '|'
            for i in xrange(self.width):
                if (i,j) in [(m.x,m.y) for m in unit.members]:
                    s += 'u'
                else:
                    s += str(self.fields[i][j])
            s += '|\n'
        s += ''.join(['-' for i in xrange(self.width + 2)])
        return s

    def plotcv(self, unit):
        scale = 20
        img = draw.drawBoard(self.width, self.height, scale)
        for cell in self.filled:
            draw.drawCell(img, (255,0,0), cell.x, cell.y, scale)

        for cell in unit.members:
            draw.drawCell(img, (0,0,255), cell.x, cell.y, scale)

        draw.drawPivot(img, (0,255,0), unit.pivot.x, unit.pivot.y, scale)

        while not (cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.imshow('board', img)


    def __str__(self):
        """
        basic ascii output for debugging
        :return:
        """
        s = ''.join(['-' for i in xrange(self.width + 2)])
        s += '\n'
        for j in xrange(self.height):
            s += '|'
            for i in xrange(self.width):
                s += str(self.fields[i][j])
            s += '|\n'
        s += ''.join(['-' for i in xrange(self.width + 2)])
        return s


class Unit:
    def __init__(self, unit_dict):
        """
        :param unit_dict: dictionary generated from JSON representation for a single unit
        """
        self.members = [Cell(m["x"], m["y"]) for m in unit_dict["members"]]  # members
        self.pivot = Cell(unit_dict["pivot"]["x"], unit_dict["pivot"]["y"])  # pivot cell

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
        for i in range(int(floor((map_width - unit_width) / 2))):
            self = self.move('E')

        return self

    def move(self, direction):
        movedUnit = deepcopy(self)

        if direction == 'W':
            movedUnit.pivot.x = movedUnit.pivot.x - 1
            for cell in movedUnit.members:
                cell.x = cell.x - 1

        elif direction == 'E':
            movedUnit.pivot.x = movedUnit.pivot.x + 1
            for cell in movedUnit.members:
                cell.x = cell.x + 1

        elif direction == 'SW':
            if movedUnit.pivot.y % 2 == 0:
                movedUnit.pivot.x = movedUnit.pivot.x - 1
            movedUnit.pivot.y = movedUnit.pivot.y + 1

            for cell in movedUnit.members:
                if cell.y % 2 == 0:
                    cell.x = cell.x - 1
                cell.y = cell.y + 1

        elif direction == 'SE':
            if not movedUnit.pivot.y % 2 == 0:
                movedUnit.pivot.x = movedUnit.pivot.x + 1
            movedUnit.pivot.y = movedUnit.pivot.y + 1

            for cell in movedUnit.members:
                if not cell.y % 2 == 0:
                    cell.x = cell.x + 1
                cell.y = cell.y + 1

        elif direction == 'RCC':  # rotate conter-clockwise
            for cell in movedUnit.members:
                upRight = movedUnit.pivot.y - cell.y
                tempX = movedUnit.pivot.x
                if movedUnit.pivot.y % 2 == 0:
                    tempX = tempX + int(floor(upRight / 2.0))
                else:
                    tempX = tempX + int(ceil(upRight / 2.0))
                right = cell.x - tempX

                newY = movedUnit.pivot.y - upRight
                if movedUnit.pivot.y % 2 == 0:
                    newX = movedUnit.pivot.x - int(ceil(upRight / 2.0))
                else:
                    newX = movedUnit.pivot.x - int(floor(upRight / 2.0))

                newY = newY - right
                if (newY + right) % 2 == 0:
                    newX = newX + int(floor(right / 2.0))
                else:
                    newX = newX + int(ceil(right / 2.0))

                cell.x = newX
                cell.y = newY

        elif direction == 'RC':  # rotate clockwise
            for cell in movedUnit.members:
                upRight = movedUnit.pivot.y - cell.y
                tempX = movedUnit.pivot.x
                if movedUnit.pivot.y % 2 == 0:
                    tempX = tempX + int(floor(upRight / 2.0))
                else:
                    tempX = tempX + int(ceil(upRight / 2.0))
                right = cell.x - tempX

                newX = movedUnit.pivot.x + upRight
                newY = movedUnit.pivot.y + right
                if (newY - right) % 2 == 0:
                    newX = newX + int(floor(right / 2.0))
                else:
                    newX = newX + int(ceil(right / 2.0))

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
