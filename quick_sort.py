# Быстрая сортировка

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = list(filter(lambda i: i < pivot, array))
        center = [i for i in array if i == pivot]
        right = [i for i in array[1:] if i > pivot]

        return quick_sort(left) + center + quick_sort(right)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))