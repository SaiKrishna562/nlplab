import nltk

# Download the POS tagger (run only once)
nltk.download('averaged_perceptron_tagger_eng')

# Read stemmed output file
with open("stemming_output.txt", "r") as file:
    words = file.read().split()

# Remove heading if present
if words[:3] == ["After", "Porter", "Stemming:"]:
    words = words[3:]

# Perform POS tagging
tagged_words = nltk.pos_tag(words)

# Write the output to a file
with open("pos_output.txt", "w") as file:
    file.write("Word\tPOS Tag\n")
    file.write("-------------------------\n")
    for word, tag in tagged_words:
        file.write(f"{word}\t{tag}\n")

print("POS Tagging completed successfully.")
print("Output saved in 'pos_output.txt'")
