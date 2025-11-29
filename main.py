import sys
from stats import number_words
from stats import num_chars
from stats import char_build

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    file_path = f"{filename}"
    text = get_book_text(file_path)
    num_words = number_words(text)
    num_characters = num_chars(text)
    sorted_chars = char_build(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for one_dict in sorted_chars:
        ch = one_dict["char"]
        count = one_dict["num"]
        if ch.isalpha() == True:
            print(f"{ch}: {count}")
    print("============= END ===============")

main()