#!/usr/bin/python

from collections import defaultdict
from collections import OrderedDict

import pickle

# https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
from itertools import izip

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)
"""
# usage:
for x, y in pairwise(l):
   print "%d + %d = %d" % (x, y, x + y)
"""

# https://stackoverflow.com/questions/18809482/python-nesting-dictionary-ordereddict-from-collections
class OrderedDefaultDict(OrderedDict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super(OrderedDefaultDict, self).__init__(*args, **kwargs)
        self.default_factory = default_factory
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        val = self[key] = self.default_factory()
        return val

f = open("words.pickle", 'r')
othersd = pickle.load(f)
f.close()


datf = open("all_hpl.txt", 'r')
words = datf.read()
datf.close()

print "files read"

# meh
# words.decode('utf-8').lower()

ld = OrderedDefaultDict(OrderedDict)
for word in words.split():
    d = defaultdict(int)
    for letter in word:
        d[letter] += 1
    od = OrderedDict(sorted(d.items()))
    # print od
    ld[word] = od

print "categorized all H.P.L. words"

## have ordered dicts of each word in H.P.L.'s texts
## need to compare to baseline (othersd)

tol = 5000
ct = 0
maxt = -9999
mint = 9999

for word in ld:
    print word
    testd = defaultdict(int)
    for letter in ld[word]:
        # compare the number of letters 'letter' in a current 
        # H.P.L word 'word' with number of these letters in english
        # 'words[letter]'. need to look for inconsistencies in
        # fractions
        try:
            q = words[letter] / ld[word][letter] * 100
        except:
            continue
        testd[letter] = int(q)

    for l1, l2 in pairwise(testd):
        ct = abs(testd[l1] - testd[l2])
        """
        if ct > maxt: maxt = ct
        if ct < mint: mint = ct
        """
        if ct > tol:
            print "YAY", word, ct
            break

# print "largest tollerance is", maxt, "smallest is", mint
