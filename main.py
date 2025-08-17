from stats import get_num_words
from stats import character_count

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return  filecontents

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")

    char_count = character_count(frankenstein_text)

    print(get_num_words(frankenstein_text))
    print(char_count)
    

main()