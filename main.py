import sys
from stats import get_word_number, get_ch_number, sort_dic

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f'''============ BOOKBOT ============ 
Analyzing book found at {sys.argv[1]}...''')
    
    contents = get_book_text(sys.argv[1])
    words = get_word_number(contents)
    chars = get_ch_number(contents)

    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    sorted_chars = sort_dic(chars)
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()