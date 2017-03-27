#!/usr/bin/env python

# Lachlan Dryburgh 188607
# 19/03/2017
# COMP90016 - Assignment 1

import sys
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)

data = []

for fn in xrange(1,len(sys.argv)):
  with open(sys.argv[fn]) as f:
    m = []
    next(f) #skip header line
    for line in f:
      m.append(float(line))
    data.append(m)

box = ax.boxplot(data)

plt.ylim(-0.1, 1.1)

plt.show()
