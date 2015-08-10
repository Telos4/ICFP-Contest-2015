import handlejson
import convert_class_to_letters

def send(gid,sid,mvlist):
	conv = convert_class_to_letters.convert_ilp(mvlist)
	handlejson.send_response(gid,[sid],conv)