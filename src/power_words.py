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
words_for_sure = ["ei!", "ia! ia!", "r'lyeh", "yuggoth"]

words_probable = ["cthulhu", "dagon", 
                  "rhan-tegoth-cthulhu fthagn-ei! ei! ei! ei!-rhan-teogth.",
                  "rhan-tegoth rhan-tegoth!",
                  "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn",
                  "h. p. lovecraft", "azathoth", "chaugnar faugn",
                  "shoggoths", "necronomicon"]

words_even_less_prob = ["derleth",
                        "zhar", "lloigor", "cyaegha", "nyogtha",
                        "tsathoggua", "aphoom-zhah", "cthugha",
                        "dagon","ghatanothoa",
                        "mother hydra","zoth-ommog", "gatanozoa",
                        "ghatanothoa", "arlyeh", "elder things",
                        "great race"]

"""
validation below said nope. check and remove from lists above
"""
words_rejected = "nyarlathotep", "shub-niggurath", "huitloxopetl",
"wza-y'ei!", "y'kaa haa ho-ii", "hastur", "ithaqua", "ponape"

words = words_for_sure + words_probable + words_even_less_prob

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
        m = reverse_matching(w)
        if not evaluate_meaning(m): 
            print "NOPE", w
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
