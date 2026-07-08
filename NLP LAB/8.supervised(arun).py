from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

sentences = [
    "He deposited money in the bank",
    "She withdrew cash from the bank",
    "The river overflowed the bank",
    "He sat on the river bank"
]

labels = ["finance", "finance", "river", "river"]

vectorizer = CountVectorizer()
model = MultinomialNB()

model.fit(vectorizer.fit_transform(sentences), labels)

test_sentence = "I went to the bank to get money"
prediction = model.predict(vectorizer.transform([test_sentence]))

print("Sentence:", test_sentence)
print("Predicted Sense:", prediction[0])
