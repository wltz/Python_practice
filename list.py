from typing import List, Self, Set, Dict
from collections import deque


def list_basic_operations():
    lst = [] # create empty list
    lst1: List[str] = []
    lst1.append("hello") # add element to the end of list
    lst1.append("world")
    print(lst1)  # ['hello', 'world']
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(lst)   # [1, 2, 3]
    lst = lst[::-1]  # reverse the list with slicing, lst[::-1] creates a new list in reverse order
    print(lst)   # [3, 2, 1]

    


if __name__ == "__main__":
    list_basic_operations()