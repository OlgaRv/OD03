# пузырьковая сортировка
def bubble_sort(mas):
    for i in range(len(mas)):
        for j in range(len(mas) - 1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
        print(mas)
    return print(mas)

a = [5, 6, 1, 0, 9, 8, 7, 2, 4, 3]

bubble_sort(a)