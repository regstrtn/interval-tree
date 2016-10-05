import os
import sys

'''
Run this to make graph: dot -Tps g.dot -o graph1.ps
'''

def printtree(mytree):
	lines = []
	f = open("mytree.dot", "w")
	f.write("digraph G {")
	printlines(f, mytree.root)
	f.write("}")


def printlines(f, root):
	lines = []
	if(root is None): return
	if(root.l is not None):
		linestr = ""; 
		linestr += str(root.val)
		linestr += "->"
		linestr += str(root.l.val)
		linestr = linestr+';\n'
		linestr += str(root.val)+'[label="'+str(root.val)+" "+" ".join(root.data)+'"];\n'
		linestr += str(root.l.val)+'[label="'+str(root.l.val)+" "+" ".join(root.l.data)+'"];\n'

		f.write(linestr)
	if(root.r is not None):
		linestr = ""; 
		linestr += str(root.val)
		linestr += "->"
		linestr += str(root.r.val)
		linestr = linestr+';\n'
		linestr += str(root.val)+'[label="'+str(root.val)+" "+" ".join(root.data)+'"];\n'
		linestr += str(root.r.val)+'[label="'+str(root.r.val)+" "+" ".join(root.r.data)+'"];\n'
		f.write(linestr)
	printlines(f, root.l)
	printlines(f, root.r)

