from typing import List

def merge_sort(arr: List[int]) -> List[int]:
	"""
	Sorts a list of integers in ascending order using the merge sort algorithm.
	This function modifies the input list in place and returns it.
	Args:
		arr (List[int]): The list of integers to sort.
	Returns:
		List[int]: The sorted list.
	"""
	length = len(arr)
	if length <= 1:
		return arr

	mid = length // 2
	left_half = arr[:mid]
	right_half = arr[mid:]

	merge_sort(left_half)
	merge_sort(right_half)

	left_index = 0
	right_index = 0
	merged_index = 0

	# Merge the sorted halves back into the original array
	while left_index < len(left_half) and right_index < len(right_half):
		if left_half[left_index] <= right_half[right_index]:
			arr[merged_index] = left_half[left_index]
			left_index += 1
		else:
			arr[merged_index] = right_half[right_index]
			right_index += 1
		merged_index += 1

	# Copy any remaining elements of left_half
	while left_index < len(left_half):
		arr[merged_index] = left_half[left_index]
		left_index += 1
		merged_index += 1

	# Copy any remaining elements of right_half
	while right_index < len(right_half):
		arr[merged_index] = right_half[right_index]
		right_index += 1
		merged_index += 1

	return arr
