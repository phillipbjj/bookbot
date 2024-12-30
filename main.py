def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = word_counter(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
def word_counter(text):
    split_text = text.split()
    count = len(split_text)
    return count

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_by(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
main()