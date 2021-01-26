# Problem 3: Huffman Coding 

## Method and Data Structures:
The following data structures were used:

* Node class: In order to create a tree
* minheap: In order to build a priority queue to pop the minimum value easily
* Tree: In order to build nodes around the minimum values and traverse through the nodes to decipher the codes

## Worst case space complexity is: <b> O(k) </b> 
k = number of nodes in the tree, since we end up creating a node for every value in the tree

## Worst case time complexity is: <b> O(nlogn) </b> 

* Algorithm:
    * huffman_encoding
        * make_frequency_dict(): <b> O(n) </b>
            * Looping through n elements in data.
        * make_priority_queue(): <b> O(nlogn) </b>
            * Looping through the dict n times and sorting each time.
        * build_huffman_tree(): <b> O(n) </b>
            * Loops through each node in the heap
        * create_code(): <b> O(logn) </b>
            * Recursively runs until depth of tree.
        * Loop through data to create encoded data from dict <b> O(n) </b>
        
    * huffman_decoding()
        * Loop through encoded string (length k) to create decoded data from tree: <b> O(k) </b>
