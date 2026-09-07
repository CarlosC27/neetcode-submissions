from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    n = 0
    l = len(nums)
    for i in range(l):
        if nums[i] == x:
            n += 1
    return n 
    pass



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
