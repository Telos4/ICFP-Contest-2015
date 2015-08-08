import datetime
import handlejson
import random
import os
import convert_class_to_letters
import all_movements


allseeds={0:[0],
1:[0],
2:[0, 679, 13639, 13948, 29639, 15385, 16783, 23862, 25221, 23027],
3:[0, 29060, 6876, 31960, 6094],
4:[0, 16868, 32001, 13661, 12352, 29707, 19957, 2584, 21791, 18451, 17818, 26137, 7533, 29971, 2895, 177, 8466, 17014, 23414, 23008, 15766, 6045, 13537, 31051, 12140, 26930, 28921, 8444, 29697, 8269, 12976, 28635, 16520, 22345, 22572, 12272, 6532, 2148, 23344, 19542, 22290, 2586, 19530, 11006, 8700, 30014, 21695, 26153, 13694, 20701],
5:[0, 22837, 22837, 15215, 24851, 11460, 14027, 32620, 32719, 15577],
6:[0, 13120, 18588, 31026, 7610, 25460, 23256, 19086, 24334, 22079, 9816, 8466, 3703, 13185, 26906, 16903, 24524, 9536, 11993, 21728, 2860, 13859, 21458, 15379, 10919, 7082, 26708, 8123, 18093, 26670, 16650, 1519, 15671, 24732, 16393, 5343, 28599, 29169, 8856, 23220, 25536, 629, 24513, 14118, 17013, 6839, 25499, 17114, 25267, 8780],
7:[0, 18705, 22828, 16651, 27669],
8:[0, 28581, 10596, 4491, 19012, 8000, 14104, 20240, 2629, 5696],
9:[0, 26637, 10998, 4150, 23855],
10:[0],
11:[0, 12877, 20528, 16526, 19558],
12:[0, 24762, 24103, 12700, 5864, 1155, 24803, 29992, 18660, 19102],
13:[0],
14:[0],
15:[0],
16:[0],
17:[0],
18:[0],
19:[0],
20:[0],
21:[0],
22:[0],
23:[0],
24:[18]}


pop_sure = ["necronomicon", "ei!", "ia! ia!",'yuggoth']

pop_never = ["elder things"]

# tested and seems not to be pops
# words_probable = ["cthulhu", "dagon", 
#                   "rhan-tegoth-cthulhu fthagn-ei! ei! ei! ei!-rhan-teogth.",
#                   "rhan-tegoth rhan-tegoth!",
#                   "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn",
#                   "h. p. lovecraft", "azathoth", "chaugnar faugn",
#                   "shoggoths"]


words_for_sure = ["r'lyeh"]

words_probable = [ "aleister crowley", "sarnath", "in his house at r'lyeh dead cthulhu waits dreaming."]

words_even_less_prob = ["derleth",
                        "zhar", "lloigor", "cyaegha", "nyogtha",
                        "tsathoggua", "aphoom-zhah", "cthugha",
                        "dagon","ghatanothoa",
                        "mother hydra","zoth-ommog", "gatanozoa",
                        "ghatanothoa", "arlyeh",
                        "great race"]


# worklist = words_for_sure + words_probable + words_even_less_prob
# random.shuffle(worklist)
# print len(worklist), worklist

dt = datetime.datetime.now().time().isoformat()
print dt
# for i,a in enumerate(worklist):
# 	idx = (i)%len(worklist)
# 	word = a.replace('-',' ')
# 	print 'sending',idx,word, '\ttag:', dt, '\ton seeds',allseeds[i]
# 	for s in allseeds[i]:
# 		handlejson.send_response(i, s, word, dt)
# 		print ''

# next_word = "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"
# word = "in his house at r'lyeh dead cthulhu waits dreaming."
# for i in range(24):
# 	for s in allseeds[i]:
# 		print 'sending', i,s,word
# 		handlejson.send_response(i, s, word, dt)


# testarray=[(1,"ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"),
# (3,"ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"),
# (6,"ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"),
# (7,"ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"),
# (8,"ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"),
# (9,"ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn"),
# ]

# testarray=[(7,"cthulhu r'lyeh wgah'nagl"),
# (10,"fhtagn"),
# (11,"cthulhu r'lyeh"),
# (12,"cthulhu r'lyeh wgah'nagl fhtagn"),
# (13,"wgah'nagl fhtagn"),
# (14,"gah'nagl fhtagn"),
# (15,"ah'nagl fhtagn"),
# (16,"h'nagl fhtagn"),
# (17,"h'nagl fhtagn"),
# ]

# testarray=[
# (11,"cthulhu r'lyeh"),
# #(13,"hou"),
# #(20,"dea"),
# ]

# for i,s in testarray:
# 	print i, s
# 	handlejson.send_response(i, allseeds[i],s,dt)

# testarray=[(5,"a! ia!"),
# (20,"ecronomicon"),
# (3,"uggoth"),
# ]

# for i,s in testarray:
# 	print i, s
# 	handlejson.send_response(i, allseeds[i],s,dt)


#handlejson.send_response(0, [0], "a4gji1rvp0gih4jg44jg4laaj4h 5hajlginnoqdd nm552nnnn5 m jooonnl5nhoo o am g lmhh4l nonllvz1ycc5 r5ooo5  ql5 ga55eenomolnah4r445mmhajahi0'mlqzq ojanogao i mmaijlhnomgigkaim4hpp mm  mcomiiij0i4oomd55y2bfaghjnlagmloo5rqhjgiimmmmybfjgja00!jhg4jihm cyb5lm5uhhgigjaahgg4ll n555immo loghmnnl4j4gh5g4a4mng1drnil5hhjol4ollo 55lammg4hgjn4 mn5hg4gmlgh4ij45lnnrddccbfonov115 nonr1rjo 5ajjhiglmmj5ni4no5m4iiagdajghggjghja44aghigilha5ivjghllngjaa''g44gj5 iigjohn5nbbll nn5odo4hmnlooocb5o4ojgj  y5224at4iiii  ogoaghglmyb mlgjmh4 lznhnlb2ere5ooon lmo nagh.pvagjailc2fqc5nggn4a4igg aao5vc5lnhhih'!g olgjhjpj4am pii55j0.'i43.'h445 oy5n5 52ld4q4qghhini1a4hby5r h4", dt)

# testarray=[
# (0,"ei!"),
# #(1,"ei!"),
# (2,"ei!"),
# (3,"yuggoth"),
# (4,"house"),
# (5,"ia! ia!"),
# (6,"ei!"),
# (7,"necronomicon"),
# (8,"ei!"),
# (9,"ei!"),
# (10,"dead"),
# (11,"cthulhu r'lyeh"),
# (12,"ei!"),
# (13,"necronomicon"),
# (14,"ei!"),
# (15,"cthulhu r'lyeh"),
# (16,"ei!"),
# (17,"ei!"),
# (18,"ei!"),
# (19,"agajaha4j4j4ajihoigh4j4 m40gjhha4al oaaaaiim lilolj4jaim3jghigio5n !olnmooggh4oggh4  oal5o44aihai 5ogg55 4iijj5j4.4i4ha5lnmo4!aa444jlmlmaj.4aihigmlmlmmlggg44momogg5 ih4jgan l ogjl4jjaja44j4om 3gia4ijia4l5 m!hjhjjjaiajggln4ihjaajgiiloalhj4hhgi4ijin5ooll iighijga45nlo....p.p0p'3p330!0'p0!..'!.''03..3efyceybyyfyefy2bcyccb2ef2b2eb2yfffc0.."),
# (20,"necronomicon"),
# (21,"ei!"),
# (22,"ei!"),
# (23,"ei!"),
# ]

# for i,s in testarray:
# 	print i, s
# 	handlejson.send_response(i, allseeds[i],s,dt)


# for gid,sid,mvseq in all_movements.all_movements:
# 	conv_mv_seq = convert_class_to_letters.convert_random(mvseq)
# 	handlejson.send_response(gid, [allseeds[gid][sid]],conv_mv_seq,dt)


# for i in range(0,8): handlejson.send_response(i, allseeds[i],"kyoto ni modoritai 4",dt)
for i in range(12,25): handlejson.send_response(i, allseeds[i],"ithaqua",dt)
for i in range(0,12): handlejson.send_response(i, allseeds[i],"trajectory",dt)
# for i in range(18,21): handlejson.send_response(i, allseeds[i],"hopeless",dt)
# for i in range(21,22): handlejson.send_response(i, allseeds[i],"kawahira",dt)
# for i in range(22,23): handlejson.send_response(i, allseeds[i],"niwasaki",dt)
# for i in range(23,25): handlejson.send_response(i, allseeds[i],"rotlast",dt)

#for i in range(25,26): handlejson.send_response(i, allseeds[i],"hasuta4",dt)

#for i in range(12,14): handlejson.send_response(i, allseeds[i],"wgah'nagl fhtagn",dt)

#for filename in os.listdir('Movements'):
# execfile('Movements/movements_map1_game0.txt')
# conv_mv_seq = convert_class_to_letters.convert_random(movement_sequence)
# handlejson.send_response(mapId, [allseeds[mapId][seedIndex]],conv_mv_seq,dt)



# handlejson.send_response( 2, allseeds[ 2], "cthulhu waits dreaming", dt)
# handlejson.send_response( 4, allseeds[ 4], "r'lyeh", dt)
# handlejson.send_response( 5, allseeds[ 5], "cthulhu", dt)
# handlejson.send_response(11, allseeds[11], "dreaming", dt)
# handlejson.send_response(12, allseeds[12], "dead cthulhu waits", dt)
# handlejson.send_response(13, allseeds[13], "house", dt)
# handlejson.send_response(15, allseeds[15], "in his house at r'lyeh", dt)
# handlejson.send_response(20, allseeds[20], "at r'lyeh dead", dt)
#handlejson.send_response(19, 0, "agajaha4j4j4ajihoigh4j4 m40gjhha4al oaaaaiim lilolj4jaim3jghigio5n !olnmooggh4oggh4  oal5o44aihai 5ogg55 4iijj5j4.4i4ha5lnmo4!aa444jlmlmaj.4aihigmlmlmmlggg44momogg5 ih4jgan l ogjl4jjaja44j4om 3gia4ijia4l5 m!hjhjjjaiajggln4ihjaajgiiloalhj4hhgi4ijin5ooll iighijga45nlo....p.p0p'3p330!0'p0!..'!.''03..3efyceybyyfyefy2bcyccb2ef2b2eb2yfffc0..", dt)



# print 'sending elder to 0'
# handlejson.send_response(0, 0, 'elder')
# print 'sending things to 1'
# handlejson.send_response(1, 0, 'things')
# print 'sending dagon to 2'
# handlejson.send_response(2, 0, 'dagon')

# requests = [(4,0,'necronomico'), (2,0,'dagon'), (20,0,'elder things')]

# for a,b,c in requests:
# 	print 'sending %s to %d, %d' % (c,a,b)
# 	handlejson.send_response(a,b,c)
# 	print ''


