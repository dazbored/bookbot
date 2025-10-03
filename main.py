import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
    

def main():
    get_book_text(sys.argv[1])
    # print(get_book_text)
    

main()

from stats import word_count
w_count = word_count(sys.argv[1])

from stats import character_count
c_count = character_count(sys.argv[1])

from stats import sorted_char
s_count = sorted_char(c_count)



print(f"============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count ----------")
print(f"Found {w_count} total words")
print("--------- Character Count -------")
for item in s_count:
    ch, cnt = item["char"], item["num"]
    print(f"{ch}: {cnt}")
