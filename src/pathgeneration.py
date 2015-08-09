import json
from math import floor
from math import ceil
from copy import deepcopy
import string
import lcd_generator as lcd
import draw
import Queue
import random
import heapq
import data_structures as ds

import power_words

class SimpleBoard:
    def __init__(self, board):
        self.width = board.width
        self.height = board.height
        self.filledCells = []
        for y in xrange(self.height):
            for x in xrange(self.width):
                if board.fields[y][x].full == True:
                    self.filledCells.append(ds.Cell(x,y, True))
        print "done"

    def fill2DArray(self, workingBoard):
        for y in xrange(workingBoard.height):
            for x in xrange(workingBoard.width):
                workingBoard.fields[y][x].full = False

        for cell in self.filledCells:
            workingBoard.fields[cell.y][cell.x].full = True
            
class PathManager:
    def __init__(self, initial_board, unit_queue, units):
        self.saved_boards = {}      # hash table of SimpleBoards
        self.hash_initial_board = initial_board.generate_hash()
        self.saved_boards[self.hash_initial_board] = SimpleBoard(initial_board)

        self.working_board = initial_board
        self.unit_queue = unit_queue
        self.units = units

        self.threshold = 0.5

        random.seed(0)

    def run(self):
        paths_init = [Path(self, ['W'], self.hash_initial_board, deepcopy(self.units[self.unit_queue[0]]),0),
            Path(self, ['E'], self.hash_initial_board, deepcopy(self.units[self.unit_queue[0]]),0),
            Path(self, ['SW'], self.hash_initial_board, deepcopy(self.units[self.unit_queue[0]]),0),
            Path(self, ['SE'], self.hash_initial_board, deepcopy(self.units[self.unit_queue[0]]),0),
            Path(self, ['R+'], self.hash_initial_board, deepcopy(self.units[self.unit_queue[0]]),0),
            Path(self, ['R-'], self.hash_initial_board, deepcopy(self.units[self.unit_queue[0]]),0)]

        paths = []
        for p in paths_init:
            p.generate_and_rate()
            if p.rating >= 0:
                paths.append(p)
        for p in paths:
            assert p.board_at_end is not None, "error: board at end is none"

        heapq.heapify(paths)

        for i in xrange(100):
            print "run " + str(i+1)
            paths = self.generate_new_paths(paths, None)
            p1 = paths[-1]
            #p2 = paths[-2]
            self.saved_boards[p1.board_at_end].fill2DArray(self.working_board)
            print self.working_board.plot(p1.active_unit)
            print "path length = " + str(len(p1.moves))
            print "____________________________________"

        p = paths[-1]
        print "best path: " + str(p)


    def clever_extend(self, path, good_segments):
        # l = 10 # max lookahead
        # number_of_moves = random.randint(1,l)

        extends = [ ]

        possible_moves = ['W', 'E', 'SW', 'SE', 'R+', 'R-']

        number_of_additional_paths = 10

        for i in xrange(number_of_additional_paths):

            number_of_additional_moves = random.randint(1, 5)
            additonal_moves = []

            for i in xrange(number_of_additional_moves):
                additonal_moves.append(possible_moves[random.randint(0, 5)])

            new_path = Path(self, additonal_moves, path.board_at_end, path.active_unit, path.index_active_unit)
            new_path.generate_and_rate()
            extends.append(new_path)
        heapq.heapify(extends)

        return extends

    def generate_new_paths(self, oldpaths, good_segments):
        threshold = 0
        maxpaths = 25

        path_result = []
        while not len(oldpaths) == 0:
            print "print paths remaining = " + str(len(oldpaths))
            path = heapq.heappop(oldpaths)
            extends = self.clever_extend(path, good_segments)

            if len(extends) == 0:
                heapq.heappush(path_result, path)

            while not len(extends) == 0:
                extended_path = heapq.heappop(extends)
                #


                if extended_path.rating >= threshold:
                    p_new = path + extended_path
                    heapq.heappush(path_result, p_new)

            if len(path_result) == 0:
                heapq.heappush(path_result, path)

        while len(path_result) > maxpaths:
            heapq.heappop(path_result)

        return path_result

class Path:
    def __init__(self, path_manager, moves, board_at_start, active_unit, index_active_unit):
        self.moves = moves      # list of moves
        self.board_at_start = board_at_start    # hash value of the board at the start of the path
        self.active_unit = active_unit          # active unit
        self.index_active_unit = index_active_unit  # index of the active unit in the list of units that spawn

        self.path_manager = path_manager

        self.rating = None
        self.move_score = 0

        self.board_at_end = None

    def generate_and_rate(self):
        # generate end state of the board for the path
        move_score, final_board = self.generate_end_state()

        self.move_score = move_score

        self.rating = Path.calculate_rating(self.moves, self.move_score, final_board, self.active_unit)

        if self.rating >= 0:
            # calculate hash of final board
            self.board_at_end = final_board.generate_hash()     # generate and save hash value of board at end
            if not self.path_manager.saved_boards.has_key(self.board_at_end):
                self.path_manager.saved_boards[self.board_at_end] = SimpleBoard(final_board)
            else:
                #print "board already exists!"
                pass
        else:
            #print "path is bad!"
            pass


    @ staticmethod
    def calculate_rating(moves, move_score, final_board, active_unit):
        r = move_score + active_unit.pivot.y # + rate(final_board)
        return r



    def generate_end_state(self):
        # get board state at start of the path
        if self.board_at_start is None:
            print "is none"
        b = self.path_manager.saved_boards[self.board_at_start]
        b.fill2DArray(self.path_manager.working_board)  # fill working board

        move_score = self.apply_moves(self.path_manager.working_board, self.path_manager.unit_queue, self.path_manager.units)

        return move_score, self.path_manager.working_board

    def apply_moves(self, working_board, unit_queue, units):
        """
        Calculate final board state for a given movement sequence
        :param board:
        :param unit_queue:
        :return:
        """
        move_score = 0
        #print "-------------------------------------------------"

        if self.active_unit is None:
            # if there is currently no active unit we create a new unit
            self.index_active_unit += 1
            if self.index_active_unit == len(unit_queue):
                #print "no more unites available -> finnished"
                return move_score
            else:
                self.active_unit = deepcopy(units[unit_queue[self.index_active_unit]])
                #self.active_unit.moveToSpawnPosition(working_board.width)
        if not working_board.at_valid_location(self.active_unit):
            return move_score

        for m in self.moves:
            # if there is an active unit, try moving it to new location
            moved_unit = self.active_unit.move(m)  # get location of unit after move

            #print working_board.plot(self.active_unit)

            if working_board.already_visited(self.active_unit.states, moved_unit):
                #print "error: already visited!"
                move_score = -1000
                return move_score
            elif working_board.at_valid_location(moved_unit):
                # move was valid -> unit is moved
                self.active_unit = moved_unit
            else:
                # move was invalid -> unit gets locked
                move_score = working_board.lock_fields(self.active_unit)

                #print "Unit locked! New move score:   " + str(board.move_score)

                # get new active unit
                self.index_active_unit += 1
                if self.index_active_unit == len(unit_queue):
                    #print "no more unites available -> finnished"
                    return move_score
                else:
                    self.active_unit = deepcopy(units[unit_queue[self.index_active_unit]])
                    if not working_board.at_valid_location(self.active_unit):
                        return move_score
                    #self.active_unit.moveToSpawnPosition(working_board.width)

        return move_score

    # def rate(self):
    #     # calculate end state for the path
    #     assert self.board is not None, "error: self.board is None -> cannot predict state"
    #     end_state = BoardManager.calc_board_state(self.board, self.moves)
    #
    #     self.rate_est = end_state.move_score #+ 10 * len(self.moves)

    def __lt__(self, other):
        return self.rating < other.rating

    def __add__(self, other):
        assert self.path_manager == other.path_manager, "error: pathmanager sind nicht gleich!!"
        p_new = Path(self.path_manager, self.moves + other.moves, self.board_at_start, other.active_unit, other.index_active_unit)
        p_new.board_at_end = other.board_at_end
        p_new.rating = self.rating + other.rating
        p_new.move_score = self.move_score + other.move_score
        return p_new

    def __str__(self):
        return "moves: " + str(self.moves) + "\nrating: " + str(self.rating) + "\nmove_score: " + str(self.move_score)

class Board:
    """
    representation of the board
    """
    def __init__(self, width, height, filled):
        self.width = width
        self.height = height
        self.fields = [[ds.Cell(x, y) for x in xrange(self.width)] for y in xrange(self.height)]

        self.move_score = 0.0
        self.power_score = 0.0
        self.ls = 0     # number of lines cleared with current unit
        self.ls_old = 0 # number of lines cleared with previous unit

        self.filled = [ds.Cell(f["x"], f["y"], full=True) for f in filled]

        for f in self.filled:
            self.fields[f.y][f.x] = f

    def generate_hash(self):
        p1 = 53
        p2 = 101

        hashvalue = 0
        for y in xrange(self.height):
            for x in xrange(self.width):
                if self.fields[y][x].full == True:
                    hashvalue += x * p1 + y * p2
        return hashvalue

    def already_visited(self, states, unit):
        unitSet = set()
        for cell in unit.members:
            unitSet.add((cell.x,cell.y))
        for state in states:
            if len(unitSet.symmetric_difference(state)) == 0:
                #print "already visited -> error"
                return True
        return False

    def at_valid_location(self, unit):
        for m in unit.members:
            if m.x < 0 or m.x >= self.width or m.y < 0 or m.y >= self.height:
                #print "moved out of the map -> invalid location"
                return False
            # check whether field is already occupied
            elif self.fields[m.y][m.x].full == True:
                #print "moved unit to occupied space -> invalid location"
                return False
        return True

    def lock_fields(self, unit):
        """
        lock the fields of the given board for the members of the unit
        """
        points = 0
        for m in unit.members:
            if self.fields[m.y][m.x].full == True:
                print "error: field was already locked! this should not have happend!"
                raise
            self.fields[m.y][m.x].full = True
            points += 1

        self.update_fields_after_lock()

        # update points
        points += 100 * (1 + self.ls) * self.ls / 2.0
        line_bonus = floor((self.ls_old - 1) * points / 10.0) if self.ls_old > 1 else 0

        self.move_score += points + line_bonus

        self.ls_old = self.ls
        self.ls = 0

        return points + line_bonus

    def update_fields_after_lock(self):
        """
        check if any rows are completely filled and delete them
        """
        self.ls = 0
        for y in xrange(self.height-1, -1, -1):
            # check if row is full
            # while because downshifted row can be full too...
            while all([self.fields[y][x].full for x in xrange(self.width)]):
                # delete the row
                for j in xrange(self.width):
                    self.fields[y][x].full = False

                # move all of the above rows one cell down
                for k in xrange(y, 0, -1):
                    for x in xrange(self.width):
                        self.fields[k][x].full = self.fields[k-1][x].full

                # update topmost layer separately
                for x in xrange(self.width):
                    self.fields[0][x].full = False

                self.ls += 1 # count number of deleted rows        return "moves: " + str(self.moves) + "\nrating: " + str(self.rating)

    def plot(self, unit):
        if unit is not None:
            s = ''.join(['-' for x in xrange(self.width + 2)])
            s += '\n'
            for y in xrange(self.height):
                s += '|'
                for x in xrange(self.width):
                    if (x,y) in [(m.x,m.y) for m in unit.members]:
                        s += 'u'
                    else:
                        s += str(self.fields[y][x])
                s += '|\n'
            s += ''.join(['-' for x in xrange(self.width + 2)])

        else:
            s = ''.join(['-' for x in xrange(self.width + 2)])
            s += '\n'
            for y in xrange(self.height):
                s += '|'
                for x in xrange(self.width):
                    s += str(self.fields[y][x])
                s += '|\n'
            s += ''.join(['-' for x in xrange(self.width + 2)])
        return s