import datetime
import handlejson
import random

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
23:[0]}


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

words_probable = [ "sarnath", "in his house at r'lyeh dead cthulhu waits dreaming."]

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


handlejson.send_response(13, 0, "in his house at r'lyeh dead cthulhu waits", dt)
handlejson.send_response(15, 0, "in his house at r'lyeh dead cthulhu", dt)
handlejson.send_response(20, 0, "in his house at r'lyeh dead", dt)




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


