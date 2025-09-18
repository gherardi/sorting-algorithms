from typing import List

def heap_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the heap sort algorithm.
    This function modifies the input list in place and returns it.
    Args:
        arr (List[int]): The list of integers to sort.
    Returns:
        List[int]: The sorted list.
    """
    length = len(arr)
    
    # Build a max heap from the array
    for root_index in range(length // 2 - 1, -1, -1):
        _heapify(arr, length, root_index)
    
    # Extract elements from heap one by one
    for current_index in range(length - 1, 0, -1):
        # Move current root to end
        arr[0], arr[current_index] = arr[current_index], arr[0]
        
        # Call heapify on the reduced heap
        _heapify(arr, current_index, 0)
    
    return arr


def _heapify(arr: List[int], heap_size: int, root_index: int) -> None:
    """
    Helper function to heapify a subtree rooted at given index.
    This function maintains the max heap property.
    Args:
        arr (List[int]): The array to heapify.
        heap_size (int): Size of the heap.
        root_index (int): Root index of the subtree.
    """
    largest_index = root_index  # Initialize largest as root
    left_child_index = 2 * root_index + 1  # Left child
    right_child_index = 2 * root_index + 2  # Right child
    
    # If left child is larger than root
    if left_child_index < heap_size and arr[left_child_index] > arr[largest_index]:
        largest_index = left_child_index
    
    # If right child is larger than largest so far
    if right_child_index < heap_size and arr[right_child_index] > arr[largest_index]:
        largest_index = right_child_index
    
    # If largest is not root
    if largest_index != root_index:
        arr[root_index], arr[largest_index] = arr[largest_index], arr[root_index]
        
        # Recursively heapify the affected sub-tree
        _heapify(arr, heap_size, largest_index)