from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    md = {}
    md[name] = age
    return md
    pass


def list_to_dict(words: List[str]) -> Dict[str, int]:
    md ={}
    l = len(words)
    for i in range (l):
        md[words[i]]= i
    return md
    pass



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
