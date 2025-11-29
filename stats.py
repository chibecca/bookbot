def number_words(text):
    words = text.split()
    number = len(words)
    return number

def num_chars(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def char_build(chars):
    char_list = []
    for char in chars:
        num = chars[char]
        one_dict = {"char": char, "num": num}
        char_list.append(one_dict)
    char_list.sort(key = helper, reverse = True)
    return char_list

def helper(one_dict):
    return one_dict["num"]
