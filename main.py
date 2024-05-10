def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = number_of_words(text)
    print(f"{num_words} words found in the entire book.")
    lowercase = small_letters(text)
    print(len(lowercase))

def get_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    words = text.split()
    return len(words)

def small_letters(text):
    return text.lower()



main()