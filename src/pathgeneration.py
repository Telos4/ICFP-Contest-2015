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

    def get2DArray(self):
        # workingBoard: 2D-array to be filled according to self.filledCells
        workingBoard = []
        row = []

        for j in range(self.height):
            for i in range(self.width):
                row.append(ds.Cell(i,j,False))
            workingBoard.append(row)
            row = []

        for cell in self.filledCells:
            workingBoard[cell.x][cell.y].full = True

        return workingBoard

def hash_board(board):
    p1 = 53
    p2 = 101
    hash = 0
    for x in len(board):
        for y in len(board[x]):
            if board[x][y].full == True:
                hash += x * p1 + y * p2
    return hash


class PathManager:
    def __init__(self, initial_board):
        self.working_board = None
        self.saved_boards = []      # hash table of SimpleBoards

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
            self.board_at_end = hash_board(final_board)
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

        # apply the movement sequence to the working board
        move_score = self.path_manager.apply_moves(self.moves, self.active_unit, self.index_active_unit)

        return move_score, self.path_manager.working_board

    def __lt__(self, other):
        return self.rating > other.rating

    def __add__(self, other):
        assert self.path_manager == other.path_manager, "error: pathmanager sind nicht gleich!!"
        return Path(self.path_manager, self.moves + other.moves, self.board_at_end, self.active_unit, self.index_active_unit)

    def __str__(self):
        return "moves: " + str(self.moves) + "\nrating: " + str(self.rating)