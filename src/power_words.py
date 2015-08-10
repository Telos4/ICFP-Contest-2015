#!/usr/bin/python

inp = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'

inv_map = {e: k for k, v in inp.items() for e in v}

"""
words of power go in lowercase because of matching
"""
words_for_sure = ["ei!", "ia! ia!", "r'lyeh", "yuggoth",
                  "necronomicon", "house", "dead", "cthulhu r'lyeh",
                  "wgah'nagl fhtagn"]

words_probable = ["the damned place must be honeycombed",
                  "massachusetts", "boston", "cambridge", "gloucester",
                  "hadley", "haverhill", "ipswich", "marblehead",
                  "salem", "new hampshire",
                  "rhode island", "providence", "vermont",
                  "brattleboro", "townshend", "dagon",
                  "rhan-tegoth-cthulhu fthagn-ei! ei! ei! ei!-rhan-teogth.",
                  "rhan-tegoth rhan-tegoth!",
                  "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn",
                  "h. p. lovecraft", "azathoth", "chaugnar faugn",
                  "shoggoths", "lilith", "xllth",
                  "in his house at r'lyeh dead cthulhu waits dreaming",
                  "watch me in the sky close by the daemon-star",
                  "that throb down in the ground", "democritus", "sarnath",
                  "god! if you could see what i am seeing!", "oida!",
                  "fata viam invenient", "marvells of science",
                  "ygnaiih . . . ygnaiih . . . thflthkh'ngha . . . yog-sothoth . . .",
                  "ygnaiih... ygnaiih... thflthkh'ngha... yog-sothoth..."]

words_even_less_prob = ["derleth",
                        "zhar", "lloigor", "cyaegha", "nyogtha",
                        "tsathoggua", "aphoom-zhah", "cthugha",
                        "dagon", "ghatanothoa",
                        "mother hydra", "zoth-ommog", "gatanozoa",
                        "ghatanothoa", "arlyeh", "elder things",
                        "great race", "apocalypse", "arrival of the messiah",
                        "defeat unholy trinity", "end of world",
                        "cataclysm", "devastation"]

"""
https://lovecraftbookclub.wordpress.com/the-lovecraft-dictionary/
https://en.wiktionary.org/wiki/Concordance:HP_Lovecraft
Lebensdaten: 20. August 1890 in Providence, Rhode Island; 15. Maerz 1937
"""
more_words = ["angarola", "call of cthulhu", "pickman's model",
              "antediluvian", "cotton mather", "cyclopean", "cymric",
              "eldritch", "fuseli", "grotto", "hadoth", "akhematen",
              "amarna", "neb",  "priory", "sime", "regnum congo",
              "pigafetta", "providence", "rhode island",
              "15.3", "3.15", "15.03", "03.15"]
# see "words.txt":
# + noch http://arkhamarchivist.com/wordcount-lovecraft-favorite-words/
even_more = ["abnormal",
"aeon",
"aesthetes",
"alienated",
"alienists",
"amorphous",
"archeological",
"anxious",
"babylon",
"bizarre",
"bungalow",
"cacodaemoniacal",
"centuries",
"chaotic",
"chthonian",
"chthonic",
"choking",
"cognizant",
"conspicuous",
"contemplative",
"contemporaneousness",
"correspondence",
"corroboration",
"crypt",
"cryptic",
"cthulhu",
"cthulhu fhtagn",
"cyclops",
"cyclopean",
"daemon",
"delirium",
"disappeared",
"disturbing",
"domdaniel",
"dread",
"dreams",
"dripping",
"eccentricity",
"eldritch",
"enigmatical",
"essential",
"evoke",
"excited",
"esquimaux",
"fancy",
"fantastically",
"fevered",
"fhtagn",
"forbidden",
"forefingers",
"formula",
"formulae",
"fugitive",
"fulgurous",
"gibberish",
"gibbous",
"glimpses",
"green",
"grimoire",
"hieroglyphics",
"hitherto",
"horror",
"hoarseness",
"howling",
"immeasurably",
"incantation",
"incessant",
"infinity",
"insane",
"intensity",
"inundation",
"jumble",
"keenly",
"kinship",
"kutulu",
"landscapes",
"latent",
"letters",
"lore",
"lucid",
"manuscript",
"mental",
"merciful",
"miscreants",
"miskatonic",
"monoliths",
"monotonously",
"nameless",
"necronomicon",
"new england",
"nocturnal",
"noisome",
"notes",
"nyarlothotep",
"ooze",
"outbuildings",
"panic",
"pertinent",
"ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn",
"physicians",
"pillars",
"poetic",
"polypheme",
"proportion",
"providence",
"psychically",
"purgation",
"quarters",
"r'lyeh",
"rambling",
"recollection",
"rejoinder",
"render",
"revelation",
"rhode island",
"rugose",
"ruthless",
"salt of the earth",
"screamings",
"sculptor",
"seizure",
"sensation",
"shambler",
"shoggoth",
"shrieking",
"sinister",
"sky-flung",
"sleeping",
"sphinx",
"squamous",
"stout",
"strange",
"subterrene",
"suspected",
"swineherd",
"syllabically",
"tale",
"terrifying",
"theosophists",
"things",
"titan",
"torchlight",
"transmute",
"typified",
"tyre",
"uninscribable",
"unnamable",
"unpronounceable",
"unspeakable",
"vague",
"venomous",
"verbal",
"verbatim",
"violently",
"visions",
"vistas",
"ye",
"yog-sothoth",
"abnormal",
"accursed",
"amorphous",
"antique",
"antiquarian",
"blasphemy",
"blasphemous",
"cat",
"charnel",
"comprehension",
"dank",
"decadent",
"daemoniac",
"effulgence",
"eldritch",
"fainted",
"fainting",
"foetid",
"fungus/fungoid/fungous",
"furtive",
"gambrel",
"gibbous",
"gibbered",
"gibbering",
"hideous",
"immemorial",
"indescribable",
"iridescence",
"loathing",
"loathsome",
"lurk",
"madness",
"manuscript",
"mortal",
"nameless",
"noisome",
"non-euclidean",
"proportion",
"disproportionate",
"shunned",
"singular",
"singularly",
"spectral",
"squamous",
"stench",
"stygian",
"swarthy",
"tenebrous",
"tentacle",
"tentacles",
"ululate",
"unmentionable",
"unnamable",
"unutterable",
"eldritch",
"azathoth",
"cthulhu",
"dagon",
"nodens",
"nyarlathotep",
"shoggoth",
"shub-niggurath",
"yog-sothoth",
"tomes",
"necronomicon",
"pnakotic",
"pnakotic manuscripts",
"de vermis mysteriis",
"book of eibon",
"eltdown shards",
"nameless cults",
"things",
"elder sign",
"locations",
"innsmouth",
"kadath",
"kingsport",
"leng",
"miskatonic",
"r'lyeh",
"yuggoth",
"irem"]

"""
validation below said nope. check and remove from lists above
"""
words_rejected = "nyarlathotep", "shub-niggurath", "huitloxopetl",
"wza-y'ei!", "y'kaa haa ho-ii", "hastur", "ithaqua", "ponape"

words = words_for_sure + words_probable + words_even_less_prob
# +  more_words
# + even_more

def reverse_matching(word):
    r = []
    for c in word:
        if c in inv_map:
            r.append(inv_map[c])
        else:
            print c,"not in map for word",word
            return ""
    return r

def is_prefix(p, ofwhat):
    if ofwhat[0:len(p)] == p: return True
    return False

def forward_matching_BROKEN(path):
    word = ""
    for s in path:
        cands = inp[s]
        for c in cands:
            possible_pref = word + c
            for w in words:
                if is_prefix(possible_pref, w):
                    part = w[0:len(possible_pref)]
                    tail = '(' + w[len(possible_pref):] + ')'
                    # print s,w
                    print s,part,tail,possible_pref

def forward_matching(path):
    return None

"""
things like [R+, R-] or [L, R] are forbidden for any tile
"""
def evaluate_meaning(path):
    rot_counter = 0
    mov_counter = 0
    for e in path:
        if e == 'R+' and rot_counter < 0: return False
        if e == 'R-' and rot_counter > 0: return False
        if e == 'R+': 
            rot_counter += 1 
            mov_counter = 0
        if e == 'R-': 
            rot_counter -= 1 
            mov_counter = 0
        if e == 'E' and mov_counter < 0: return False
        if e == 'W' and mov_counter > 0: return False
        if e == 'E': 
            mov_counter += 1 
            rot_counter = 0
        if e == 'W': 
            mov_counter -= 1 
            rot_counter = 0
        if e == 'SW' or e == 'SE': 
            mov_counter = 0 
            rot_counter = 0
    return True

def main():
    for w in words:
        print w
    print
    print "===================="
    print

    for w in words:
        m = reverse_matching(w)
        if not evaluate_meaning(m): 
            print "NOPE", w, m
            continue
        print "word", w
        print m
        

    print
    print "===================="
    print
    """
    suspects = [['SW', 'SE'], ['W', 'SE'], ['E', 'SW'], 
                ['W', 'SW'], ['E', 'SE'], 
                ['W', 'R+'], ['W', 'R-'], 
                ['E', 'R+'], ['E', 'R-'], 
                ['E', 'E'], ['W','W'],
                ['SW', 'R-', 'SE', 'E', 'E', 'SW']]
    for p in suspects:
        forward_matching(p)
        print "-------------"
    """
    print
    print "===================="
    print

    # print evaluate_meaning(['W', 'SE', 'SE', 'SW', 'W', 'E'])
    # should be false
    
if __name__ == "__main__":
    main()
