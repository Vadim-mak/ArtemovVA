from heap import MinHeap

def heapsort(array: list) -> list:
    """Сортировка кучей (HeapSort)"""
    # Создаем кучу из массива
    heap = MinHeap()  # O(1)
    heap.build_heap(array)  # O(n)
    
    # Извлекаем элементы в отсортированном порядке
    sorted_array = []  # O(1)
    while len(heap) > 0:  # O(n) итераций
        sorted_array.append(heap.extract_min())  # O(log n) каждая
        
    return sorted_array  # O(1)


def heapsort_inplace(array: list) -> None:
    """In-place сортировка кучей (без дополнительной памяти)"""
    def _sift_down(arr, n, i):
        """Вспомогательная функция для погружения"""
        largest = i  # O(1)
        left = 2 * i + 1  # O(1)
        right = 2 * i + 2  # O(1)
        
        if left < n and arr[left] > arr[largest]:  # O(1)
            largest = left
            
        if right < n and arr[right] > arr[largest]:  # O(1)
            largest = right
            
        if largest != i:  # O(1)
            arr[i], arr[largest] = arr[largest], arr[i]  # O(1)
            _sift_down(arr, n, largest)  # O(log n) рекурсия
            
    n = len(array)  # O(1)
    
    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):  # O(n) итераций
        _sift_down(array, n, i)  # O(log n) каждая
        
    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):  # O(n) итераций
        array[0], array[i] = array[i], array[0]  # O(1)
        _sift_down(array, i, 0)  # O(log n) каждая