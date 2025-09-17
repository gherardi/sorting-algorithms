from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.
    This function modifies the input list in place and returns it.
    Args:
        arr (List[int]): The list of integers to sort.
    Returns:
        List[int]: The sorted list.
    """
    length = len(arr)
    
    # Traverse through all array elements
    for current_index in range(length):
        # Find the minimum element in remaining unsorted array
        minimum_index = current_index
        
        for comparison_index in range(current_index + 1, length):
            if arr[comparison_index] < arr[minimum_index]:
                minimum_index = comparison_index
        
        # Swap the found minimum element with the first element
        arr[current_index], arr[minimum_index] = arr[minimum_index], arr[current_index]
    
    return arr