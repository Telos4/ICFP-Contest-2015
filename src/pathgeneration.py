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
    def __init__(self, width, height, filledCells):
        self.width = width
        self.height = height
        self.filledCells = filledCells

    def fill2DArray(self, workingBoard):
        # workingBoard: 2D-array to be filled according to self.filledCells
        col = []

        for i in range(self.width):
            for j in range(self.height):
                col.append(ds.Cell(i,j,False))
            workingBoard.append(col)
            col = []

        for cell in self.filledCells:
            workingBoard[cell.x][cell.y].full = True

class PathManager:
    def __init__(self, initial_board):
        self.working_board = None
        self.saved_boards = []

    def get_board(self, hash):
        pass

class Path:
    def __init__(self, path_manager, moves, board_at_start, active_unit, index_active_unit):
        self.moves = moves      # list of moves
        self.board_at_start = board_at_start    # hash value of the board at the start of the path
        self.active_unit = active_unit          # active unit
        self.index_active_unit = index_active_unit  # index of the active unit in the list of units that spawn

        self.path_manager = path_manager

        # generate end state of the board for the path
        self.generate_end_state()

    def generate_end_state(self):
        # get board state at start of the path
        b = self.path_manager.get_board(self.board_at_start)
        b.fill2D(self.path_manager.working_board)

        move_score = apply_moves(self.path_manager, self.moves, self.active_unit, self.index_active_unit)

        return move_score


    # def rate(self):
    #     # calculate end state for the path
    #     assert self.board is not None, "error: self.board is None -> cannot predict state"
    #     end_state = BoardManager.calc_board_state(self.board, self.moves)
    #
    #     self.rate_est = end_state.move_score #+ 10 * len(self.moves)

    def __lt__(self, other):
        return self.rate_est > other.rate_est

    def __add__(self, other):
        return Path(self.moves + other.moves, self.board)

    def __str__(self):
        return "moves: " + str(self.moves) + "\nrating: " + str(self.rate_est)