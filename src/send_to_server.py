import handlejson
import convert_class_to_letters

def send(gid,sid,mvlist,tag):
    print "send_to_server = "
    print mvlist
    conv = convert_class_to_letters.convert_greedy(mvlist)
    handlejson.send_response(gid,[sid],conv,tag)

if __name__ == "__main__":
    tag = ''
    mvlist = ['E', 'R-', 'W', 'SE', 'E', 'E', 'SW', 'R-', 'W', 'SE', 'E', 'E', 'SW', 'W', 'R-', 'E', 'SW', 'W', 'W', 'SW', 'R-', 'R-', 'SW', 'E', 'SW', 'W', 'R-', 'W', 'W', 'SE', 'E', 'SW', 'W', 'R-', 'SW', 'E', 'E', 'E', 'SW', 'W', 'W', 'W', 'R-', 'SE', 'W', 'W', 'W', 'W', 'W', 'SE', 'E']
    send(10,0,mvlist,tag)

    mvlist = ['SW', 'SW', 'SW', 'W', 'SE', 'SW', 'SW', 'W', 'SW', 'SW', 'W', 'SE', 'SW', 'SW', 'W', 'SW', 'SW', 'W', 'SE', 'SW', 'SW', 'W', 'SW', 'SE', 'SE', 'SW', 'SW', 'R+', 'SE', 'SW', 'SE', 'R+', 'R+', 'E', 'SE', 'SW', 'R+', 'SE', 'R-', 'W', 'SE', 'E', 'E', 'SW', 'SE', 'R-', 'E', 'SW', 'R-', 'SE', 'E', 'R+', 'SW', 'R+', 'SE', 'SW', 'R+', 'SE', 'R+', 'SW', 'SW', 'R+', 'R+', 'SE', 'R-', 'R-', 'E', 'SW', 'SE', 'SW', 'SE', 'SW', 'W', 'R-', 'W', 'SE', 'E', 'E', 'SW', 'SE', 'E', 'E', 'R-', 'SE', 'SE', 'SE', 'SE', 'SW', 'E', 'SE', 'SE', 'E', 'R+', 'SW', 'SW', 'SE', 'R+', 'SW', 'SE', 'E', 'E', 'R-', 'SE', 'SE', 'SE', 'SE', 'SW', 'E', 'SE', 'SE', 'R+', 'R+', 'SW', 'R+', 'SW', 'SE', 'SW', 'SW', 'R+', 'SW', 'SW', 'SW', 'W', 'SE', 'SW', 'SW', 'W', 'E', 'SW', 'W', 'R+', 'R+', 'SW', 'R+', 'SW', 'SE', 'SW', 'SW', 'R+', 'SW', 'SE', 'R-', 'R-', 'SE', 'E', 'E', 'R-', 'SE', 'SE', 'SE', 'SE', 'SW', 'E', 'SE', 'SE', 'E', 'SW', 'W', 'SE', 'E', 'SW', 'W', 'R+', 'R+', 'E', 'R+', 'SE', 'E', 'SW', 'W', 'R+', 'SW', 'W', 'R+', 'R+', 'W', 'SW']
    send(0,0,mvlist,tag)