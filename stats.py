def get_book_text(filepath):
    file_contents = filepath
    return file_contents


def get_num_words(filepath):
    file_contents = len(filepath.split())
    return file_contents


def get_num_letters(filepath):
    letterCount = {}

    for ch in filepath:
        if ch.isalpha():
            if ch in letterCount:
                letterCount[ch] += 1
            else:
                letterCount[ch] = 1
    return letterCount


def sort_on(dictionary):
    return dictionary["num"]


def sort(file):
    counts = []
    starter = get_num_letters(file)
    for key, value in starter.items():
        temp = {"char": key, "num": value}
        counts.append(temp)
        counts.sort(reverse=True, key=sort_on)

    return counts
