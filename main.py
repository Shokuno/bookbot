def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return  filecontents

def main():
    print(get_book_text("books/frankenstein.txt"))

main()