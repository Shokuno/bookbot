def get_num_words(text):
    word_count = None

    words = text.split()
    word_count = len(words)
    
    return f"{word_count} words found in the document"