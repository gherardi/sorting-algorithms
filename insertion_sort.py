from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the insertion sort algorithm.
    This function modifies the input list in place and returns it.
    Args:
        arr (List[int]): The list of integers to sort.
    Returns:
        List[int]: The sorted list.
    """
    length = len(arr)

    for index in range(1, length):
        current_value = arr[index]
        position = index - 1
        # Move elements of arr[0..index-1], that are greater than current_value,
        # to one position ahead of their current position
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current_value
    return arr
