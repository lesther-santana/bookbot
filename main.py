def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counts = count_letters(text)
    print(f"{num_words} words found in the document")
    print_report(counts)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_letters(text):
    counts = {}
    for letter in text:
        if not letter.isalpha():
            continue
        c = letter.lower()
        counts[c] = counts.get(c, 0) + 1
    return counts


def print_report(counts):
    for k, v in counts.items():
        s = f"The '{k}' character was found {v} times"
        print(s)
main()
