# Сортировка слиянием

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Сливаем отсортированные половины
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    left_index = 0
    right_index = 0

    # Слияние двух половин в отсортированный массив
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы
    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr

# Пример использования
arr = [38, 27, 43, 3, 9, 82, 3,10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
