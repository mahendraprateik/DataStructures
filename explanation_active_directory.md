# Problem 4: Active Directory

## Method and Data Structures:
I used recursion over doing it in a normal list form and looping over to check if it is a group or not. Because, I wanted to practice recursion more at this point. One downside of using recursion here is that the call stack limit for recursion in python is 10000, so if we end up having a recursive call stack that exceeds 10000, we will get an error.

## Worst case space complexity is: <b> O(1) </b>
Since it only returns a bool value True/False and returns it

## Worst case time complexity is: <b> O(n * k) </b>

* Algorithm:
    * Search for users in the user list for a group: <b> O(n) </b>
    * Recursively search for all k subgroups: <b> O(k) </b>
