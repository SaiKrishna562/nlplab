# basic verb list (main + helping verbs)
verbs = ["eat", "eats", "ate", "play", "plays", "played",
         "like", "likes", "liked", "see", "sees", "saw",
         "is", "are", "was", "were", "fly"]

def get_base(word):     # simple normalization
    if word.endswith("ing"):
        return word[:-3]
    if word.endswith("ed"):
        return word[:-2]
    return word

def predicate_argument(sentence):
    words = sentence.split()

    subject = ""
    predicate = ""
    obj = ""

    for i, word in enumerate(words):
        w = word.lower()

        # check verb (direct or base form)
        if w in verbs or get_base(w) in verbs:
            predicate = word

            # subject = before verb
            subject = " ".join(words[:i]) if i > 0 else "Unknown"

            # object = after verb (if exists)
            obj = " ".join(words[i+1:]) if i < len(words)-1 else "None"
            break

    print("Sentence:", sentence)
    print("Predicate:", predicate if predicate else "Not found")
    print("Agent (Subject):", subject if subject else "Not Found")

    print("Theme (Object):", obj if obj else "Not found")
    print()
# Examples
predicate_argument("Ram is eating an apple")
predicate_argument("The boy played football")
predicate_argument("She likes ice cream")
predicate_argument("Birds fly")
