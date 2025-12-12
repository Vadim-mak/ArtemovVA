"""
Тестирование производительности алгоритмов сортировки.
"""

import timeit
import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sorts import (
    bubble_sort, 
    selection_sort, 
    insertion_sort,
    merge_sort,
    quick_sort,
    is_sorted
)
from generate_data import generate_test_datasets


def measure_sorting_time(sort_func, data):
    """
    Измеряет время выполнения функции сортировки.
    Возвращает время в миллисекундах.
    """
    data_copy = data.copy()  # работаем с копией
    start_time = timeit.default_timer()
    sort_func(data_copy)
    end_time = timeit.default_timer()
    return (end_time - start_time) * 1000  # миллисекунды


def run_performance_tests(sizes=None, algorithms=None):
    """
    Запуск тестов производительности.
    """
    if sizes is None:
        sizes = [100, 500, 1000]
    
    if algorithms is None:
        algorithms = [
            ("Пузырьковая", bubble_sort),
            ("Выбором", selection_sort),
            ("Вставками", insertion_sort)
        ]
    
    # Генерация тестовых данных
    print("Генерация тестовых данных...")
    datasets = generate_test_datasets(sizes)
    
    results = {}
    
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ АЛГОРИТМОВ СОРТИРОВКИ")
    print("=" * 70)
    
    # Тестирование на случайных данных
    print("\n1. Случайные данные:")
    print("-" * 70)
    print("{:<15} ".format("Размер"), end="")
    for algo_name, _ in algorithms:
        print("{:<20} ".format(algo_name), end="")
    print()
    print("-" * 70)
    
    for size in sizes:
        print("{:<15} ".format(size), end="")
        data = datasets['random'][size]
        
        for algo_name, algo_func in algorithms:
            time_taken = measure_sorting_time(algo_func, data)
            
            # Проверка корректности
            sorted_data = data.copy()
            algo_func(sorted_data)
            if not is_sorted(sorted_data):
                print(f"\nОшибка: {algo_name} не отсортировала массив размера {size}!")
                return None
            
            if algo_name not in results:
                results[algo_name] = {}
            results[algo_name][size] = time_taken
            
            print("{:<20.4f} ".format(time_taken), end="")
        print()
    
    # Тестирование на отсортированных данных
    print("\n2. Отсортированные данные (размер 1000):")
    print("-" * 70)
    data = datasets['sorted'][1000]
    
    for algo_name, algo_func in algorithms:
        time_taken = measure_sorting_time(algo_func, data)
        print(f"{algo_name}: {time_taken:.4f} мс")
    
    # Тестирование на обратно отсортированных данных
    print("\n3. Обратно отсортированные данные (размер 1000):")
    print("-" * 70)
    data = datasets['reversed'][1000]
    
    for algo_name, algo_func in algorithms:
        time_taken = measure_sorting_time(algo_func, data)
        print(f"{algo_name}: {time_taken:.4f} мс")
    
    return results


def print_summary(results):
    """Вывод сводной информации по результатам тестов."""
    print("\n" + "=" * 70)
    print("СВОДНАЯ ИНФОРМАЦИЯ")
    print("=" * 70)
    
    if not results:
        print("Нет результатов для анализа")
        return
    
    for algo_name in results:
        print(f"\n{algo_name}:")
        for size in sorted(results[algo_name].keys()):
            time_ms = results[algo_name][size]
            print(f"  Размер {size}: {time_ms:.4f} мс")


if __name__ == "__main__":
    # Характеристики ПК (заполнить своими данными)
    pc_info = """
Характеристики ПК для тестирования:
- Процессор: (укажите свой процессор)
- Оперативная память: (укажите объем ОЗУ)
- OC: (укажите операционную систему)
- Python: (укажите версию Python)
"""
    print(pc_info)
    
    # Запуск тестов
    results = run_performance_tests()
    
    if results:
        print_summary(results)
    
    print("\n" + "=" * 70)
    print("Тестирование завершено успешно!")
    print("=" * 70)