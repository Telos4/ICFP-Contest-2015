import datetime
import handlejson

pop_sure = ["necronomicon", "ei!", "ia! ia!"]

# tested and seems not to be pops
# words_probable = ["cthulhu", "dagon", 
#                   "rhan-tegoth-cthulhu fthagn-ei! ei! ei! ei!-rhan-teogth.",
#                   "rhan-tegoth rhan-tegoth!",
#                   "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn",
#                   "h. p. lovecraft", "azathoth", "chaugnar faugn",
#                   "shoggoths"]


words_for_sure = ["r'lyeh", "yuggoth"]

words_probable = [ "sarnath", "in his house at r'lyeh dead cthulhu waits dreaming."]

words_even_less_prob = ["derleth",
                        "zhar", "lloigor", "cyaegha", "nyogtha",
                        "tsathoggua", "aphoom-zhah", "cthugha",
                        "dagon","ghatanothoa",
                        "mother hydra","zoth-ommog", "gatanozoa",
                        "ghatanothoa", "arlyeh", "elder things",
                        "great race"]


worklist = pop_sure + words_for_sure + words_probable + words_even_less_prob
print len(worklist)

s = sorted(worklist,key=len)

print datetime.datetime.now().time().isoformat()
for i,a in enumerate(s):
	idx = (i)%len(s)
	print 'sending',idx,a.replace('-','')
	handlejson.send_response(i, 0, a.replace('-',''), str(idx))
	print ''


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


