def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_content(book_path)
    counted_words = count_words(file_contents)
    counted_characters = character_counter(file_contents)
    counted_ordered_characters =  sort_dict(counted_characters)
    print()
    print(f"--- Here begins the report of {book_path} ---")
    print()
    print(f"{counted_words} words were found in the provided text")
    print()

    for item in counted_ordered_characters:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print()
    print(f"--- Ending report of {book_path} ---")
    

def get_book_content(path):
    with open(path) as f:
        return f.read()

def count_words(content_string):
    words = content_string.split()
    words_count = len(words)
    return words_count

def character_counter(text_as_string):
    text_to_lower = text_as_string.lower()
    char_dict = {}
    for string in text_to_lower:
        if not string.isalpha():
            continue
        elif string in char_dict:
            char_dict[string] += 1
        else:
            char_dict[string] = 1    
    return char_dict

def sort_dict(counted_chars_dict):
    sorted = []
    for char in counted_chars_dict:
        sorted.append({"char": char, "num": counted_chars_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dict):
    return dict["num"]

main()