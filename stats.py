def word_count(book):
    with open(book) as b:
        text = b.read()
        text_list = text.split()
    words = len(text_list)
    return words
    # print(f"Found {word_count} total words")

def character_count(book):
    with open(book) as b:
        text = b.read()
        chars = {}
        for characters in text:
            lower_char = characters.lower()
            if lower_char in chars:
                chars[lower_char] += 1
            else:
                chars[lower_char] = 1
        return chars

def sorted_char(chars):
    new_count = []
    for c, n in chars.items():
        if c.isalpha() == True:
            new_count.append({"char": c, "num": n})
            new_count.sort(key=lambda item: item["num"], reverse=True)
    return new_count

