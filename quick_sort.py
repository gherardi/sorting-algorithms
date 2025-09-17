from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the quick sort algorithm.
    This function modifies the input list in place and returns it.
    Args:
        arr (List[int]): The list of integers to sort.
    Returns:
        List[int]: The sorted list.
    """
    length = len(arr)
    if length <= 1:
        return arr
    
    _quick_sort_helper(arr, 0, length - 1)
    return arr


def _quick_sort_helper(arr: List[int], low_index: int, high_index: int) -> None:
    """
    Helper function for quick sort that recursively sorts subarrays.
    Args:
        arr (List[int]): The list to sort.
        low_index (int): Starting index of the subarray.
        high_index (int): Ending index of the subarray.
    """
    if low_index < high_index:
        # Partition the array and get the pivot index
        pivot_index = _partition(arr, low_index, high_index)
        
        # Recursively sort elements before and after partition
        _quick_sort_helper(arr, low_index, pivot_index - 1)
        _quick_sort_helper(arr, pivot_index + 1, high_index)


def _partition(arr: List[int], low_index: int, high_index: int) -> int:
    """
    Partitions the array around a pivot element.
    Args:
        arr (List[int]): The list to partition.
        low_index (int): Starting index of the subarray.
        high_index (int): Ending index of the subarray.
    Returns:
        int: The final position of the pivot element.
    """
    # Choose the rightmost element as pivot
    pivot = arr[high_index]
    
    # Index of smaller element, indicates right position of pivot
    smaller_element_index = low_index - 1
    
    for current_index in range(low_index, high_index):
        # If current element is smaller than or equal to pivot
        if arr[current_index] <= pivot:
            smaller_element_index += 1
            arr[smaller_element_index], arr[current_index] = arr[current_index], arr[smaller_element_index]
    
    # Place pivot in correct position
    arr[smaller_element_index + 1], arr[high_index] = arr[high_index], arr[smaller_element_index + 1]
    return smaller_element_index + 1