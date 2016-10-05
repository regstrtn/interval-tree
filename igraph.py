from __future__ import print_function
import os
import sys
from pprint import pprint
from itree import itree
from collections import defaultdict

#Turn this flag 1 to print debugging information
debug = 0
def dg(param):
	if(debug ==1):
		pprint(param)

class igraph:
	def __init__(self, mytree, composers):
		self.edgelist = []
		self.vertexlist = set()
		self._graph = defaultdict(set)
		self.getallvertices(composers)
		self.buildedgelist(mytree, composers)
		#pprint(self._graph)
		#self.getmaxclique()
		#self.getlcc()

	def getoverlappingcomposers(self, mytree, composer):
		#Return all composers overlapping with given composer
		overlaps = mytree.findrange(composer[0], composer[1])
		dg([composer[0], composer[1], overlaps])
		return overlaps

	def buildedgelist(self, mytree, composers):
		#Get all edges for the interval graph
		self.edgelist = []
		for composer in composers:
			overlaps = self.getoverlappingcomposers(mytree, composer)
			for item in overlaps:
				edgetuple = (composer[-1], item)
				b = edgetuple[::-1]
				if(b[0]!=b[1]):
					self._graph[composer[-1]].add(edgetuple)
					self._graph[item].add(b)
				if (b not in self.edgelist and b[0]!=b[1]):
					self.edgelist.append(edgetuple)
		
	def getvertices(self, edgelist):
		#Get vertices from edgelist
		v = []
		for edge in edgelist:
			v.append(edge[0])
			v.append(edge[1])
		return list(set(v))

	def getallvertices(self, composers):
		#Return all vertices in the graph
		v = []
		for composer in composers:
			v.append(composer[-1])
		setv = set(v)
		for vertex in setv:
			self._graph[vertex] = set()
		self.vertexlist = setv

	def getmaxclique(self):
		#Find largest clique in the graph
		size = len(self._graph.keys())
		alist = [' C1', ' C2']
		for i in range(size+1, 1, -1):
			keysubset = self.k_subsets(self._graph.keys(), i)
			for klist in keysubset:
				subgraph = {}
				for k in klist:
					subgraph[k] = self._graph[k]
				if(self.isclique(subgraph)):
					print("Largest clique size: ",len(subgraph.keys()))
					print("Elements in the clique: ",subgraph.keys())
					return
			#subgraph = {k: self._graph[k] for k in alist} 
		pass

	def getsubsets(self):
		
		pass

	def isclique(self, subgraph):
		#get a subgraph
		#check if all possible edges are present. If yes, subgraph is a clique 
		vlist = subgraph.keys()
		alledges = self.k_subsets(list(vlist), 2)
		alltuples = []
		for t in alledges:	
			alltuples.append(tuple(t))
		for t in alltuples:
			reverset = t[::-1]
			if(t not in subgraph[t[0]] and reverset not in subgraph[t[1]]): 
				return(False)
		return(True)
	
	def k_subsets(self, lst, k):
		#Recursively enumerate all k-size subsets of a given set 
		if(len(lst)<k):
			return []
		if(len(lst) == k):
			return [lst]
		if(k==1):
			return [[i] for i in lst]
		return self.k_subsets(lst[1:], k) + [[lst[0]]+x for x in self.k_subsets(lst[1:], k-1)]
		#return self.k_subsets(lst[1:],k) + map(lambda x:x+[lst[0]],self.k_subsets(lst[1:], k-1))

	def getlcc(self):
		#Print largest connected component in a graph. Uses self.dfs
		sizecc = 0
		cc = []
		v = set(self.vertexlist)
		while v:
			path = self.dfs(v.pop())
			cc.append(path)
			for p in path:				
				v.discard(p)
		sizecc = [len(x) for x in cc]
		maxsize = max(sizecc)
		#print(self.vertexlist)
		for c in cc:
			if(len(c) == maxsize):
				print("Largest connected component: ",c)

	def dfs(self, start, path = []):
		#Iterative implementation of DFS
		q = [start]
		while q:
			v = q.pop(0)
			if v not in path:
				path = path+[v]
				q = [x[1] for x in self._graph[v]]+q
		return path

	
	def printdotfile(self):
		'''
		Print the dot file for graphviz
		Run this to make graph: dot -Tps myg.dot -o graph1.ps
		'''	
		f = open("myg.dot", "w")
		f.write("graph G {")
		for s in self._graph:
			if(len(self._graph[s])==0):
					linestr = s
					f.write(linestr+";\n")

		for edge in self.edgelist:
			linestr = edge[0]+"--"+edge[1]+";\n"
			f.write(linestr)
		f.write("}")
