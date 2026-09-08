from typing import List

def read_integers() -> List[int]:
    n = input()
    nl = n.split(",")
    inl = [int(i) for i in nl]
    return inl
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
