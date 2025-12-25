from stats import get_num_words, get_num_char, sort_list
import sys


def sort_on(items):
    return items['num']

def main():
    print("Usage: python3 main.py <path_to_book>")
    print(sys.argv[1])

    program_name = " BookBot "
    book_path = sys.argv[1]
    word_count = get_num_words(book_path)
    print(f"{program_name:{'='}^{33}}")
    print(f"Analyzing book found at {book_path}")
    print(f"{' Word Count ':{'-'}^{33}}")
    print(f"Found {get_num_words(book_path)} total words")
    print(f"{' Character Count ':{'-'}^{33}}")    
    
    for i in sort_list(get_num_char(book_path)):
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
        else:
            pass
    
    print(f"{' End ':{'='}^{33}}")  
    print("\nFinished Running Main")
    

    

main()