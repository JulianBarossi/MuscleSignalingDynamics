# Muscle Signaling Flow Chart
# Julian Barossi
# 02/09/24

from graphviz import Digraph

dot = Digraph(comment = 'Neuron Signaling to Muscle Movement')

# Nodes
dot.node('1', 'Action Potential Initiation')
dot.node('2', 'Depolarization')
dot.node('3', 'Propagation')
dot.node('4', 'Neurotransmitter Release')
dot.node('5', 'Muscle Fiber Activation')
dot.node('6', 'Muscle Contraction')

# Connect Nodes
dot.edges(['12', '23', '34', '45', '56'])

# Render Graph
dot.render('muscle_signaling_flowchart', view=True)