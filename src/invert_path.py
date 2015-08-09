#!/usr/bin/python
"""
it is not possible to fully invert a path, because of each cell at
most once requirement. but we can build some kind of a
"pseudo-inverse": an attempt to undo path's actions as much as
possible.

There is a "left pseudo-inverse" and "right" one. "Left" means that we
spool the undo information and then perform the actual path, the
"right" one means that we have executed the path already and are
trying to mitigate the result.

We need to verify in each step that our inverse path does nothing
wrong. Ideally: couple this with piece and map and position
knowdlege. However, for now we try to find "universal" inverses.
"""

# import power_words
# can use evaluate_meaning() to validate
# fuck you
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

"""
# both versions of conversion tables
inp = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'SW': ['a', 'g', 'h', 'i', 'j', '4'],
        'SE': ['l', 'm', 'n', 'o', ' ', '5'],
        'R-': ['d', 'q', 'r', 'v', 'z', '1'],
        'R+': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'

inp2 = { 'W' : ['p', '\'',  '!', '.', '0', '3'],
        'E' : ['b', 'c', 'e', 'f', 'y', '2'],
        'T': ['a', 'g', 'h', 'i', 'j', '4'],
        'Q': ['l', 'm', 'n', 'o', ' ', '5'],
        'Y': ['d', 'q', 'r', 'v', 'z', '1'],
        'X': ['k', 's', 't', 'u', 'w', 'x'],
        ' ' : ['\t', '\n', '\r', '-']} # let's also ignore '-'
"""

# ' '  is a noop
# make a universal version that accepts both encodings, may however
# still need a conversion from `inp` to `inp2` in some parts
m = { 'W' : ['E', 'SE', ' '],
      'E' : ['W', 'SW', ' '],
      'SW': [' ', 'E'],
      'SE': [' ', 'W'],
      'R-': ['R+', ' ', 'SE', 'SW'],
      'R+': ['R-', ' ', 'SW', 'SE'],
      # the other version
      'T':  [' ', 'E'],
      'Q':  [' ', 'W'],
      'Y':  ['X', ' ', 'Q', 'T'],
      'X':  ['Y', ' ', 'T', 'Q'],
      ' ' : [] }


def inverseLeft(path):
    res = []
    for (i, step) in enumerate(path):
        off = 0
        found = False
        while off < len(m[step]):
            candidate = m[step][off]
            newres = list(res)
            newres.append(candidate)
            # print "trying", res, "+", candidate, "@", m[step]
            if(evaluate_meaning(newres)):
                res = newres
                # print "found", res
                found = True
                break
            else:
                off += 1
        if not found:
            # still have not found a suitable movement
            print "failed to find a suitable left inverse for", path
            print "inverted merely",i,"tokens:", res, "for", path[0:i]
            return None
    print res, "seems to be a left-inverse of", path

    # need to check that `left-inverse + original path` are still a
    # valid path
    if not reduce(lambda x, y: x and y, map(evaluate_meaning, res + path)):
        print "but the concatenation of them is still not valid!"
        return None

    return res

# very similar to above
def inverseRight(path):
    res = []
    for (i, step) in enumerate(reversed(path)):
        off = 0
        found = False
        while off < len(m[step]):
            candidate = m[step][off]
            newres = list(res)
            newres.append(candidate)
            # print "trying", res, "+", candidate, "@", m[step]
            if(evaluate_meaning(newres)):
                res = newres
                # print "found", res
                found = True
                break
            else:
                off += 1
        if not found:
            # still have not found a suitable movement
            print "failed to find a suitable right inverse for", path
            print "inverted merely",i,"tokens:", res, "for", path[0:i]
            return None
    print res, "seems to be a right-inverse of", path

    # need to check that `right-inverse + original path` are still a
    # valid path
    if not reduce(lambda x, y: x and y, map(evaluate_meaning, path + res)):
        print "but the concatenation of them is still not valid!"
        return None

    return res


def test():
    l = inverseLeft(['E', 'SW', 'W', 'SW', 'SW',
    'W', 'SE', 'SW', 'SW', 'W', 'SE', 'E', 'E', 'R-', 'SE', 'SE',
    'SE', 'SE', 'SW', 'E', 'SE', 'SE', 'E', 'R+', 'SW', 'SW', 'SE',
    'R+', 'SW', 'SW', 'SE', 'R+', 'R+', 'E'])

    r = inverseRight(['E', 'SW', 'W', 'SW', 'SW',
    'W', 'SE', 'SW', 'SW', 'W', 'SE', 'E', 'E', 'R-', 'SE', 'SE',
    'SE', 'SE', 'SW', 'E', 'SE', 'SE', 'E', 'R+', 'SW', 'SW', 'SE',
    'R+', 'SW', 'SW', 'SE', 'R+', 'R+', 'E'])

    if l == r:
        print "left-inverse is the same as right-inverse"
    if l == reversed(r):
        print "left-inverse is the same as reversed right-inverse"


if __name__ == "__main__":
    test()


                
