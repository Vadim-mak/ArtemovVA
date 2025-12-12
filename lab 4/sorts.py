"""
Реализация алгоритмов сортировки.
"""

# 1. Сортировка пузырьком (Bubble Sort)
def bubble_sort(arr):
    """
    Сортировка пузырьком.
    Временная сложность: O(n^2) во всех случаях.
    Пространственная сложность: O(1).
    """
    n = len(arr)                     # O(1)
    for i in range(n):               # O(n)
        for j in range(0, n - i - 1):  # O(n)
            if arr[j] > arr[j + 1]:    # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1)
    return arr


# 2. Сортировка выбором (Selection Sort)
def selection_sort(arr):
    """
    Сортировка выбором.
    Временная сложность: O(n^2) во всех случаях.
    Пространственная сложность: O(1).
    """
    n = len(arr)                     # O(1)
    for i in range(n):               # O(n)
        min_idx = i                  # O(1)
        for j in range(i + 1, n):    # O(n)
            if arr[j] < arr[min_idx]:  # O(1)
                min_idx = j            # O(1)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # O(1)
    return arr


# 3. Сортировка вставками (Insertion Sort)
def insertion_sort(arr):
    """
    Сортировка вставками.
    Временная сложность: O(n^2) в худшем и среднем, O(n) в лучшем.
    Пространственная сложность: O(1).
    """
    n = len(arr)                     # O(1)
    for i in range(1, n):            # O(n)
        key = arr[i]                 # O(1)
        j = i - 1                    # O(1)
        while j >= 0 and arr[j] > key:  # O(n)
            arr[j + 1] = arr[j]        # O(1)
            j -= 1                     # O(1)
        arr[j + 1] = key              # O(1)
    return arr


# 4. Сортировка слиянием (Merge Sort)
def merge_sort(arr):
    """
    Сортировка слиянием.
    Временная сложность: O(n log n) во всех случаях.
    Пространственная сложность: O(n).
    """
    if len(arr) <= 1:                # O(1)
        return arr
    
    mid = len(arr) // 2              # O(1)
    left = merge_sort(arr[:mid])     # O(n/2)
    right = merge_sort(arr[mid:])    # O(n/2)
    
    return merge(left, right)        # O(n)


def merge(left, right):
    """Вспомогательная функция для слияния двух отсортированных массивов."""
    result = []                      # O(1)
    i = j = 0                        # O(1)
    
    while i < len(left) and j < len(right):  # O(n)
        if left[i] <= right[j]:      # O(1)
            result.append(left[i])   # O(1)
            i += 1                   # O(1)
        else:
            result.append(right[j])  # O(1)
            j += 1                   # O(1)
    
    result.extend(left[i:])          # O(n)
    result.extend(right[j:])         # O(n)
    return result


# 5. Быстрая сортировка (Quick Sort)
def quick_sort(arr):
    """
    Быстрая сортировка.
    Временная сложность: O(n log n) в среднем, O(n^2) в худшем.
    Пространственная сложность: O(log n) в среднем.
    """
    if len(arr) <= 1:                # O(1)
        return arr
    
    pivot = arr[len(arr) // 2]       # O(1)
    left = [x for x in arr if x < pivot]      # O(n)
    middle = [x for x in arr if x == pivot]   # O(n)
    right = [x for x in arr if x > pivot]     # O(n)
    
    return quick_sort(left) + middle + quick_sort(right)  # O(n log n)


# Проверка корректности сортировки
def is_sorted(arr):
    """Проверяет, отсортирован ли массив по возрастанию."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))