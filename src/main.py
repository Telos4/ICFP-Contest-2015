# dummy main
import lcd_generator as lcd
import handlejson
import data_structures
import os
from data import *

def main():
    print "ICFP 2015"

    map_number = 2

    if not os.path.exists('Movements'):
        os.makedirs('Movements')

    datalist = [data0, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10,
                data11, data12, data13, data14, data15, data16, data17, data18, data19, data20,
                data21, data22, data23, data24]

    # test JSON parser
    problem_dict = handlejson.parse_to_dictionary(datalist[map_number])



    # create a boardmanager
    boardmanager = data_structures.BoardManager(problem_dict)


    # size = len(boardmanager.queued_units[0])
    # id = 0
    # for i in xrange(810):
    #     #board = data_structures.Board(10,10,[],boardmanager.unit_dict,boardmanager.queued_units[0][:])
    #     #boardmanager.unit_dict[boardmanager.queued_units[0].pop(0)]
    #     id += 1
    # print id
    # for i in boardmanager.queued_units[0]:
    #     board = data_structures.Board(10,10,[],boardmanager.unit_dict,boardmanager.queued_units[0][:])
    #     board.plotcv(data_structures.Unit(boardmanager.unit_dict[boardmanager.queued_units[0].pop(810)]), id)
    #     id += 1
    # print id

    boardmanager.path_generation(0)


    #for game_number in range(len(boardmanager.queued_units)):
        #boardmanager.simulation(map_number, game_number)
        #boardmanager.playTetris(map_number, game_number)


if __name__ == "__main__":
    main()
