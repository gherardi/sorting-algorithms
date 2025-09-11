import random
from bubble_sort import bubble_sort

random_list = [random.randint(1, 1000) for _ in range(1000)]

if __name__ == "__main__":
    sorted_list = bubble_sort(random_list)
    print(sorted_list)