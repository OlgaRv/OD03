# Сортировка вставкой с вводом произвольного количества чисел

def read_numbers():
    numbers = []
    while True:
        user_input = input("Введите целое число (или 'stop' для завершения ввода): ")
        if user_input.lower() == 'stop':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Пожалуйста, введите действительное целое число.")
    return numbers

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    numbers = read_numbers()
    print("Введенные числа:", numbers)

    a = list(numbers)
    insert_sort(a)
    print(a)