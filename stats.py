def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_cound(text):
    return len(text.split())

def get_chars_map(text):
    char_map = {}
    for c in text.lower():
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1
    return char_map


def transform_c_map(c_map):
    c_list = []
    for k in c_map:
        c_list.append({'char': k, 'num': c_map[k]})
    return c_list

def sort_on(c_list):
    return c_list['num']

def sort_map(c_map):
    c_list = transform_c_map(c_map)
    c_list.sort(reverse=True, key=sort_on)
    return c_list
