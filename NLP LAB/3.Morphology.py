class DictionaryMorphologicalAnalyzer:
    def __init__(self):
        self.lexicon = {
            "playing": {"root": "play", "type": "Verb", "tense": "Present Continuous"},
            "played": {"root": "play", "type": "Verb", "tense": "Past"},
            "cats": {"root": "cat", "type": "Noun", "number": "Plural"},
            "went": {"root": "go", "type": "Verb", "tense": "Past (Irregular)"},
            "running": {"root": "run", "type": "Verb", "tense": "Present Continuous"}
        }

    def analyze(self, word):
        result = self.lexicon.get(word.lower())
        if result:
            return {"Word": word, "Root": result["root"], "Details": result}
        return {"Word": word, "Root": "Unknown",
                "Details": "Word not found in dictionary"}

analyzer = DictionaryMorphologicalAnalyzer()

for word in ["playing", "cats", "went", "run"]:
    print(analyzer.analyze(word))