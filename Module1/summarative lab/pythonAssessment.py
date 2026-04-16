# MARTIN LENGA MWAPAHE

import re # For pattern matching (words, sentences)
import os


# READ FILE
# Reads the news article from a file
def read_article(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""   # ❗ no print (AutoTest safe)


# COUNT SPECIFIC WORD
# Counts how many times a word appears in the text
def count_specific_word(text, word):
    text = text.lower()
    word = word.lower()

    words = re.findall(r'\b\w+\b', text)

    count = 0
    for w in words:  # Loop through words
        if w == word:  # Check match
            count += 1
    return count


# MOST COMMON WORD
# Finds the most frequent word using a dictionary
def identify_most_common_word(text):
    if not text.strip():
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    word_count = {}  # Dictionary to store frequencies

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return max(word_count, key=word_count.get)


# AVERAGE WORD LENGTH
# Calculates average length of words (ignores punctuation)
def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)

    total_length = 0
    count = 0

    i = 0
    while i < len(words):
        total_length += len(words[i])
        count += 1
        i += 1

    if count == 0:
        return 0

    return total_length / count


# COUNT PARAGRAPHS
# Counts paragraphs based on empty lines
def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = text.split("\n\n")
    return len([p for p in paragraphs if p.strip() != ""])


# COUNT SENTENCES
# Counts sentences using punctuation (. ! ?)
def count_sentences(text):
    if not text.strip():
        return 1

    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip() != ""])


# MAIN PROGRAM
def main():

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "news_article.txt")

    text = read_article(file_path)

    if text == "":
        print("File not found or empty.")
        return
    else:
        print("File loaded successfully.")

    print("\n===== TEXT ANALYSIS =====\n")

    word = input("Enter a word to search: ")

    word_count = count_specific_word(text, word)
    common_word = identify_most_common_word(text)
    avg_length = calculate_average_word_length(text)
    paragraph_count = count_paragraphs(text)
    sentence_count = count_sentences(text)

    print(f"\nOccurrences of '{word}': {word_count}")
    print(f"Most common word: '{common_word}'")
    print(f"Average word length: {avg_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")


if __name__ == "__main__":
    main()