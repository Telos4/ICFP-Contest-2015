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
import power_words
import data_structures as ds

class SimpleBoard:
    def __init__(self, width, height, filledCells):
        self.width = width
        self.height = height
        self.filledCells = filledCells

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