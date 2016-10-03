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
		self.getallvertices(composers)
		self.isclique(self.edgelist)


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

	def getvertices(self, edgelist):
		v = []
		for edge in edgelist:
			v.append(edge[0])
			v.append(edge[1])
		return list(set(v))

	def getallvertices(self, composers):
		v = []
		for composer in composers:
			v.append(composer[-1])
		self.vertexlist = set(v)
		print(self.vertexlist)

	def getmaxclique(self):
		pass

	def getsubsets(self):
		pass

	def isclique(self, edgelist):
		#get list of vertices
		#check if each edge is present
		vlist = self.getvertices(edgelist)
		alledges = self.k_subsets(list(vlist), 2)
		alltuples = []
		for t in alledges:	
			alltuples.append(tuple(t))
		for t in alltuples:
			reverset = t[::-1]
			if(t not in edgelist and reverset not in edgelist): 
				return(False)
		return(True)
	
	def k_subsets(self, lst, k):
		if(len(lst)<k):
			return []
		if(len(lst) == k):
			return [lst]
		if(k==1):
			return [[i] for i in lst]
		return self.k_subsets(lst[1:], k) + [[lst[0]]+x for x in self.k_subsets(lst[1:], k-1)]
		#return self.k_subsets(lst[1:],k) + map(lambda x:x+[lst[0]],self.k_subsets(lst[1:], k-1))


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
