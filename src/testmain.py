import argparse
import handlejson
import main

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

print j

print

print j[0]

print

print j[1]

import convert_class_to_letters


for singlejson in j:
# do something
    l_mv=main.main2(singlejson, p, t, m, c)

    for i,seed in enumerate(singlejson):
        current_mv = l_mv[i]
        conv = convert_class_to_letters.convert_greedy(current_mv,p)
        handlejson.send_response(singlejson['id'],[seed],conv,'test')


#todo

arr_tuple_pid_seednr_tag_sol = []
for jinglejson in j:
    seeds = jinglejson['sourceSeeds']
    for seedIndex in range(len(seeds)):


arr_tuple_pid_seednr_tag_sol=[
(1,2,'','a'),
(3,4,'','b')
]
print

print handlejson.get_final_output(arr_tuple_pid_seednr_tag_sol)