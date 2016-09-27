import graphvizparent

dot = graphvizparent.Digraph(comment='The Round Table')
dot
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edges(['BL'])
dot.format = 'png'

dot.render('round-table.gv', view=True)
