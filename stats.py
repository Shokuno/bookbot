def get_num_words(text):
    word_count = None

    words = text.split()
    word_count = len(words)
    
    return f"{word_count} words found in the document"

def character_count(text):
    lower_text = text.lower()
    
    char_dictionary = {}

    for char in lower_text:
        if char in char_dictionary:
            char_dictionary[char] = char_dictionary[char] + 1
        else:
            char_dictionary[char] = 1
    
    return char_dictionary