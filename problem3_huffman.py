# Used to create prriority queue
import heapq

class Node(object):
    """
    Node class
    """
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other_node):
        if other_node is None:
            return
        return self.frequency < other_node.frequency

    def __eq__(self, other_node):
        if other_node is None:
            return
        return self.frequency == other_node.frequency

def make_frequency_dict(string):
    """
    Function to create frequency dict from string

    Parameters:
    string (str): String to create frequency dict from

    Returns:
    Dict of the form of {character: frequqncy}
    """
    string_set = set(string)

    di = dict()
    for s in string_set:
        di[s] = di.get(s, 0) + string.count(s)

    return di


def make_priority_queue(di):
    """
    Function that converta frequency dict into a priority queue heap

    Parameters:
    di (dict): Frequency dict

    Return:
    heap (list): priority queue of nodes
    """
    heap = []
    for key in di:
        heapq.heappush(heap, Node(key, di[key]))
    return heap


def build_huffman_tree(heap):
    """
    Function that converts a priority queue list to a tree

    Parameters:
    heap (list): heap priority queue of nodes

    Returns:
    root node of the tree
    """
    while len(heap) > 1:
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)

        merged_node = Node(None, min1.frequency + min2.frequency)
        merged_node.left = min1
        merged_node.right = min2
        heapq.heappush(heap, merged_node)

    return heap[0]


def create_code(tree):
    """
    Func that initiates code creation recursively

    Parameters:
    tree (Node Object): root node of tree

    Returns:
    Dict of the form of {character: encoded_character}
    """
    root = tree
    current_code = ""
    code_dict = create_code_recursion(root, current_code)
    return code_dict


def create_code_recursion(node, current_code):
    """
    Func that recurively traverses through the tree and assign codes

    Parameters:
    node (Node Object): to start the traversing from
    current_code (str): current_code being formed

    Returns:
    Dict of the form of {character: encoded_character}
    """
    if node is None:
        return
    if node.character is not None:
        return {node.character: current_code}
    code_dict = {}

    code_dict.update(create_code_recursion(node.left, current_code + "0"))
    code_dict.update(create_code_recursion(node.right, current_code + "1"))


    return code_dict


import sys

def huffman_encoding(data):
    di = make_frequency_dict(data)
    heap = make_priority_queue(di)
    tree = build_huffman_tree(heap)
    code_dict = create_code(tree)

    encoded_text = ""
    for s in data:
        encoded_text += code_dict[s]

    return encoded_text, tree

    pass

def huffman_decoding(data,tree):
    if len(data) == 0:
        return
    decoded_text = ""
    current_node = tree

    for s in data:
        if s == '0' and current_node.left:
            current_node = current_node.left
        elif s == '1' and current_node.right:
            current_node = current_node.right

        if not current_node.left and not current_node.right:
            decoded_text += current_node.character
            current_node = tree
    return decoded_text

    pass

if __name__ == "__main__":
    codes = {}

    # Test cases
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
