verbs = ["eat","eats","ate","play","plays","played","like","likes","liked","see","sees","saw","is","are","was","were","fly"]

def pa(s):
    w = s.split()
    for i,x in enumerate(w):
        if x.lower().rstrip("ing").rstrip("ed") in verbs or x.lower() in verbs:
            print("Sentence:", s)
            print("Predicate:", x)
            print("Agent:", " ".join(w[:i]) or "Unknown")
            print("Theme:", " ".join(w[i+1:]) or "None", "\n")
            return

pa("Ram is eating an apple")
pa("The boy played football")
pa("She likes ice cream")
pa("Birds fly")