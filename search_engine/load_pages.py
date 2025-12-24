import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "documents")

FILLER = {"the", "is", "a", "an", "of", "to", "and", "in"}

def tokenize(text):
    words = re.findall(r"\b[a-z]+\b", text.lower())
    return [w for w in words if w not in FILLER]

def load_pages(folder=DOCS_DIR):
    pages = {}

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                pages[filename] = tokenize(f.read())

    return pages


