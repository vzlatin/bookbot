from stats import get_word_cound, get_book_text, get_chars_map, sort_map
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>') 
        sys.exit(1)


    filepath = sys.argv[1] 
    contents = get_book_text(filepath)
    wordcount = get_word_cound(contents)
    chars_map = get_chars_map(contents)
    sorted_map = sort_map(chars_map)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {wordcount} total words')
    print('--------- Character Count -------')
    for c in sorted_map:
        if c['char'].isalpha():
            print(f'{c["char"]}: {c["num"]}')
    print('============= END ===============')

main()
