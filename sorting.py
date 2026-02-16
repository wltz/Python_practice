import heapq
from typing import List, Set, Dict

def sort_list(lst: List[int]) -> List[int]:
    return sorted(lst)

def sort_set(s: Set[int]) -> List[int]:
    return sorted(s)

def sort_dict(d: Dict[int, int]) -> List[int]:
    return sorted(d.items(), key=lambda x: x[0])

def sort_interval():
    intervals = [[1, 3], [2, 1], [1, 2]]
    print("original intervals:", intervals)
    intervals.sort(key=lambda interval: interval[1])
    print("sorted intervals by end time:", intervals)
    intervals = [[1, 3], [2, 1], [1, 2]]
    print("original intervals:", intervals)
    intervals.sort(key=lambda interval: interval[0])
    print("sorted intervals by start time:", intervals)
    intervals = [[1, 3], [2, 1], [1, 2]]
    print("original intervals:", intervals)
    intervals.sort(key=lambda interval: (interval[0], interval[1]))
    print("sorted intervals by start time and end time:", intervals)
    intervals = [[1, 3], [2, 1], [1, 2]]
    print("original intervals:", intervals)
    intervals.sort(key=lambda interval: (interval[1], -interval[0])) 
    print("# sort by end time, if end time is the same, sort by start time in descending order:", intervals)

def sort_heapq():
    nums = [3, 1, 2, 6, 9, 8, 5]
    heapq.heapify(nums)
    print("heapified nums:", nums)
    while nums:
        print(heapq.heappop(nums))

if __name__ == "__main__":
    sort_interval()
    #sort_heapq()