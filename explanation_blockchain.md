# Problem 5: blockchain

## Method and Data Structures:
I used a Linkedlist in this since it is tailor made for a data structure where the information of the next/previous node is stored in the node.

## Worst case space complexity is: <b> O(n) </b>
n = number of blocks to be used to create a blockchain

## Worst case time complexity is: O(n)

* Algorithm:
    * Append method: <b> O(1) </b>
        * It will work on a constant time since we have the tail of the linked list and we just need to append to that

    * Pop method: <b> O(n) </b>
        * Popping the tail would be done in linear time since we have to traverse through the list from the head

    * convert_to_list(): <b> O(n) </b>
        * Converting to list would be done in linear time since we have to traverse through the list from the head

    * Append would be done in constant time
