<h1> Problem 3: Huffman Coding </h1>

<h2> Worst case time complexity is: <b> O(nlogn) </b> </h2>

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
