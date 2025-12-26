import sys

from stats import get_num_words, sort


def main(file):
    with open(file) as f:
        book = f.read().lower()
        num_words = get_num_words(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        sortedBook = sort(book)
        for item in sortedBook:
            print(f"{item['char']}: {item['num']}")


if sys.argv == ["main.py"]:
    raise Exception("Usage: python3 main.py <path_to_book>")
else:
    main(sys.argv[1])
