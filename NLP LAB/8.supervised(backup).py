from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

labels, sentences = [], []

with open("bank_dataset.txt", "r") as f:
    for line in f:
        label, sentence = line.strip().split("\t")
        labels.append(label)
        sentences.append(sentence)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = MultinomialNB()
model.fit(X, labels)

tests = [
    "I deposited cash in the bank.",
    "The fisherman sat on the bank.",
    "The bank approved the loan.",
    "Children played near the river bank."
]

pred = model.predict(vectorizer.transform(tests))

for s, p in zip(tests, pred):
    print(f"{s} --> {p}")