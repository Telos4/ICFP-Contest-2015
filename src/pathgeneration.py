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
        self.width = len(board)
        self.height = len(board[0])
        self.filledCells = []
        for i in xrange(self.width):
            for j in xrange(self.height):
                if board[i][j].full == True:
                    self.filledCells.append(ds.Cell(i,j, True))

    def fill2DArray(self, workingBoard):
        for cell in self.filledCells:
            workingBoard[cell.x][cell.y].full = True
            
class PathManager:
    def __init__(self, initial_board):
        self.working_board = None
        self.saved_boards = {}      # hash table of SimpleBoards

        self.threshold = 0.5


    def clever_extend(self, path, good_segments):
        # l = 10 # max lookahead
        # number_of_moves = random.randint(1,l)

        extends = [ ]

        possible_moves = ['W', 'E', 'SW', 'SE']#, 'R+', 'R-']

        for i in xrange(10):

            number_of_additional_moves = random.randint(1, 10)
            additonal_moves = []

            for i in xrange(number_of_additional_moves):
                additonal_moves.append(possible_moves[random.randint(0, 3)])

            new_path = Path(self, additonal_moves, path.board_at_end, path.active_unit, path.index_active_unit)
            extends.append(new_path)
        heapq.heapify(extends)

        return extends

    def generate_paths(self, oldpaths, good_segments):
        threshold = 0.5
        maxpaths = 100

        path_result = []
        while not len(oldpaths) == 0:
            print "print paths remaining = " + str(len(oldpaths))
            path = heapq.heappop(oldpaths)
            extends = self.clever_extend(path, good_segments)

            if len(extends) == 0:
                heapq.heappush(path_result, path)

            while not len(extends) == 0:
                extended_path = heapq.heappop(extends)
                p_new = path + extended_path
                p_new.rate()

                if p_new.rate_est > threshold:
                    heapq.heappush(path_result, p_new)

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

        # generate end state of the board for the path
        move_score, final_board = self.generate_end_state()

        self.rating = Path.calculate_rating(self.moves, move_score, final_board)

        if self.rating > path_manager.threshold:
            # calculate hash of final board
            self.board_at_end = final_board.generate_hash()     # generate and save hash value of board at end
            if path_manager.saved_boards[self.board_at_end] is not None:
                path_manager.saved_boards[self.board_at_end] = SimpleBoard(final_board)
            else:
                print "board already exists!"

    @ staticmethod
    def calculate_rating(moves, move_score, final_board):
        r = move_score + len(moves) # + rate(final_board)
        return r



    def generate_end_state(self):
        # get board state at start of the path
        b = self.path_manager.get_board(self.board_at_start)
        b.fill2DArray(self.path_manager.working_board)  # fill working board

        move_score = self.apply_moves(self.path_manager.working_board, self.path_manager.unit_queue)

        return move_score, self.path_manager.working_board

    def apply_moves(self, working_board, unit_queue):
        """
        Calculate final board state for a given movement sequence
        :param board:
        :param unit_queue:
        :return:
        """
        move_score = 0

        if self.active_unit is None:
            # if there is currently no active unit we create a new unit
            self.index_active_unit += 1
            if self.index_active_unit == len(unit_queue):
                #print "no more unites available -> finnished"
                return move_score
            else:
                self.active_unit = unit_queue[self.index_active_unit]

        for m in self.moves:
            # if there is an active unit, try moving it to new location
            moved_unit = self.active_unit.move(m)  # get location of unit after move

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
                    self.active_unit = unit_queue[self.index_active_unit]

        return move_score

    # def rate(self):
    #     # calculate end state for the path
    #     assert self.board is not None, "error: self.board is None -> cannot predict state"
    #     end_state = BoardManager.calc_board_state(self.board, self.moves)
    #
    #     self.rate_est = end_state.move_score #+ 10 * len(self.moves)

    def __lt__(self, other):
        return self.rating > other.rating

    def __add__(self, other):
        assert self.path_manager == other.path_manager, "error: pathmanager sind nicht gleich!!"
        return Path(self.path_manager, self.moves + other.moves, self.board_at_end, self.active_unit, self.index_active_unit)

    def __str__(self):
        return "moves: " + str(self.moves) + "\nrating: " + str(self.rate_est)

class Board:
    """
    representation of the board
    """
    def __init__(self, width, height, filled):
        self.width = width
        self.height = height
        self.fields = [[ds.Cell(i, j) for j in xrange(self.height)] for i in xrange(self.width)]

        self.move_score = 0.0
        self.power_score = 0.0
        self.ls = 0     # number of lines cleared with current unit
        self.ls_old = 0 # number of lines cleared with previous unit

        for f in filled:
            self.fields[f.x][f.y].full = True

    def generate_hash(self):
        p1 = 53
        p2 = 101

        hashvalue = 0
        for i in self.height:
            for j in self.width:
                if self.fields[i][j].full == True:
                    hashvalue += i * p1 + j * p2
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
            elif self.fields[m.x][m.y].full == True:
                #print "moved unit to occupied space -> invalid location"
                return False
        return True

    def lock_fields(self, unit):
        """
        lock the fields of the given board for the members of the unit
        """
        points = 0
        for m in unit.members:
            if self.fields[m.x][m.y].full == True:
                print "error: field was already locked! this should not have happend!"
                raise
            self.fields[m.x][m.y].full = True
            self.filled.append(self.fields[m.x][m.y])
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
        for j in xrange(self.height-1, -1, -1):
            # check if row is full
            # while because downshifted row can be full too...
            while all([self.fields[i][j].full for i in xrange(self.width)]):
                # delete the row
                for i in xrange(self.width):
                    self.fields[i][j].full = False

                # move all of the above rows one cell down
                for k in xrange(j, 0, -1):
                    for i in xrange(self.width):
                        self.fields[i][k].full = self.fields[i][k-1].full

                # update topmost layer separately
                for i in xrange(self.width):
                    self.fields[i][0].full = False

                self.ls += 1 # count number of deleted rows        return "moves: " + str(self.moves) + "\nrating: " + str(self.rating)