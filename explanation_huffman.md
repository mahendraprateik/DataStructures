Problem 3: Huffman Coding

Worst case time complexity is: O(nlogn)
    Algorithm:
        huffman_encoding
            make_frequency_dict():  O(n)
            Looping through n elements in data.
            make_priority_queue(): O(nlogn)
            Looping through the dict n times and sorting each time.
            build_huffman_tree(): O(n)
            Loops through each node in the heap
            create_code(): O(logn)
            Recursively runs until depth of tree.
            Loop through data to create encoded data from dict O(n)

        huffman_decoding()
            Loop through encoded string (length k) to create decoded data from tree: O(k)
