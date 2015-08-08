import json
from math import floor
from math import ceil
from copy import deepcopy
import string
import lcd_generator as lcd
import draw
import Queue
import random
try:
    import cv2
except ImportError:
    print "opencv not found"

class BoardManager:
    def __init__(self, problem_dict):
        # create list of units to spawn
        self.queued_units = [lcd.generate_random_sequence(seed, problem_dict['sourceLength'],
                                                          len(problem_dict['units'])) for seed in
                             problem_dict['sourceSeeds']]
        self.number_of_games = len(self.queued_units)

        self.unit_dict = problem_dict['units']
        self.width = problem_dict['width']
        self.height = problem_dict['height']
        self.filled = problem_dict['filled']

    def get_initial_board(self, game_number):
        board = Board(self.width, self.height, self.filled, self.unit_dict, self.queued_units[game_number])
        return board

    def simulation(self, map_number, game_number):
        assert game_number < self.number_of_games, "error: no such game"

        # create empty board
        board = self.get_initial_board(game_number)



        movement_sequence = ['E', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW',
                             'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE',
                             'SW', 'SE', 'SW', 'SE', 'SW', 'W', 'SE', 'SW', 'R+', 'R+', 'W', 'R-',
                             'E', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW',
                             'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE',
                             'SW', 'SE', 'SW', 'SE', 'SW', 'W', 'SE', 'SW', 'R+', 'R+', 'W', 'R-']

        board = self.calc_board_state(board, movement_sequence)

        print "board after movements: \n" + str(board)
        print "status: " + board.status

        board = self.get_initial_board(game_number)
        self.manual(board, map_number, game_number)

    def calc_board_state(self, board, movement_sequence):
        """
        Calculate final board state for a given movement sequence
        :param board:
        :param movement_sequence:
        :return:
        """
        if board.active_unit is None:
            # if there is currently no active unit we create a new unit
            board.active_unit = board.get_new_unit()

            # if this fails, then we loose
            if board.status == 'fail' or board.status == 'done':
                return board

        for m in movement_sequence:
            # if there is an active unit, try moving it to new location
            moved_unit = board.active_unit.move(m)  # get location of unit after move

            if board.at_valid_location(moved_unit):
                # move was valid -> unit is moved
                board.active_unit = moved_unit
            else:
                # move was invalid -> unit gets locked
                board.lock_fields(board.active_unit)

                # get new active unit
                board.active_unit = board.get_new_unit()

                # if this fails, or there are no more units return the board
                if board.status == 'fail' or board.status == 'done':
                    return board

            if board.active_unit is not None:
                print board.plot(board.active_unit)
            else:
                print str(board)

            pass


        return board

    def manual(self, board, map_number, game_number):
        """
        Simulate the game starting with the current board state and apply the movement sequence
        for the active unit. If the unit becomes stuck the next unit in queued_units runs the
        movement sequence, and so on
        """
        if board.active_unit is None:
            # if there is currently no active unit we create a new unit
            board.active_unit = board.get_new_unit()

            states = []
            visited = set()
            for cell in board.active_unit.members:
                visited.add((cell.x, cell.y))
            states.append(visited)

        movement_sequence = []

        #for m in movement_sequence:
        while True:
            if board.active_unit is not None:
                m = board.plotcv(board.active_unit)

                if m == ord('4'):
                    m = 'W'
                elif m == ord('6'):
                    m = 'E'
                elif m == ord('1'):
                    m = 'SW'
                elif m == ord('3'):
                    m = 'SE'
                elif m == ord('7'):
                    m = 'R+'
                elif m == ord('9'):
                    m = 'R-'
                elif m == ord('5'):
                    m = ' '
                    movement_sequence.append(m)
                    continue
                else:
                    break

                movement_sequence.append(m)

                # if there is an active unit, try moving it to new location
                moved_unit = board.active_unit.move(m)  # get location of unit after move

                if board.at_valid_location(moved_unit):
                    if self.already_visited(states, moved_unit):
                        break
                    else:
                        # move was valid -> unit is moved
                        board.active_unit = moved_unit
                else:
                    # move was invalid -> unit gets locked
                    board.lock_fields(board.active_unit)

                    # get new active unit
                    board.active_unit = board.get_new_unit()
                    states = []

            if board.active_unit is not None:
                visited = set()
                for cell in board.active_unit.members:
                    visited.add((cell.x, cell.y))
                states.append(visited)

                print board.plot(board.active_unit)

            if board.active_unit is None:
                # there are no more active units -> stop
                print "no more units in queue!"
                break

        answ = raw_input('save movements? (y/n)')
        if answ == 'y':
            filename = 'Movements/movements_map' + str(map_number) + '_game' + str(game_number) + '.txt'
            f = open(filename, 'w')
            f.write('mapId = ' + str(map_number) + '\n')
            f.write('seedIndex = ' + str(game_number) + '\n')
            f.write('movement_sequence = [')
            for i in range(len(movement_sequence)-1):
                f.write('\'' + movement_sequence[i] + '\',')
            f.write('\'' + movement_sequence[len(movement_sequence)-1] + '\']')
            f.close()

        return board

    def already_visited(self, states, unit):
        unitSet = set()
        for cell in unit.members:
            unitSet.add((cell.x,cell.y))
        for state in states:
            if len(unitSet.symmetric_difference(state)) == 0:
                print "already visited -> error"
                return True

        return False


class Path:
    def __init__(self, moves):
        self.moves = moves      # list of moves
        self.rate_est = 0.0

    def rate(self):
        # calculate end position for the current path
        pass

    def __gt__(self, other):
        return self.rate_est > other.rate_est

    def __add__(self, other):
        return self.moves.append(other.moves)



def clever_extend(path, good_segments):
    extends = Queue.PriorityQueue()

    # l = 10 # max lookahead
    # number_of_moves = random.randint(1,l)

    possible_moves = ['W', 'E', 'SW', 'SE', 'R+', 'R-']

    for i in xrange(6):
        extends.put(Path(possible_moves[i]))

    return extends

def generate_paths(oldpaths, good_segments):
    threshold = 0.5
    maxpaths = 100

    path_result = Queue.PriorityQueue()
    for path in oldpaths:
        extends = clever_extend(path, good_segments)

        if extends.empty():
            path_result.put(path)

        while not extends.empty():
            extended_path = extends.get()
            p_new = path + extended_path
            p_new.rate()

            if p_new.rate_est > threshold:
                path_result.put(p_new)

    while path_result.qsize() > maxpaths:
        path_result.get()

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
    def __init__(self, width, height, filled, unit_dict, queued_units):
        self.width = width
        self.height = height
        self.fields = [[Cell(i, j) for j in xrange(self.height)] for i in xrange(self.width)]
        self.filled = [Cell(f["x"], f["y"], full=True) for f in filled]
        self.status = 'good'

        self.active_unit = None
        self.unit_dict = unit_dict
        self.queued_units = queued_units

        for f in self.filled:
            self.fields[f.x][f.y] = f

    def get_new_unit(self):
        if len(self.queued_units) > 0:
            # when there are still units in the queue we create the next unit
            unit = Unit(self.unit_dict[self.queued_units.pop()])
            unit = unit.moveToSpawnPosition(self.width)
            if not self.at_valid_location(unit):
                print "spawn location was already occupied! -> Game over"
                self.status = 'fail'
                unit = None
        else:
            self.status = 'done'
            # when there are no more units we return None
            unit = None
        return unit

    def at_valid_location(self, unit):
        for m in unit.members:
            if m.x < 0 or m.x >= self.width or m.y < 0 or m.y >= self.height:
                print "moved out of the map -> invalid location"
                return False
            # check whether field is already occupied
            elif self.fields[m.x][m.y].full == True:
                print "moved unit to occupied space -> invalid location"
                return False
        return True

    def lock_fields(self, unit):
        """
        lock the fields of the given board for the members of the unit
        """
        for m in unit.members:
            if self.fields[m.x][m.y].full == True:
                print "error: field was already locked! this should not have happend!"
                raise
            self.fields[m.x][m.y].full = True
            self.filled.append(self.fields[m.x][m.y])

        self.update_fields_after_lock()

    def update_fields_after_lock(self):
        """
        check if any rows are completely filled and delete them
        """
        for j in xrange(self.height-1, -1, -1):
            # check if row is full
            # while because downshifted row can be full too...
            while all([self.fields[i][j].full for i in xrange(self.width)]):
                # delete the row
                for i in xrange(self.width):
                    self.fields[i][j].full = False

                # move all of the above rows one cell down
                for k in xrange(j, 1, -1):
                    for i in xrange(self.width):
                        self.fields[i][k].full = self.fields[i][k-1].full

                # update topmost layer separately
                for i in xrange(self.width):
                    self.fields[i][0].full = False

        # update list of filled cells on the board
        self.filled = []
        for i in xrange(self.width):
            for j in xrange(self.height):
                if self.fields[i][j].full == True:
                    self.filled.append(Cell(i,j, full=True))


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

        k = '0'
        """
        1: south-west
        3: south-east
        4: west
        5: nothing
        6: east
        7: rotate counterclockwise
        9: rotate clockwise
        q: exit
        """
        while not (k in [ord('1'),ord('3'),ord('4'),ord('5'),ord('6'),ord('7'),ord('9'),ord('q')]):
            cv2.imshow('board', img)
            k = cv2.waitKey(1)

        return k

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

        elif direction == 'R+':  # rotate conter-clockwise
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

        elif direction == 'R-':  # rotate clockwise
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

