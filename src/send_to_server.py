import handlejson
import convert_class_to_letters

def send(gid,sid,mvlist):
	conv = convert_class_to_letters.convert_greedy(mvlist)
	handlejson.send_response(gid,[sid],conv)

if __name__ == "__main__":
	import all_movements
	send(*all_movements.all_movements_computer_gen[-1])