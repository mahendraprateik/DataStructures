Problem 2: File Recursion

Worst case time complexity is: O(n*k)
    Algorithm:
        For loop: O(n)
        List append: O(1)
        List extend: O(k)
        Extends list by k elements for each for loop run: O(n*k)
