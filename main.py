from stats import get_num_words,count_chars,report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

    
def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) < 2:
        print("Invalid arguments")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    wc = get_num_words(book_text)
    char_count = count_chars(book_text)
    report(char_count, path, wc)

main()