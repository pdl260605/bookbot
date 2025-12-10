#!/usr/bin/env python3
def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

def get_num_words(file_content):
    print(f"Found {len(file_content.split())} total words")
        

def get_char_count(file_content):
    res = {}
    file_lower = file_content.lower()
    for char in file_lower:
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1
    return res

def sort_dict(char_count):
    res = []
    for char in char_count:
        res.append({"char" : char, "num" : char_count[char]})
    def sort_on(items):
        return items["num"]
    
    res.sort(reverse=True, key=sort_on)
    return res

def print_report(file_path):
    file_content = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    get_num_words(file_content)
    print("--------- Character Count -------")
    char_count = get_char_count(file_content)
    res = sort_dict(char_count)
    for item in res:
        #     print(f"{item["char"]}: {item["nums"]}")
        if item["char"].isalpha():
            idx1 = "char"
            idx2 = "num"
            print(f"{item[idx1]}: {item[idx2]}")