def get_book_text(filepath):
    file_contents = filepath.read()
    return file_contents


def count_words(filepath):
    file_contents = len(filepath.read().split())
    return file_contents


def main():
    with open("books/frankenstein.txt") as f:
        # print(get_book_text(f))
        num_words = count_words(f)
        print(f"Found {num_words} total words")


main()
