#!/usr/bin/python
# uses n-grams to inject words of power into the existing sequence
# makes use of `ngram` package, do `pip install ngram` beforehand
import ngram

import sys

# adapts some code from `power_words.py`: we need single commands to
# be single characters, this makes this much easier
# see also `convert...py`

"""
inp = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'
"""

inp =  { 'W' : ['p', '\'',  '!', '.', '0', '3'],
         'E' : ['b', 'c', 'e', 'f', 'y', '2'],
         'T': ['a', 'g', 'h', 'i', 'j', '4'],    # SW is T
         'Q': ['l', 'm', 'n', 'o', ' ', '5'],    # SE is Q
         'Y': ['d', 'q', 'r', 'v', 'z', '1'],    # R- is Y
         'X': ['k', 's', 't', 'u', 'w', 'x'],    # R+ is X
         ' ' : ['\t', '\n', '\r']}

inv_map = {e: k for k, v in inp.items() for e in v}



def reverse_matching(word):
    r = []
    for c in word:
        if c in inv_map:
            r.append(inv_map[c])
        else:
            print c,"not in map for word",word
            return ""
    return r

def evaluate_meaning(path):
    rot_counter = 0
    mov_counter = 0
    for e in path:
        if e == 'X' and rot_counter < 0: return False
        if e == 'Y' and rot_counter > 0: return False
        if e == 'X': 
            rot_counter += 1 
            mov_counter = 0
        if e == 'Y': 
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
        if e == 'T' or e == 'Q': 
            mov_counter = 0 
            rot_counter = 0
    return True

def path_from_word(w):
    m = reverse_matching(w)
    if not evaluate_meaning(m): 
        print "NOPE", w, m
        return None
    _m = "".join(map(str, m))
    # print "word", w, _m
    return m

"""
def flatten_words(words):
    words = [item if isinstance(item, str) else "".join(item) for item in words ]
"""
    
# convert power words from input to ngrams
def remember_power_words(words):
    words = map(lambda word: "".join(map(str, word)), words)
    print "remembering", words
    return ngram.NGram(words)

# https://stackoverflow.com/questions/9114402/regexp-finding-longest-common-prefix-of-two-strings
def common_prefix(a,b):
  i = 0
  for i, (x, y) in enumerate(zip(a,b)):
    if x!=y: break
  return a[:i]

"""
for each, say, 3 characters in the path search for a fitting word of
power that begins with these characters. then we inject the fitting
word of power into the path
"""
def search_prefix(ngrams, path):
    wops = []
    nums = map(lambda (x,y): x, enumerate(path))
    for (k, a,b,c) in zip(nums, path, path[1:], path[2:]):
        # print k,a,b,c
        if ngrams == None:
            print "no ngrams, oh my!"
            continue # for testing

        possible = "".join([str(a),str(b),str(c)])
        # if possible == None: continue
        # print "searching for", possible

        candidate = ngrams.find(possible)
        if candidate == None: continue
        pre = common_prefix("".join(map(str, path[k:])), candidate)
        if len(pre) < 1: continue
        print "candidate:", candidate, "at offset", k, "common prefix there:", pre
        # "--> (",path[max(0,k-2):k], ")", path[k], "(", path[min(len(path),k+1):min(len(path),k+3)], ")"
        wops.append((candidate,k,pre))
        
    if len(wops) < 1:
        print "nothing found"
        return None

    """
    # pick the largest w.o.p.
    theword = None
    ranked = map(lambda (x,k): [x,len(x),k], wops)
    theword, l, offset = max(ranked, key=operator.itemgetter(1))

    return theword, offset, path[0:offset], path[offset+1:]
    """

    # return all candidates? 
    # return first, adapt path (not here), repeat?
    
    return wops

def test():
    # search_prefix(None, "asdfghjmk,.")
    return None

def convert_from_elaborate(movement_sequence):
    movement_sequence = [ x if x != 'SE' else 'Q' for x in movement_sequence]
    movement_sequence = [ x if x != 'SW' else 'T' for x in movement_sequence]
    movement_sequence = [ x if x != 'R+' else 'X' for x in movement_sequence]
    movement_sequence = [ x if x != 'R-' else 'Y' for x in movement_sequence]
    movement_sequence = "".join(movement_sequence)
    return movement_sequence

def main():
    if len(sys.argv) < 2:
        path = convert_from_elaborate(['E', 'SW', 'W', 'SW', 'SW',
    'W', 'SE', 'SW', 'SW', 'W', 'SE', 'E', 'E', 'R-', 'SE', 'SE',
    'SE', 'SE', 'SW', 'E', 'SE', 'SE', 'E', 'R+', 'SW', 'SW', 'SE',
    'R+', 'SW', 'SW', 'SE', 'R+', 'R+', 'E'])
    else:
        path = sys.argv[1]
    if len(sys.argv) < 3:
        words_for_sure = ["ei!", "ia! ia!", "r'lyeh", "yuggoth",
                          "necronomicon", "house", "dead", "cthulhu r'lyeh",
                          "wgah'nagl fhtagn"]
    else:
        words_for_sure = sys.argv[2]

    _p = "".join(map(str, path))
    print "path we are searching for is", _p

    # TODO: save the ngram and don't generate it over and over again
    print "generating words..."
    converted_words = map(path_from_word, words_for_sure)
    ng = remember_power_words(converted_words)

    print "searching..."
    """
    res = search_prefix(ng, path)
    if not res == None:
        word, path, offset, _ = res
    else:
        return

    if not word == None:
        print "found word of power:", word, "the prefix is", path,
        "at offset", offset
    """
    wops = search_prefix(ng, path)

    """
    if wops == None: return

    largest, off = max(wops, key=lambda (x,y,z): len(x) + len(z))
    print "largest word with largest prefix is", largest, "at offset", off
    """

if __name__ == "__main__":
    main()

