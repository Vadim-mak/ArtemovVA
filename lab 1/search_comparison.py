def linear_search(arr, target):
    """
    Линейный поиск элемента в массиве.
    
    Args:
        arr: Массив для поиска
        target: Искомый элемент
    
    Returns:
        Индекс элемента или -1 если не найден
    """
    # O(n) - проходим по всем элементам массива
    for i in range(len(arr)):
        # O(1) - сравнение элемента
        if arr[i] == target:
            # O(1) - возврат индекса
            return i
    # O(1) - возврат -1
    return -1
    # Общая сложность: O(n)


def binary_search(arr, target):
    """
    Бинарный поиск элемента в отсортированном массиве.
    
    Args:
        arr: Отсортированный массив для поиска
        target: Искомый элемент
    
    Returns:
        Индекс элемента или -1 если не найден
    """
    # O(1) - инициализация переменных
    left = 0
    right = len(arr) - 1
    
    # O(log n) - цикл пока интервал поиска не пуст
    while left <= right:
        # O(1) - вычисление середины
        mid = (left + right) // 2
        
        # O(1) - сравнение с целевым элементом
        if arr[mid] == target:
            # O(1) - возврат индекса
            return mid
        # O(1) - если целевой элемент меньше
        elif arr[mid] > target:
            # O(1) - сдвиг правой границы
            right = mid - 1
        # O(1) - если целевой элемент больше
        else:
            # O(1) - сдвиг левой границы
            left = mid + 1
    
    # O(1) - возврат -1 если элемент не найден
    return -1
    # Общая сложность: O(log n)


def test_searches():
    """Тестирование функций поиска на различных сценариях."""
    print("Тестирование алгоритмов поиска:")
    print("=" * 50)
    
    # Тест 1: Поиск существующего элемента
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15]
    target1 = 7
    print(f"Массив: {arr1}")
    print(f"Поиск элемента: {target1}")
    print(f"Линейный поиск: индекс {linear_search(arr1, target1)}")
    print(f"Бинарный поиск: индекс {binary_search(arr1, target1)}")
    print()
    
    # Тест 2: Поиск несуществующего элемента
    target2 = 8
    print(f"Поиск элемента: {target2}")
    print(f"Линейный поиск: индекс {linear_search(arr1, target2)}")
    print(f"Бинарный поиск: индекс {binary_search(arr1, target2)}")
    print()
    
    # Тест 3: Поиск первого элемента
    target3 = 1
    print(f"Поиск элемента: {target3}")
    print(f"Линейный поиск: индекс {linear_search(arr1, target3)}")
    print(f"Бинарный поиск: индекс {binary_search(arr1, target3)}")
    print()


def measure_performance():
    """Измерение производительности алгоритмов на массивах разного размера."""
    import time
    import random
    
    print("Измерение производительности:")
    print("=" * 50)
    print(f"{'Размер':>8} | {'Линейный':>12} | {'Бинарный':>12} | {'Ускорение':>10}")
    print("-" * 60)
    
    sizes = [1000, 5000, 10000]
    
    for size in sizes:
        # Создание отсортированного массива
        arr = sorted(random.randint(1, size * 10) for _ in range(size))
        
        # Выбор целевого элемента (последний в массиве)
        target = arr[-1]
        
        # Замер времени для линейного поиска
        start_time = time.perf_counter()
        linear_search(arr, target)
        linear_time = time.perf_counter() - start_time
        
        # Замер времени для бинарного поиска
        start_time = time.perf_counter()
        binary_search(arr, target)
        binary_time = time.perf_counter() - start_time
        
        # Расчет ускорения
        speedup = linear_time / binary_time if binary_time > 0 else 0
        
        print(f"{size:8} | {linear_time:12.8f} | {binary_time:12.8f} | {speedup:10.2f}x")


if __name__ == "__main__":
    test_searches()
    measure_performance()