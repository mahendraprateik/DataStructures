<h1> Problem 1: LRU Cache </h1>

<h2> Worst case time complexity is: <b> O(1) </b> </h2>

* Algorithm:
    * get(): <b>O(1)</b>
        * dict.get method runs in constant time
    * set(): <b>O(1)</b>
        * popitem() method removes the least recent element so runs in constant time
