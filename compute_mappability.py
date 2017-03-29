#!/usr/bin/env python

# Lachlan Dryburgh 188607
# 19/03/2017
# COMP90016 - Assignment 1

# Compute the mappability of each base in a fasta file using a specified length k

from Bio import SeqIO
import sys

class mappability:
  def __init__(self, read, k):
    self.name = read.id
    self.seq = read.seq
    self.k = k
    self.dic = self.buildDict()

  def buildDict(self):
    kmers = {}
    # could just increment a counter but storing positions could be useful
    for i in range(len(self.seq)-self.k +1):
      kmer = self.seq[i:i+self.k]

      # Store each kmer once, if a reverse complement has already been recorded it will be stored under that kmer
      # Storing once means no special cases for palindromes etc.
      if kmer in kmers:
        kmers[kmer].append(i)
      elif kmer.reverse_complement() in kmers:
        kmers[kmer.reverse_complement()].append(i)
      else:
        kmers[kmer] = [i]

    return kmers

  def calc_mappability(self):
    maps = [0.0]*(len(self.seq)-self.k+1)
    for i in range(len(self.seq)-self.k+1):

      # The position will appear as either itself or its reverse complement
      if self.seq[i:i+self.k] in self.dic:
        n = len(self.dic[self.seq[i:i+self.k]])
      elif self.seq[i:i+self.k].reverse_complement() in self.dic:
        n = len(self.dic[self.seq[i:i+self.k].reverse_complement()])
      else:
      # Should be impossible to not find either
        print("error at position " + str(i))
      maps[i] = 1.0/n
    return maps 


if (len(sys.argv) < 3):
  print("Usage: <read file (fasta)> <k length (int)> ")
  sys.exit(0)

try:
  for read in SeqIO.parse(sys.argv[1], "fasta"):
    mapper = mappability(read, int(sys.argv[2]))
    maps = mapper.calc_mappability()

    # Stop after first read in fasta file
    break
except IOError as e:
  print(e)
  sys.exit(1)

f = open("map$" + sys.argv[2] + ".wig", 'w')

f.write("fixedStep  chrom=" + mapper.name + " start=1\n")
for m in maps:
  f.write("{0:.2f}".format(m) + "\n")
