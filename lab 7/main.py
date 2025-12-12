from heap import MinHeap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue


def demonstrate_heap_basics():
    """Демонстрация основных операций с кучей"""
    print("Лабораторная работа 7: Кучи (Heaps)")
    print("=" * 60)
    
    print("1. Создание и базовые операции с min-heap")
    print("-" * 40)
    
    heap = MinHeap()
    
    # Вставка элементов
    values = [10, 5, 15, 3, 7, 12, 20]
    print("Вставка значений:", values)
    for value in values:
        heap.insert(value)
        print(f"  Вставлено: {value}, текущий минимум: {heap.peek()}")
    
    print(f"\nТекущий размер кучи: {len(heap)}")
    print(f"Минимальный элемент: {heap.peek()}")
    
    # Извлечение элементов
    print("\nИзвлечение элементов в порядке возрастания:")
    while not heap.is_empty():
        min_val = heap.extract_min()
        print(f"  Извлечено: {min_val}")
    
    print(f"\nКуча пуста: {heap.is_empty()}")


def demonstrate_heapsort():
    """Демонстрация сортировки кучей"""
    print("\n\n2. Сортировка кучей (HeapSort)")
    print("-" * 40)
    
    # Тестовый массив
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", array)
    
    # Сортировка с использованием дополнительной памяти
    sorted_array = heapsort(array)
    print("Отсортированный массив (HeapSort):", sorted_array)
    
    # In-place сортировка
    array_copy = array[:]
    heapsort_inplace(array_copy)
    print("Отсортированный массив (in-place):", array_copy)


def demonstrate_priority_queue():
    """Демонстрация очереди с приоритетом"""
    print("\n\n3. Очередь с приоритетом на основе кучи")
    print("-" * 40)
    
    pq = PriorityQueue()
    
    # Моделирование системы задач
    tasks = [
        ("Отправить отчет", 2),
        ("Срочный звонок", 1),  # Высший приоритет
        ("Проверить почту", 3),
        ("Встреча с клиентом", 2),
        ("Планирование", 4)
    ]
    
    print("Добавление задач в очередь:")
    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"  Добавлено: '{task}' (приоритет: {priority})")
    
    print(f"\nРазмер очереди: {len(pq)}")
    print(f"Следующая задача: '{pq.peek()}'")
    
    print("\nОбработка задач по приоритету:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"  Выполняется: '{task}'")


def demonstrate_build_heap():
    """Демонстрация различных методов построения кучи"""
    print("\n\n4. Методы построения кучи")
    print("-" * 40)
    
    array = [3, 9, 2, 1, 4, 5, 7, 8, 6]
    
    print("Исходный массив:", array)
    
    # Метод 1: Последовательная вставка
    heap1 = MinHeap()
    for value in array:
        heap1.insert(value)
    print("\nКуча после последовательной вставки:")
    print("  Минимум:", heap1.peek())
    print("  Структура:", heap1.heap)
    
    # Метод 2: BuildHeap
    heap2 = MinHeap()
    heap2.build_heap(array)
    print("\nКуча после build_heap:")
    print("  Минимум:", heap2.peek())
    print("  Структура:", heap2.heap)


def run_performance_tests():
    """Запуск тестов производительности"""
    print("\n" + "=" * 60)
    print("5. Анализ производительности")
    print("=" * 60)
    
    # Импортируем здесь, чтобы избежать циклических импортов
    import performance_analysis
    
    print("\nИзмерение времени операций кучи")
    print("-" * 40)
    performance_analysis.measure_heap_operations()
    
    print("\nСравнение методов построения кучи")
    print("-" * 40)
    performance_analysis.compare_heap_construction()
    
    print("\nСравнение алгоритмов сортировки")
    print("-" * 40)
    performance_analysis.compare_sorting_algorithms()
    
    print("\nТестирование очереди с приоритетом")
    print("-" * 40)
    performance_analysis.test_priority_queue()
    
    print("\nТекстовая визуализация кучи")
    print("-" * 40)
    performance_analysis.visualize_heap()


def main():
    """Основная функция программы"""
    demonstrate_heap_basics()
    demonstrate_heapsort()
    demonstrate_priority_queue()
    demonstrate_build_heap()
    run_performance_tests()
    
    print("\n" + "=" * 60)
    print("Выводы:")
    print("-" * 60)
    print("1. Min-heap обеспечивает O(log n) для вставки и извлечения")
    print("2. BuildHeap метод (O(n)) эффективнее последовательной вставки (O(n log n))")
    print("3. HeapSort имеет сложность O(n log n) во всех случаях")
    print("4. Очередь с приоритетом на основе кучи эффективна для задач с динамическими приоритетами")
    print("5. In-place HeapSort не требует дополнительной памяти")


if __name__ == "__main__":
    main()