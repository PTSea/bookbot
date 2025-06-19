def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def number_of_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    new_text = text.lower()
    character_dict = {}
    for text in new_text:
        if text in character_dict:
            character_dict[text] += 1
        else:
            character_dict[text] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def sorted_character_counts(character_dict):
    list_of_entries = []
    for text in character_dict:
        if text.isalpha():
            smol_dict = {
                "char" : text,
                "num" :  character_dict[text]
            }
            list_of_entries.append(smol_dict)
    list_of_entries.sort(reverse=True, key=sort_on)
    return list_of_entries