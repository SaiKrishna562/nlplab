from nltk import CFG
from nltk.parse import ChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> N
VP -> V NP
N -> 'Ramya' | 'apple'
V -> 'eats'
""")
parser = ChartParser(grammar)
sentence = "Ramya eats apple".split()
for tree in parser.parse(sentence):
 print(tree)
 tree.pretty_print() 
