def get_num_words(text):
    word_count = None

    words = text.split()
    word_count = len(words)

    return f"Found {word_count} total words"

def character_count(text):
    lower_text = text.lower()
    
    char_dictionary = {}

    for char in lower_text:
        if char in char_dictionary:
            char_dictionary[char] = char_dictionary[char] + 1
        else:
            char_dictionary[char] = 1
    
    return char_dictionary



def character_report(char_dictionary):
    def sort_on(items):
        return items["num"]                                                   
    
    report_list = []

    for char in char_dictionary:
        if char.isalpha():
            item = {"char":char, "num":char_dictionary[char]}
            report_list.append(item)
    
    report_list.sort(reverse=True, key=sort_on)

    return report_list
