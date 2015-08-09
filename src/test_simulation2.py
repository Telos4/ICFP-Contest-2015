import data_structures
import handlejson
import check_word
import data
import convert_class_to_letters
import random
import time

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'


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

def firstpart(inputstring):
	inputstring_mv = convert_class_to_letters.convert_back_letter_to_classes(inputstring)


	
	a = check_word.possibleid(inputstring_mv)
	if a == None:
		return None
	g,s = a

	bm = data_structures.BoardManager(handlejson.parse_to_dictionary(data.datas[g]))
	score = bm.calc_board_state(bm.get_initial_board(s),inputstring_mv).move_score

	if score <0:
		return None

	handlejson.send_response(g,[allseeds[g][s]],inputstring,'qwe')

	return (g,s,inputstring,score)


def secondpart(inputstring):
	a = handlejson.get_dictionary_of_all_solutions()
	b = [ i for i in a if i['solution'] == inputstring ]

	#print b

	return b[0]['score']



listofstrings=[]


while True:
	for i in range(4):
		l = random.choice(range(10,11))
		#req = "".join([random.choice("abcdefghijklmnopqrstuvwxyz012345'!. ") for j in range(l) ])
		req = "".join([random.choice("pbaldk") for j in range(l) ])
		
		a = firstpart(req)

		if a == None:
			continue

		g,s,inputstring,score = a

		listofstrings.append((g,s,inputstring,score,None))

	print listofstrings
		
	while len( [ i for i in listofstrings if i[4] == None ] ) >= 1:
		time.sleep(20)
		for a in [ i for i in listofstrings if i[4] == None ]:
			g,s,inputstring,score,_ = a
			ret = secondpart(inputstring)
			if ret == None:
				continue
			listofstrings.remove((g,s,inputstring,score,None))
			listofstrings.append((g,s,inputstring,score,ret))

		print listofstrings


	diff = [ i for i in listofstrings if i[3] == i[4] ]

	print color.RED,diff,color.END



