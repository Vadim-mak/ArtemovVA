"""
Генерация тестовых данных для сортировки.
"""

import random


def generate_random_array(size, min_val=1, max_val=10000):
    """Генерация случайного массива."""
    return [random.randint(min_val, max_val) for _ in range(size)]


def generate_sorted_array(size):
    """Генерация отсортированного массива."""
    return list(range(size))


def generate_reversed_array(size):
    """Генерация массива, отсортированного в обратном порядке."""
    return list(range(size, 0, -1))


def generate_almost_sorted_array(size, swap_percent=5):
    """
    Генерация почти отсортированного массива.
    swap_percent - процент элементов для перемешивания.
    """
    arr = generate_sorted_array(size)
    num_swaps = max(1, int(size * swap_percent / 100))
    
    for _ in range(num_swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr


def generate_test_datasets(sizes):
    """
    Генерация наборов данных всех типов для заданных размеров.
    Возвращает словарь: тип_данных -> размер -> массив.
    """
    data_types = {
        'random': generate_random_array,
        'sorted': generate_sorted_array,
        'reversed': generate_reversed_array,
        'almost_sorted': generate_almost_sorted_array
    }
    
    datasets = {data_type: {} for data_type in data_types}
    
    for data_type, generator in data_types.items():
        for size in sizes:
            datasets[data_type][size] = generator(size)
    
    return datasets


if __name__ == "__main__":
    # Пример использования
    sizes = [100, 500, 1000]
    datasets = generate_test_datasets(sizes)
    
    print("Сгенерированные наборы данных:")
    for data_type in datasets:
        print(f"\n{data_type}:")
        for size in sizes:
            arr = datasets[data_type][size]
            print(f"  Размер {size}: первые 5 элементов - {arr[:5]}")