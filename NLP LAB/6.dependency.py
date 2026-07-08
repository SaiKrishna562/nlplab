from nltk.grammar import DependencyGrammar
from nltk.parse import ProjectiveDependencyParser
grammar = DependencyGrammar.fromstring("""
'chased' -> 'dog'
'chased' -> 'cat'
'dog' -> 'the'
'cat' -> 'a'
""")
parser = ProjectiveDependencyParser(grammar)
sentence = "the dog chased a cat".split()
for tree in parser.parse(sentence):
 print(tree)
 tree.pretty_print()