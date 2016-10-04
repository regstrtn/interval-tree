from __future__ import print_function
import itree
import os 
import sys
import pprint
import pgraph
import csv
from igraph import igraph


fbcsv = open("b.csv", "r")
fbcsv.readline()

#Read csv file after ignoring the first line
composers = csv.reader(fbcsv, delimiter = ",", quotechar = '"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
data = []

for row in composers:
	life = []
	#print(row[2].split("-")[1])
	life.append(int(row[2].split("-")[0]))
	life.append(int(row[2].split("-")[1]))
	life.append(row[1])
	data.append(life)

print(data)

#Construct tree
a = data
mytree = itree.itree(a)
mytree.traverse()

#Print composer Overlap
overlaps = mytree.findrange(1895, 1957)
print(overlaps)

#Print Songs
fbcsv.seek(0); fbcsv.readline()
mytree.findsongs(1895, 1957,composers)

#Output tree dot file
pgraph.printtree(mytree)

#Test igraph module
g = igraph(mytree, a)
g.printdotfile()


'''
myTree = ngit.intervalTree(a, 0, 1, 1679, 1998)
myTree.pprint(6)
r = [1800, 1900]
print(myTree.findRange(r))
'''
