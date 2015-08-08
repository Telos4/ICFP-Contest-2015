#!/usr/bin/python

from collections import defaultdict
from collections import OrderedDict

import pickle

# words = "apple banana apple strawberry banana lemon"

datf = open("others_combined.txt", 'r')
words = datf.read()
datf.close()

# meh
# words.decode('utf-8').lower()

d = defaultdict(int)
for word in words.split():
    for letter in word:
        d[letter] += 1

od = OrderedDict(sorted(d.items()))

print od

f = open("words.pickle", 'w')
pickle.dump(od, f)
f.close()



