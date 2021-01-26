# Problem 2: File Recursion

## Method and Data Structures:
I used recursion over doing it in a normal list form and looping over to check if it is a directory or not. Because, I wanted to practice recursion more at this point. One downside of using recursion here is that the call stack limit for recursion in python is 10000, so if we end up having a recursive call stack that exceeds 10000, we will get an error. 

## Worst case space complexity is: <b> O(k) </b>
k = number of files found/returned by the function

## Worst case time complexity is: <b> O(n*k) </b>
* Algorithm:
    * For loop: <b> O(n) </b>
    * List append: <b> O(1) </b>
    * List extend: <b> O(k) </b>
    * Extends list by k elements for each for loop run: <b> O(n* k) </b>
