#!/usr/bin/python

import cv2
import numpy as np
import sys

if len(sys.argv) < 2: sys.exit()

a = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR)

# split the channels
a1,a2,a3 = cv2.split(a)

a_ = a3-a2

h1 = np.bincount(a_.ravel(),minlength=256)

v = h1[0]

if   v == 43478: print "."
elif v == 42638: print " longdash "
elif v == 43058: print " shortdash "
else: print " "

