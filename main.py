import sys
from stats import get_num_words, get_char_counts, sort_char_counts


def main():
    # 1. Check we got exactly one extra argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 2. Use that argument as the book path
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # 3. Open the file at that path
    with open(book_path) as f:
        text = f.read()

    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()


