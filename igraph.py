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
				self.edgelist.append(edgetuple)
		pprint(self.edgelist)
