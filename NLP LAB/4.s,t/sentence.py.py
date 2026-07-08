import nltk
from nltk.tokenize import sent_tokenize
# Download tokenizer (only needed once)
nltk.download('punkt')
nltk.download('punkt_tab')
text = """
Artificial intelligence (AI) has become one of the most transformative technologies of the twenty-first
century, influencing nearly every aspect of modern life, from healthcare and education to
transportation, finance, and entertainment. By analyzing vast amounts of data at remarkable speeds,
AI systems can identify patterns, make predictions, automate repetitive tasks, and assist humans in
solving complex problems that would otherwise require significant time and effort. In healthcare,
AI-powered tools help doctors diagnose diseases more accurately, recommend personalized
treatment plans, and monitor patients remotely, improving both efficiency and patient outcomes."
"""
sentences = sent_tokenize(text)
for i, sentence in enumerate(sentences, 1):
 print(f"{i}. {sentence}") 