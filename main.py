import questionary
import time
import random
from typing import Callable

from bubble_sort import bubble_sort
# from insertion_sort import insertion_sort
# from merge_sort import merge_sort
# from quick_sort import quick_sort
# from selection_sort import selection_sort
# from heap_sort import heap_sort

LIST_SIZE = 10000

RANDOM_LIST = [random.randint(1, 1000) for _ in range(LIST_SIZE)]

SORTING_ALGORITHMS = [
    "Bubble sort",
    "Insertion sort", 
    "Merge sort",
    "Quick sort",
    "Selection sort",
    "Heap sort",
]

def measure_algorithm_performance(algorithm_func: Callable):
    # Measures and reports the execution time of a sorting algorithm.
    start_time = time.perf_counter()
    algorithm_func(RANDOM_LIST)
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    algorithm_name = algorithm_func.__name__

    print(f"{algorithm_name} took {execution_time:.6f} seconds to sort {LIST_SIZE} elements.")


def main():
    # prompt the user to select a sorting algorithm interactively
    choice = questionary.select(
        "Which sorting algorithm do you want to use?",
        choices=SORTING_ALGORITHMS
    ).ask()

    # handle the user's choice
    match choice:
        case "Bubble sort": measure_algorithm_performance(bubble_sort)
        # case "Insertion sort": measure_algorithm_performance(insertion_sort)
        # case "Merge sort": measure_algorithm_performance(merge_sort)
        # case "Quick sort": measure_algorithm_performance(quick_sort)
        # case "Selection sort": measure_algorithm_performance(selection_sort)
        # case "Heap sort": measure_algorithm_performance(heap_sort)
        case _:
            print("No valid selection made.")

if __name__ == "__main__":
    main()
