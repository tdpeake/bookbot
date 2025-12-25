def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        #print("\n Ran 'with'")
    #print("\nfinished with get_book_text")
    return file_contents

def get_num_words(text):
    book = get_book_text(text)
    split_text = book.split()
    word_count = len(split_text)
    return word_count
    # count = len(split_text)
    # return count

def get_num_char(text):
    book = get_book_text(text)
    book_char = list(book.lower())
    char_count = {}
    for character in book_char:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

def sort_key(items):
    return items['num']

def sort_list(dict):
    new_list = []
    for key, value in dict.items():
        new_list.append({'char': key, 'num': value})
    new_list.sort(reverse=True, key=sort_key)
    return new_list




