"""
Визуализация результатов тестирования сортировок.
"""

import matplotlib.pyplot as plt
import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from performance_test import run_performance_tests


def plot_results(results, sizes):
    """
    Построение графика результатов тестирования.
    """
    if not results:
        print("Нет данных для построения графика")
        return
    
    plt.figure(figsize=(12, 8))
    
    # График для каждого алгоритма
    for algo_name in results:
        times = [results[algo_name].get(size, 0) for size in sizes]
        plt.plot(sizes, times, marker='o', linewidth=2, markersize=8, label=algo_name)
    
    plt.xlabel('Размер массива (элементов)', fontsize=12)
    plt.ylabel('Время выполнения (мс)', fontsize=12)
    plt.title('Сравнение времени выполнения алгоритмов сортировки\n(случайные данные)', fontsize=14, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    plt.tight_layout()
    
    # Сохранение графика
    plt.savefig('sorting_performance.png', dpi=200, bbox_inches='tight')
    print("График сохранен в файл 'sorting_performance.png'")
    
    plt.show()


def main():
    """Основная функция для визуализации."""
    print("Запуск тестов для построения графика...")
    
    sizes = [100, 500, 1000, 2000]
    algorithms = [
        ("Пузырьковая", lambda arr: __import__('sorts').bubble_sort(arr)),
        ("Выбором", lambda arr: __import__('sorts').selection_sort(arr)),
        ("Вставками", lambda arr: __import__('sorts').insertion_sort(arr))
    ]
    
    results = run_performance_tests(sizes, algorithms)
    
    if results:
        plot_results(results, sizes)
    else:
        print("Не удалось получить результаты тестирования")


if __name__ == "__main__":
    # Проверка наличия matplotlib
    try:
        import matplotlib.pyplot as plt
        main()
    except ImportError:
        print("Ошибка: Для построения графиков необходим matplotlib.")
        print("Установите его командой: pip install matplotlib")
        print("Или запустите только performance_test.py для текстовых результатов")