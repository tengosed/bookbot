from stats import get_num_words, get_chars_dict, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    # print(f"Found {num_words} total words")
    # print(chars_dict)
    list_dicts = sort_dict(chars_dict)
    # print(list_dicts)
    print_reported_stats(list_dicts, book_path, num_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_reported_stats(stats, path, num_words):
    print("============ BOOKBOT ============")
    print("Analyzing book found at path:", path, "...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words:")
    print("--------- Character Count -------")
    for item in stats:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")
main()