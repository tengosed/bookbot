def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict(dict):
    list_of_dicts = []
    for k in dict:
        if k.isalpha() is False:
            continue
        else:
            current_item = {
            "char": k,
            "num": dict[k]
            }
            list_of_dicts.append(current_item)

    def sort_on(items):
        return items["num"]
    
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts