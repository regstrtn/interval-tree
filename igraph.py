from __future__ import print_function
import os
import sys
from pprint import pprint
from itree import itree
from collections import defaultdict


class igraph:
	def __init__(self, mytree, composers):
		self.edgelist = []
		self.vertexlist = set()
		self._graph = defaultdict(set)
		self.buildedgelist(mytree, composers)


	def getoverlappingcomposers(self, mytree, composer):
		overlaps = mytree.findrange(composer[0], composer[1])
		return overlaps

	def buildedgelist(self, mytree, composers):
		self.edgelist = []
		for composer in composers:
			overlaps = self.getoverlappingcomposers(mytree, composer)
			for item in overlaps:
				edgetuple = (composer[-1], item)
				b = edgetuple[::-1]
				if (b not in self.edgelist and b[0]!=b[1]):
					self.edgelist.append(edgetuple)
		pprint(self.edgelist)

	def printdotfile(self):
		'''
		Run this to make graph: dot -Tps myg.dot -o graph1.ps
		'''	
		f = open("myg.dot", "w")
		f.write("graph G {")
		for edge in self.edgelist:
			linestr = edge[0]+"--"+edge[1]+"\n"
			f.write(linestr)
		f.write("}")

