import data
import data_structures
import handlejson
import convert_class_to_letters

def possibleid(a):
	mv = []
	if type(a) == str:
		mv = convert_class_to_letters.convert_back_letter_to_classes(a)
	else:
		mv = a
	for gameid in range(25):
		gamedata = data.datas[gameid]
		bm = data_structures.BoardManager(handlejson.parse_to_dictionary(gamedata))
		for seedid in range(len(bm.queued_units)):
			score = bm.calc_board_state(bm.get_initial_board(seedid),mv).move_score
			if score >= 0:
				#print gameid,seedid
				return (gameid,seedid)
	return None


