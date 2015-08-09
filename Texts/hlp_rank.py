#!/usr/bin/python

from collections import defaultdict
from collections import OrderedDict

import pickle

# words = "apple banana apple strawberry banana lemon"

datf = open("filtered_hpl.txt", 'r')
words = datf.read()
datf.close()

# meh
# words.decode('utf-8').lower()

d = defaultdict(int)
for word in words.split():
        d[word] += 1

od = OrderedDict(sorted(d.items()))
# print od

## sort by ranking
sd = sorted(d, key=d.get)

ld = list(sd)
# there comes some wikimedia jibbrish first?
# print ld[0:1000]
for i in range(0,1000):
    print ld[i]

## still save all
f = open("words.pickle", 'w')
pickle.dump(od, f)
f.close()



