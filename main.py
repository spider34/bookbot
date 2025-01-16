def main():
    path = "books/frankenstein.txt"
    text = read_file(path)
    print(count_words(text))

def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    return len(text.split())

main()
