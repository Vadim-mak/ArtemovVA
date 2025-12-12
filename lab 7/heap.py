class MinHeap:
    """Min-Heap (минимальная куча) на основе массива"""
    
    def __init__(self):
        self.heap = []  # O(1) - создание пустого списка
        
    def _parent_index(self, index: int) -> int:
        """Индекс родителя для узла с заданным индексом"""
        return (index - 1) // 2  # O(1) - целочисленное деление
        
    def _left_child_index(self, index: int) -> int:
        """Индекс левого потомка"""
        return 2 * index + 1  # O(1) - умножение и сложение
        
    def _right_child_index(self, index: int) -> int:
        """Индекс правого потомка"""
        return 2 * index + 2  # O(1) - умножение и сложение
        
    def _has_parent(self, index: int) -> bool:
        """Проверка наличия родителя"""
        return self._parent_index(index) >= 0  # O(1)
        
    def _has_left_child(self, index: int) -> bool:
        """Проверка наличия левого потомка"""
        return self._left_child_index(index) < len(self.heap)  # O(1)
        
    def _has_right_child(self, index: int) -> bool:
        """Проверка наличия правого потомка"""
        return self._right_child_index(index) < len(self.heap)  # O(1)
        
    def _swap(self, i: int, j: int) -> None:
        """Обмен элементов по индексам"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]  # O(1)
        
    def _sift_up(self, index: int) -> None:
        """Всплытие элемента (heapify-up)"""
        # O(log n) - подъем от листа к корню
        while self._has_parent(index) and self.heap[index] < self.heap[self._parent_index(index)]:  # O(log n)
            parent_idx = self._parent_index(index)  # O(1)
            self._swap(index, parent_idx)  # O(1)
            index = parent_idx  # O(1)
            
    def _sift_down(self, index: int) -> None:
        """Погружение элемента (heapify-down)"""
        # O(log n) - спуск от корня к листьям
        while self._has_left_child(index):  # O(log n)
            # Находим наименьшего потомка
            smaller_child_idx = self._left_child_index(index)  # O(1)
            if (self._has_right_child(index) and 
                self.heap[self._right_child_index(index)] < self.heap[smaller_child_idx]):  # O(1)
                smaller_child_idx = self._right_child_index(index)  # O(1)
                
            # Если текущий элемент меньше наименьшего потомка - свойство кучи выполнено
            if self.heap[index] < self.heap[smaller_child_idx]:  # O(1)
                break
                
            # Иначе меняем с наименьшим потомком
            self._swap(index, smaller_child_idx)  # O(1)
            index = smaller_child_idx  # O(1)
            
    def insert(self, value: int) -> None:
        """Вставка элемента в кучу"""
        self.heap.append(value)  # O(1) - добавление в конец списка
        self._sift_up(len(self.heap) - 1)  # O(log n) - всплытие
        
    def extract_min(self) -> int:
        """Извлечение минимального элемента (корня)"""
        if len(self.heap) == 0:  # O(1)
            raise IndexError("Куча пуста")
            
        # Сохраняем минимальный элемент
        min_value = self.heap[0]  # O(1)
        
        # Заменяем корень последним элементом
        last_value = self.heap.pop()  # O(1) - удаление последнего элемента
        if len(self.heap) > 0:  # O(1)
            self.heap[0] = last_value  # O(1)
            self._sift_down(0)  # O(log n) - погружение
            
        return min_value  # O(1)
        
    def peek(self) -> int:
        """Получение минимального элемента без удаления"""
        if len(self.heap) == 0:  # O(1)
            raise IndexError("Куча пуста")
        return self.heap[0]  # O(1)
        
    def build_heap(self, array: list) -> None:
        """Построение кучи из произвольного массива (алгоритм Флойда)"""
        self.heap = array[:]  # O(n) - копирование массива
        
        # Начинаем с последнего нелистового узла
        # O(n) - каждый sift_down занимает O(log n), но общая сложность O(n)
        for i in range(len(self.heap) // 2 - 1, -1, -1):  # O(n/2) итераций
            self._sift_down(i)  # O(log n) каждая
            
    def __len__(self) -> int:
        """Размер кучи"""
        return len(self.heap)  # O(1)
        
    def is_empty(self) -> bool:
        """Проверка на пустоту"""
        return len(self.heap) == 0  # O(1)