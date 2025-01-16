def main():
    path = "books/frankenstein.txt"
    print(read_file(path))



def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()
