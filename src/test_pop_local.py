import data_structures
import data
import handlejson
import itertools
import convert_class_to_letters

pop=['ei!','ia! ia!','necronomicon','yuggoth','house','dead',"cthulhu r'lyeh"]
pop_mov=[ convert_class_to_letters.convert_back_letter_to_classes(i) for i in pop ]

#allmoves = list(itertools.product(pop,repeat=2))
allmoves = list(itertools.permutations(range(len(pop)),1))


for gameid in range(25):
	gamedata = data.datas[gameid]
	bm = data_structures.BoardManager(handlejson.parse_to_dictionary(gamedata))

	for seedid in range(len(bm.queued_units)):
		
		bestmove=(0,[])

		for currentmove in allmoves:
			testmove = [ i for a in currentmove for b in pop_mov[a] for i in b ]

			score = bm.calc_board_state(bm.get_initial_board(seedid),testmove).move_score

			if score >= -1:
				print 'the move',testmove,'yields',score,'points'
				if score > bestmove[0]:
					bestmove=(score,testmove)

		print 'bestmove',bestmove


