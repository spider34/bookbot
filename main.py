from unittest import result
def main():
    path = "books/frankenstein.txt"
    text = read_file(path)
    num_words = count_words(text)
    print(count_char(text))

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
