import random
from task.ProfileDecorator import ProfileDecorator

@ProfileDecorator
def bubble_sort(array):
    n = len(array)

    if n <= 1:
        return array
    
    for i in range(n-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    
    return bubble_sort(array[:-1]) + [array[-1]]

def bubble_sort_interface() -> None:
    arr = []

    for i in range (0, 100):
        arr.append(random.randint(0,10000))

    bubble_sort(arr)

    for i in arr:
        print(i)

    calls, totalTime = bubble_sort.get_stats()

    print(
        f"Number of calls: {calls}\n" +
        f"Execution time: {totalTime}"
    )