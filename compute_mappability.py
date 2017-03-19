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

    for i in range(len(self.seq)-self.k +1):
      kmer = self.seq[i:i+self.k]
      if kmer in kmers:
        kmers[kmer].append(i)
      elif kmer.reverse_complement() in kmers:
        kmers[kmer.reverse_complement()].append(i)
      else:
        kmers[kmer] = [i]

    return kmers

  def calc_mappability(self):
    for i in range(len(self.seq)-self.k+1):
      if self.seq[i:i+self.k] in self.dic:
        n = len(self.dic[self.seq[i:i+self.k]])
      elif self.seq[i:i+self.k].reverse_complement() in self.dic:
        n = len(self.dic[self.seq[i:i+self.k].reverse_complement()])
      else:
        print("error at position " + str(i))
      print(str(1.0/n))


if (len(sys.argv) < 3):
  print("Usage: <read file (fasta)> <k length (int)> ")
  sys.exit(0)

try:
  for read in SeqIO.parse(sys.argv[1], "fasta"):
    mapper = mappability(read, int(sys.argv[2]))
    mapper.calc_mappability()
    break
except IOError as e:
  print(e)
  sys.exit(1)
