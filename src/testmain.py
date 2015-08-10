import argparse
import handlejson


parser = argparse.ArgumentParser(description='H. P. Wagner, ICFP 2015')

parser.add_argument('-f', type=list, nargs='+', action='append')
parser.add_argument('-t', type=int)
parser.add_argument('-m', type=int)
parser.add_argument('-c', type=int)
parser.add_argument('-p', type=list, nargs='+', action='append')

args = parser.parse_args()

f = [ "".join(i[0]) for i in args.f ]
t = args.t
m = args.m
c = args.c
p = [ "".join(i[0]) for i in args.p ]

print f,t,m,c,p


j = [ handlejson.parse_to_dictionary(open(i).read()) for i in f ]

"""
print j

print

print j[0]

print

print j[1]


# do something
"""

for map_ in j:
    # old code:
    
    # create a boardmanager
    boardmanager = BoardManager(j)


    boardmanager.path_generation()

    r = boardmanager.calc_board_state(boardmanager.get_initial_board(s), sys.argv[1])
    print "sim says:",r.move_score


## output format
arr_tuple_pid_seednr_tag_sol=[
(1,2,'','a'),
(3,4,'','b')
]
print

print handlejson.get_final_output(arr_tuple_pid_seednr_tag_sol)
