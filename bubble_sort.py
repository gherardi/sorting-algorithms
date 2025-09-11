from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.
    This function modifies the input list in place and returns it.
    Args:
        arr (List[int]): The list of integers to sort.
    Returns:
        List[int]: The sorted list.
    """
    length = len(arr)

    # Outer loop for each pass through the list
    for i in range(length):
        # Inner loop for comparing adjacent elements
        for j in range(0, length - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr