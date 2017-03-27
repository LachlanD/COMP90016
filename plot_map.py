#!/usr/bin/env python

# Lachlan Dryburgh 188607
# 19/03/2017
# COMP90016 - Assignment 1


# plot boxplots of the mappability distrbution of an arbitrary number of wig files specified on the command line 
import sys
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)

data = []
labels = []

for fn in xrange(1,len(sys.argv)):
  with open(sys.argv[fn]) as f:
    m = []
    labels.append(sys.argv[fn])
    next(f) #skip header line
    for line in f:
      try:
        m.append(float(line))
      except ValueError:
        print("unexpected value") 
    data.append(m)

box = ax.boxplot(data)

plt.ylim(-0.1, 1.1)

plt.title("Mabbaility Distributions")
plt.ylabel("mappability")
plt.xlabel("k length")

ax.set_xticklabels(labels)


plt.show()
