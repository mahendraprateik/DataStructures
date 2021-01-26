import hashlib
import datetime

class Block(object):
    """
    Block class that initializes block data with timestamp, data and previous hash variables
    """

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        if self.previous_hash:
            pre_hash_string = self.data + self.previous_hash
        else:
            pre_hash_string = self.data
        return hashlib.sha256(pre_hash_string.encode()).hexdigest()

    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)


class BlockChain(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Append a block at the end of the blockchain

        Parameters:
        data (str): data to be used to create the block that is being added
        """
        if data is None or len(data) == 0:
            print("Please provide a valid data value")
            return

        if self.head is None:
            self.head = Block(datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"), data)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"), data, self.tail.hash)
            self.tail = self.tail.next

    def pop(self):
        """
        Pop the last value from the blockchain
        """
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        self.tail = current_node
        self.tail.next = None

    def convert_to_list(self):
        """
        Convert the blocks in the blockchain into a list and return the list
        """

        if self.head is None:
            print("There are no blocks in the chain")
            return
        li = []
        current_node = self.head
        while current_node:
            li.append([current_node.timestamp, current_node.previous_hash, current_node.data])
            current_node = current_node.next

        return li


# Test Cases - Regular

block_chain = BlockChain()

block1 = "First block"
block2 = "Second block"
block3 = "Third block"
block4 = "Fourth Block"

block_chain.append(block1)
block_chain.append(block2)
block_chain.append(block3)

print(block_chain.convert_to_list())
"""
[['24/01/2021 20:00:17', None, 'First block'],
['24/01/2021 20:00:17', '0ea9277023796a23a4bb5ff95f2cf26c18ae5e01f339934d6420f93a526d63f3', 'Second block'],
['24/01/2021 20:00:17', 'dda1fb5214ae938aea536020c18f12a4f34bd5f0cd6d07289a61d325a80e688b', 'Third block']]
"""

block_chain.pop()

print(block_chain.convert_to_list())
"""
[['24/01/2021 20:00:17', None, 'First block'],
 ['24/01/2021 20:00:17',
  '0ea9277023796a23a4bb5ff95f2cf26c18ae5e01f339934d6420f93a526d63f3',
  'Second block']]
"""


# Test cases - Edge

# Empty blockchain
block_chain = BlockChain()
block1 = ""
block_chain.append(block1) # Missinig data warning

block_chain = BlockChain()
block_chain.convert_to_list() # Empty blockchain warning

# Trying to think of a test case for same value, but 2 blocks can have the same value in my best understanding
