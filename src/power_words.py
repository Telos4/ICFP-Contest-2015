#!/usr/bin/python

inp = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'

inv_map = {e: k for k, v in inp.items() for e in v}

words_for_sure = ["ei!", "ia! ia!", "r'lyeh", "yuggoth"]

words_probable = ["cthulhu", "dagon", "nyarlathotep",
                  "shub-niggurath", "huitloxopetl", 
                  "wza-y'ei!", "y'kaa haa ho-ii", 
                  "rhan-tegoth-cthulhu fthagn-ei! ei! ei! ei!-rhan-teogth.",
                  "rhan-tegoth rhan-tegoth!",
                  "ph'nglui mglw'nafh cthulhu r'lyeh wgah'nagl fhtagn",
                  "H. P. Lovecraft"]

words_even_less_prob = ["derleth", "hastur", "ithaqua",
                        "zhar", "lloigor", "cyaegha", "nyogtha",
                        "tsathoggua", "aphoom-zhah", "cthugha",
                        "dagon","ghatanothoa",
                        "mother hydra","zoth-ommog", "gatanozoa",
                        "ghatanothoa", "arlyeh", "ponape"]

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

def forward_matching(path):
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
        
def main():
    for w in words:
        print "word", w
        print reverse_matching(w)

    print
    print "===================="
    print

    suspects = [['SW', 'SE'], ['W', 'SE'], ['E', 'SW'], 
                ['W', 'SW'], ['E', 'SE'], 
                ['W', 'R+'], ['W', 'R-'], 
                ['E', 'R+'], ['E', 'R-'], 
                ['E', 'E'], ['W','W'],
                ['SW', 'R-', 'SE', 'E', 'E', 'SW']]
    for p in suspects:
        forward_matching(p)
        print "-------------"

if __name__ == "__main__":
    main()
