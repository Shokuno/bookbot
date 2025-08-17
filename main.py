from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return  filecontents

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    print(get_num_words(frankenstein_text))

main()