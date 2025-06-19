import sys
from stats import number_of_words, get_book_text, get_character_counts, sorted_character_counts

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = number_of_words(text)
    character_counts = get_character_counts(text)
    sorted_list = sorted_character_counts(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

main()