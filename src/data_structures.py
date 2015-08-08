import json
from math import floor
from math import ceil
from copy import deepcopy
import string
import lcd_generator as lcd
import draw
import Queue
import random
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

    def simulation(self, map_number, game_number):
        assert game_number < len(self.queued_units), "error: no such game"

        # create empty board
        board = deepcopy(self.initial_board)

        movement_sequence = []

        # movement_sequence = ['E', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW',
        #                      'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE', 'SW', 'SE',
        #                      'SW', 'SE', 'SW', 'SE', 'SW', 'W', 'SE', 'SW', 'RC', 'RC', 'W', 'RCC']
        queued_units = self.queued_units[game_number]

        board = self.apply_sequence(board, None, queued_units, movement_sequence, map_number, game_number)


        # for unit_index in self.queued_units[game_number]:
        #     # spawn unit
        #     u = Unit(self.unit_dict[unit_index])
        #     u = u.moveToSpawnPosition(board.width)
        #     self.update_board(board, u)
        #
        #     print board
        #     pass

    def apply_sequence(self, board, active_unit, queued_units, movement_sequence, map_number, game_number):
        """
        Simulate the game starting with the current board state and apply the movement sequence
        for the active unit. If the unit becomes stuck the next unit in queued_units runs the
        movement sequence, and so on
        """
        if active_unit is None:
            # if there is currently no active unit we create a new unit
            active_unit = self.get_new_unit(board, queued_units)

            states = []
            visited = set()
            for cell in active_unit.members:
                visited.add((cell.x, cell.y))
            states.append(visited)

        movement_sequence = []

        #for m in movement_sequence:
        while True:
            if active_unit is not None:
                m = board.plotcv(active_unit)

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
                else:
                    break

                movement_sequence.append(m)

                # if there is an active unit, try moving it to new location
                moved_unit = active_unit.move(m)  # get location of unit after move

                if self.at_valid_location(board, moved_unit):
                    if self.already_visited(states, moved_unit):
                        # move was valid -> unit is moved
                        active_unit = moved_unit
                    else:
                        break
                else:
                    # move was invalid -> unit gets locked
                    self.lock_fields(board, active_unit)

                    # get new active unit
                    active_unit = self.get_new_unit(board, queued_units)

            if active_unit is not None:
                visited = set()
                for cell in active_unit.members:
                    visited.add((cell.x, cell.y))
                states.append(visited)

                print board.plot(active_unit)

            if active_unit is None:
                # there are no more active units -> stop
                print "no more units in queue!"
                break

        answ = raw_input('save movements? (y/n)')
        if answ == 'y':
            filename = 'Movements/movements_map' + str(map_number) + '_game' + str(game_number) + '.txt'
            f = open(filename, 'w')
            f.write('movement_sequence = [')
            for i in range(len(movement_sequence)-1):
                f.write('\'' + movement_sequence[i] + '\',')
            f.write('\'' + movement_sequence[len(movement_sequence)-1] + '\']')
            f.close()

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
            if m.x < 0 or m.x >= board.width or m.y < 0 or m.y >= board.height:
                print "moved out of the map -> invalid location"
                return False
            # check whether field is already occupied
            elif board.fields[m.x][m.y].full == True:
                print "moved unit to occupied space -> invalid location"
                return False

        return True

    def already_visited(self, states, unit):
        unitSet = set()
        for cell in unit.members:
            unitSet.add((cell.x,cell.y))
        for state in states:
            if len(unitSet.symmetric_difference(state)) == 0:
                print "already visited -> error"
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

        self.update_fields_after_lock(board)

    def update_fields_after_lock(self, board):
        """
        check if any rows are completely filled and delete them
        """
        for j in xrange(board.height-1, -1, -1):
            # check if row is full
            # while because downshifted row can be full too...
            while all([board.fields[i][j].full for i in xrange(board.width)]):
                # delete the row
                for i in xrange(board.width):
                    board.fields[i][j].full = False

                # move all of the above rows one cell down
                for k in xrange(j, 1, -1):
                    for i in xrange(board.width):
                        board.fields[i][k].full = board.fields[i][k-1].full

                # update topmost layer separately
                for i in xrange(board.width):
                    board.fields[i][0].full = False

        # update list of filled cells on the board
        board.filled = []
        for i in xrange(board.width):
            for j in xrange(board.height):
                if board.fields[i][j].full == True:
                    board.filled.append(Cell(i,j, full=True))


class Path:
    def __init__(self, moves):
        self.moves = moves      # list of moves
        self.rate_est = 0

    def rate(self):
        pass

    def __gt__(self, other):
        return self.rate_est > other.rate_est

    def __add__(self, other):
        return self.moves.append(other.moves)



def clever_extend(path, good_segments):
    extends = Queue.PriorityQueue()
    l = 10 # lookahead
    number_of_moves = random.randint(1,l)

    for i in xrange(3):
        moves = []
        for j in xrange(number_of_moves):
            moves.append()



    pass

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

#     std::priority_queue<path> clever_extend(path p, std::priority_queue<path> good_segments){
#   srand (time(NULL));
#   std::priority_queue<path> extends;
#   int new_entries = rand() % 10 + 1;
#   for(int i = 0; i < 3; i++)
#   {
#     path dummy;
#     for(int j = 0; j < new_entries; j++)
#     {
#       dummy.moves.append(std::to_string(rand() % 6));
#     }
#     extends.push(dummy);
#   }
#   return extends;
# }


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

