from unittest import result
def main():
    path = "books/frankenstein.txt"
    text = read_file(path)
    num_words = count_words(text)
    num_char = count_char(text)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    for i in sorted(num_char):
        print(f"The '{i}' character was found {num_char[i]} times")
    print("--- End report ---")

def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_char(text):
    result = {}
    for i in text:
        i = i.lower()
        if i in result:
            result[i] += 1
        elif i.isalpha():
            result[i] = 1
    return result


main()
