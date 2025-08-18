from stats import get_num_words
from stats import character_count
from stats import character_report

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return  filecontents

def main():
    book_filepath = "books/frankenstein.txt"

    frankenstein_text = get_book_text(book_filepath)
    
    num_words = get_num_words(frankenstein_text)
    char_count = character_count(frankenstein_text)
    char_report = character_report(char_count)

    # Print report
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_filepath}...\n----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for item in char_report:
        print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()