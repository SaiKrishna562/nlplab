from nltk.tokenize import TextTilingTokenizer
import nltk
nltk.download('stopwords')
with open("input.txt", "r", encoding="utf-8") as f:
 text = f.read()
topics = text.split("\n\n")
for i, topic in enumerate(topics, 1):
 print(f"\nTopic {i}:\n{topic}")