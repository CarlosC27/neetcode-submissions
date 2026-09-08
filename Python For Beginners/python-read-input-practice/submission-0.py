def add_two_numbers() -> int:
    nums = input()
    nl = nums.split(",")
    inl = [int(i) for i in nl]
    s = inl[0] + inl[1]
    return s
    pass



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
