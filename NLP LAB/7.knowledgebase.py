# meanings (dictionary)
senses = {
 "bank": [
 "place where money is deposited",
 "side of a river"
 ]
}
def knowledge_wsd(sentence, word):
 words = sentence.lower().split()
 meanings = senses[word]
 best_meaning = None
 max_overlap = 0
 for meaning in meanings:
 meaning_words = meaning.lower().split()
 # Count common words
 overlap = len(set(words) & set(meaning_words))
 if overlap > max_overlap:
 max_overlap = overlap
 best_meaning = meaning
 return best_meaning
# Example
sentence = "I went to bank to get money"
print("Meaning:", knowledge_wsd(sentence, "bank"))