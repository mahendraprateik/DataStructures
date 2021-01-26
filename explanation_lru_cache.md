# Problem 1: LRU Cache

## Method and Data Structures:
Many data structures can be used perform LRU caching like dictionaries, sets (maybe) as all of them work in a constant time. Ordered dictionary was chosen as it provides an additional advantage of popping the most/recent element in constant time when the LRU cache reaches its capacity.

## Worst case space complexity is: <b> O(n) </b>
Since it stores n items in the cache

## Worst case time complexity is: <b> O(1) </b>
 
* Algorithm:
    * get(): <b>O(1)</b>
        * dict.get method runs in constant time
    * set(): <b>O(1)</b>
        * popitem() method removes the least recent element so runs in constant time
