#!/usr/bin/env python

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

    for i in xrange(len(self.seq)-self.k +1):
      kmer = self.seq[i:i+self.k]
      if kmer in kmers:
        kmers[kmer].append(i)
      else if kmer.reverse_complement() in kmers
        kmers[kmer.reverse_complement().append(i)
      else
        kmers[kmer] = [i]

    return kmers


if len(sys.argv) < 3):
  print("Usage: <read file (fasta)> <k length (int)> ")
  sys.exit(0)

try:
  for read in SeqIO.parse(sys.argv[1], "fasta"):
    mapper = mappability(read, int(sys.arv[2]))
