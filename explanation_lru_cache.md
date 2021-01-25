Problem 1: LRU Cache

Worst case time complexity is: O(1)

Algorithm:
    get(): O(1)
        dict.get method runs in constant time
    set(): O(1)
        popitem() method removes the least recent element so runs in constant time
