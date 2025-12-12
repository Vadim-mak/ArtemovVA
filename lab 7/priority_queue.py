from heap import MinHeap

class PriorityQueue:
    """Очередь с приоритетом на основе min-heap"""
    
    def __init__(self):
        self.heap = MinHeap()  # O(1) - создание кучи
        
    def enqueue(self, item, priority: int) -> None:
        """Добавление элемента с приоритетом"""
        # В min-heap меньший приоритет означает более высокий приоритет
        self.heap.insert((priority, item))  # O(log n)
        
    def dequeue(self):
        """Извлечение элемента с наивысшим приоритетом"""
        if self.heap.is_empty():  # O(1)
            raise IndexError("Очередь пуста")
            
        priority, item = self.heap.extract_min()  # O(log n)
        return item  # O(1)
        
    def peek(self):
        """Просмотр элемента с наивысшим приоритетом без удаления"""
        if self.heap.is_empty():  # O(1)
            raise IndexError("Очередь пуста")
            
        priority, item = self.heap.peek()  # O(1)
        return item  # O(1)
        
    def is_empty(self) -> bool:
        """Проверка на пустоту"""
        return self.heap.is_empty()  # O(1)
        
    def __len__(self) -> int:
        """Размер очереди"""
        return len(self.heap)  # O(1)