import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK resources (only needed the first time)
nltk.download('punkt')
nltk.download('stopwords')

# Read input file
with open("input.txt", "r") as file:
    text = file.read().lower()

# ---------------- Tokenization ----------------
tokens = word_tokenize(text)

with open("tokenization_output.txt", "w") as file:
    file.write("Tokens:\n")
    for token in tokens:
        file.write(token + "\n")

# ---------------- Stop Word Removal ----------------
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

with open("stopword_output.txt", "w") as file:
    file.write("After Stop Word Removal:\n")
    for word in filtered_tokens:
        file.write(word + "\n")

# ---------------- Stemming ----------------
ps = PorterStemmer()
stemmed_tokens = [ps.stem(word) for word in filtered_tokens]

with open("stemming_output.txt", "w") as file:
    file.write("After Stemming:\n")
    for word in stemmed_tokens:
        file.write(word + "\n")

print("Processing completed successfully.")
print("Generated files:")
print("1. tokenization_output.txt")
print("2. stopword_output.txt")
print("3. stemming_output.txt")
