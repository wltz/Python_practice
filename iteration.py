from typing import List, Self, Set, Dict
from collections import deque 
import heapq 


def iterate_list():
    lst = []
    lst.append(3)
    lst.append(5)
    lst.append(7)

    for n in lst: # iterate with elemment
        print("element in list:", n)
    # for i in range(idx_start, idx_stop, step)
    # iterate through the list with idx_start, 
    # end with idx_stop(exclusive)
    for i in range(len(lst)):  # iterte with index      
        print("ith element in list", lst[i])

    for i in range(1,len(lst)):
        print("ith index of list", i, lst[i])

    for i in lst[1:]:  # iterate with slice
        print("element in list with slice:", i)    

def iterate_list_reverse():
    """
    reversed(lst) returns a new list in reverse order.
    range(len(lst)-1, -1, -1) iterates from the last index to the first index.
    range(start, stop, step)
    Produces values from start up to but not including stop.
    start is inclusive, stop is exclusive.
    step is the increment. Default is 1, negative value means reverse order.
    """
    lst = []
    lst.append(3)
    lst.append(5)
    lst.append(7)   

    for n in reversed(lst):
        print("element in list in reverse order:", n)   
    
    for i in range(len(lst)-1, -1, -1):
        print("ith element in list in reverse order:", lst[i])

def iterate_dict():
    hm = {}
    hm[1] = 2
    hm[2] = 3
    hm[3] = 4

    for k,v in hm.items():
        print("key, val pair:", k, v)

    for k in hm.keys():
        print("key in map:", k)

    for v in hm.values():
        print("val in map:", v)         

    if 1 in hm.keys():
        print("key 1 is in map")
    else:
        print("key 1 is not in map")

    if 1 in hm:
        print("key 1 is in map")
    else:
        print("key 1 is not in map")


def heapq_test():
    hm = {}
    hm[3] = 6
    hm[5] = 4
    hm[7] = 9
    heap = []

    for k,v in hm.items():
        heapq.heappush(heap, (v,k))

    # Below is WRONG
    # for p in heap:
    #     p = heapq.heappop(heap, (v, k))
    #     print("sorted by val:", p)            

    while heap:
        v, k = heapq.heappop(heap)
        print("sorted key val pair:", k, v)

def matrix_test(m:List[List[int]]):
    if not m:
        return []

    INF = float('inf')
    print(INF > 10000)

    r = len(m)
    c = len(m[0])

    matrix = [[INF] * c for _ in range(r)] 

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c])      

    return matrix

if __name__ == "__main__":
    #iterate_list_reverse()
    #iterate_list()
    iterate_dict()
    #heapq_test()
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]
    #matrix_test(matrix)