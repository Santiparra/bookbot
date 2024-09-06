def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_content(book_path)
    counted_words = count_words(file_contents)
    print(f"{counted_words} words were found in the provided text")

def get_book_content(path):
    with open(path) as f:
        return f.read()

def count_words(content_string):
    words = content_string.split()
    words_count = len(words)
    return words_count


main()