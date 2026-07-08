import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a sentence: ")
doc = nlp(text)

subject = predicate = obj = "Not Found"

for token in doc:
    if token.dep_ == "nsubj":
        subject = token.text
    elif token.dep_ == "ROOT":
        predicate = token.text
    elif token.dep_ in ["dobj", "obj"]:
        obj = token.text

print("Subject  :", subject)
print("Predicate:", predicate)
print("Object   :", obj)