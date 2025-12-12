import time
import random
from heap import MinHeap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue

def measure_heap_operations():
    """Измерение времени основных операций кучи"""
    print("Измерение времени операций кучи")
    print("=" * 60)
    
    sizes = [100, 500, 1000, 5000, 10000]
    
    print(f"{'Размер':<10} {'Вставка (мс)':<15} {'Извлечение (мс)':<18} {'Peek (мс)':<15}")
    print("-" * 60)
    
    for size in sizes:
        heap = MinHeap()
        
        # Измерение времени вставки
        start = time.perf_counter()
        for i in range(size):
            heap.insert(random.randint(1, 10000))
        insert_time = (time.perf_counter() - start) * 1000
        
        # Измерение времени peek
        start = time.perf_counter()
        for _ in range(100):
            heap.peek()
        peek_time = (time.perf_counter() - start) * 1000
        
        # Измерение времени извлечения
        start = time.perf_counter()
        for _ in range(size):
            heap.extract_min()
        extract_time = (time.perf_counter() - start) * 1000
        
        print(f"{size:<10} {insert_time:<15.4f} {extract_time:<18.4f} {peek_time:<15.4f}")


def compare_heap_construction():
    """Сравнение методов построения кучи"""
    print("\n\nСравнение методов построения кучи")
    print("=" * 60)
    
    sizes = [1000, 5000, 10000, 50000]
    
    print(f"{'Размер':<10} {'Посл. вставка (мс)':<20} {'BuildHeap (мс)':<20} {'Отношение':<15}")
    print("-" * 60)
    
    for size in sizes:
        array = [random.randint(1, 100000) for _ in range(size)]
        
        # Метод последовательной вставки
        heap1 = MinHeap()
        start = time.perf_counter()
        for value in array:
            heap1.insert(value)
        sequential_time = (time.perf_counter() - start) * 1000
        
        # Метод build_heap
        heap2 = MinHeap()
        start = time.perf_counter()
        heap2.build_heap(array)
        buildheap_time = (time.perf_counter() - start) * 1000
        
        ratio = sequential_time / buildheap_time if buildheap_time > 0 else 0
        
        print(f"{size:<10} {sequential_time:<20.4f} {buildheap_time:<20.4f} {ratio:<15.2f}")


def compare_sorting_algorithms():
    """Сравнение алгоритмов сортировки"""
    print("\n\nСравнение алгоритмов сортировки")
    print("=" * 60)
    
    sizes = [100, 500, 1000, 5000]
    
    print(f"{'Размер':<10} {'HeapSort (мс)':<20} {'QuickSort (мс)':<20} {'MergeSort (мс)':<20}")
    print("-" * 60)
    
    for size in sizes:
        array = [random.randint(1, 10000) for _ in range(size)]
        
        # HeapSort
        arr_copy = array[:]
        start = time.perf_counter()
        heapsort(arr_copy)
        heapsort_time = (time.perf_counter() - start) * 1000
        
        # QuickSort (встроенная)
        arr_copy = array[:]
        start = time.perf_counter()
        sorted(arr_copy)
        quicksort_time = (time.perf_counter() - start) * 1000
        
        # MergeSort (реализация)
        arr_copy = array[:]
        start = time.perf_counter()
        merge_sort(arr_copy)
        mergesort_time = (time.perf_counter() - start) * 1000
        
        print(f"{size:<10} {heapsort_time:<20.4f} {quicksort_time:<20.4f} {mergesort_time:<20.4f}")


def merge_sort(arr):
    """Реализация сортировки слиянием для сравнения"""
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def test_priority_queue():
    """Тестирование очереди с приоритетом"""
    print("\n\nТестирование очереди с приоритетом")
    print("=" * 60)
    
    pq = PriorityQueue()
    
    # Добавление элементов с приоритетами
    tasks = [
        ("Задача 1", 3),
        ("Задача 2", 1),  # Высший приоритет
        ("Задача 3", 5),
        ("Задача 4", 2),
        ("Задача 5", 4)
    ]
    
    print("Добавление задач:")
    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"  Добавлено: {task} (приоритет: {priority})")
    
    print("\nИзвлечение задач по приоритету:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"  Выполняется: {task}")


def visualize_heap():
    """Текстовая визуализация кучи"""
    print("\n\nТекстовая визуализация кучи")
    print("=" * 60)
    
    heap = MinHeap()
    values = [10, 20, 15, 30, 40, 50, 25]
    
    print("Построение кучи из значений:", values)
    heap.build_heap(values)
    
    print("\nСтруктура кучи:")
    print_heap_structure(heap.heap)
    
    print("\nИзвлечение минимальных элементов:")
    for i in range(3):
        min_val = heap.extract_min()
        print(f"  Извлечено: {min_val}")
        print(f"  Новая структура кучи:")
        print_heap_structure(heap.heap)
        print()


def print_heap_structure(heap):
    """Печать структуры кучи в виде дерева"""
    if not heap:
        print("  (пусто)")
        return
        
    def print_level(node_idx, level, prefix):
        if node_idx >= len(heap):
            return
            
        value = heap[node_idx]
        indent = "  " * level
        
        if level == 0:
            print(f"{indent}{value} (корень)")
        else:
            print(f"{indent}{prefix} {value}")
            
        # Рекурсивно печатаем потомков
        print_level(2 * node_idx + 1, level + 1, "├── L:")
        print_level(2 * node_idx + 2, level + 1, "└── R:")
    
    print_level(0, 0, "")


if __name__ == "__main__":
    measure_heap_operations()
    compare_heap_construction()
    compare_sorting_algorithms()
    test_priority_queue()
    visualize_heap()