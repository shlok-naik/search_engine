import re
import difflib

FILLER = {"the", "is", "a", "an", "of", "to", "and", "in"}

def load_dictionary(path="words.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return set(word.strip().lower() for word in f)

DICTIONARY = load_dictionary()

def correct_word(word):
    if word in DICTIONARY:
        return word

    matches = difflib.get_close_matches(word, DICTIONARY, n=1, cutoff=0.8)
    return matches[0] if matches else word

def tokenize(text):
    words = re.findall(r"\b[a-z]+\b", text.lower())
    keywords = [w for w in words if w not in FILLER]
    return [correct_word(w) for w in keywords]

def get_query_keywords():
    query = input("Search: ")
    return tokenize(query)
