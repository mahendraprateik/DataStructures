class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return
        node = self.head
        out = ""
        while node:
            out += str(node.value) + " ---> "
            node = node.next
        return out

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    """
    Function to find union of 2 linked lists

    Parameters:
    llist_1 (LinkedList Object): first linked list
    llist_2 (LinkedList Object): second linked list

    Returns:
    Union-ed linked list of all elements
    """
    if llist_1.head is None:
        return llist_2
    elif llist_2.head is None:
        return llist_1

    union_set = set()

    llist1_node = llist_1.head
    while llist1_node:
        union_set.add(llist1_node.value)
        llist1_node = llist1_node.next

    llist2_node = llist_2.head
    while llist2_node:
        union_set.add(llist2_node.value)
        llist2_node = llist2_node.next

    llist_union = LinkedList()
    for ele in union_set:
        llist_union.append(ele)

    return str(llist_union)
    pass


def intersection(llist_1, llist_2):
    # Your Solution Here
    """
    Function to find intersection of 2 linked lists

    Parameters:
    llist_1 (LinkedList Object): first linked list
    llist_2 (LinkedList Object): second linked list

    Returns:
    Intersection-ed linked list of all elements
    """
    if llist_1 is None or llist_2 is None:
        return None

    set1 = set()

    llist1_node = llist_1.head

    while llist1_node:
        set1.add(llist1_node.value)
        llist1_node = llist1_node.next

    set2 = set()

    llist2_node = llist_2.head

    while llist2_node:
        set2.add(llist2_node.value)
        llist2_node = llist2_node.next

    intersection_set = set1.intersection(set2)
    if len(intersection_set) == 0:
        return None

    llist_intersection = LinkedList()

    for ele in intersection_set:
        llist_intersection.append(ele)

    return llist_intersection

    pass


# Test cases

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Union\n",union(linked_list_1, linked_list_2))

print("Intersection\n",intersection(linked_list_1, linked_list_2))

"""
Union
 32 ---> 65 ---> 2 ---> 35 ---> 3 ---> 4 ---> 6 ---> 1 ---> 9 ---> 11 ---> 21 --->
Intersection
 4 ---> 21 ---> 6 --->
"""

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = []
element_4 = [1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print("Union\n",union(linked_list_3, linked_list_4))

print("Intersection\n",intersection(linked_list_3, linked_list_4))

"""
Union
 1 --->
Intersection
 None
"""


linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [1]
element_6 = [1]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print("Union\n",union(linked_list_5, linked_list_6))

print("Intersection\n",intersection(linked_list_5, linked_list_6))

"""
Union
 1 --->
Intersection
 1 --->
"""
