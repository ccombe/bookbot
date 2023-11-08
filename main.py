def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)
    print_pretty_dict(chars_dict, book_path)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def alpha_only(text):
    return text if text.key().isalpha() else None

def print_pretty_dict(text, path):
    spacer = "---"
    sorted_dict = dict(sorted(text.items(), key=lambda x:x[1], reverse=True))
    # filtered_dict = {filter(alpha_only, sorted_dict.items())}
    print(f"{spacer} Begin report of {path} {spacer}")
    for k, v in sorted_dict.items():
        if k.isalpha():
            print(f"The {k} character was found {v} times")
    print(f"{spacer} End report {spacer}")

main()