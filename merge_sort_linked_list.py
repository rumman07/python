from linked_list import *

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list

    Takes O(n log n) time
    Takes O(n) space
    """
    if linked_list.__len__() == 1:
        return linked_list
    elif linked_list.head is None: 
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(log n) time
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else: 
        size = linked_list.__len__()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid -1)

        left_half = linked_list
        right_half = SinglyLinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None 

        return left_half, right_half
    
def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = SinglyLinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right as long until the tail node of both
    # left and right
    while left_head and right_head:
        # If the head node of left is None, we're at the tail
        # Add the tail node from right to the merged linked list
        if left_head is None: 
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        
        # If the head node of right is None, we're at the tail
        # Add the tail node from left to the merged linked list
        elif right_head is None:
            current.next_node = left_head 
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is lesser than right set current to left node
            # Move left head to next node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on left is greater than right set current to right node
            # Move right head to next node
            else: 
                current.next_node = right_head
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head 

    return merged

l = SinglyLinkedList()
l.add(5)
l.add(8)


merge_sort(l)










         











