from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    md = {}
    wl  = len(word)
    for i in range(wl):
        if word[i] not in md :
            md.update({word[i]: 1})
        else:
            md.update({word[i]: md[word[i]] +1})
    return md
    pass




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
