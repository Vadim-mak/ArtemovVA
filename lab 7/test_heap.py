import unittest
from heap import MinHeap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue


class TestMinHeap(unittest.TestCase):
    """Тесты для MinHeap"""
    
    def setUp(self):
        self.heap = MinHeap()
    
    def test_insert_and_peek(self):
        """Тест вставки и просмотра минимума"""
        self.heap.insert(5)
        self.assertEqual(self.heap.peek(), 5)
        
        self.heap.insert(3)
        self.assertEqual(self.heap.peek(), 3)
        
        self.heap.insert(7)
        self.assertEqual(self.heap.peek(), 3)
    
    def test_extract_min(self):
        """Тест извлечения минимума"""
        values = [5, 3, 7, 1, 9]
        for v in values:
            self.heap.insert(v)
        
        self.assertEqual(self.heap.extract_min(), 1)
        self.assertEqual(self.heap.extract_min(), 3)
        self.assertEqual(self.heap.extract_min(), 5)
        self.assertEqual(self.heap.extract_min(), 7)
        self.assertEqual(self.heap.extract_min(), 9)
        
        with self.assertRaises(IndexError):
            self.heap.extract_min()
    
    def test_build_heap(self):
        """Тест построения кучи из массива"""
        array = [9, 5, 3, 7, 1, 8, 2]
        self.heap.build_heap(array)
        
        self.assertEqual(self.heap.extract_min(), 1)
        self.assertEqual(self.heap.extract_min(), 2)
        self.assertEqual(self.heap.extract_min(), 3)
    
    def test_heap_property(self):
        """Проверка свойства кучи"""
        import random
        values = [random.randint(1, 100) for _ in range(100)]
        
        # Метод 1: последовательная вставка
        heap1 = MinHeap()
        for v in values:
            heap1.insert(v)
        
        # Проверяем свойство кучи
        for i in range(len(heap1.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < len(heap1.heap):
                self.assertTrue(heap1.heap[i] <= heap1.heap[left])
            
            if right < len(heap1.heap):
                self.assertTrue(heap1.heap[i] <= heap1.heap[right])
        
        # Метод 2: build_heap
        heap2 = MinHeap()
        heap2.build_heap(values)
        
        for i in range(len(heap2.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < len(heap2.heap):
                self.assertTrue(heap2.heap[i] <= heap2.heap[left])
            
            if right < len(heap2.heap):
                self.assertTrue(heap2.heap[i] <= heap2.heap[right])


class TestHeapSort(unittest.TestCase):
    """Тесты для HeapSort"""
    
    def test_heapsort(self):
        """Тест сортировки кучей"""
        import random
        for _ in range(10):  # 10 случайных тестов
            array = [random.randint(1, 100) for _ in range(50)]
            sorted_array = heapsort(array)
            
            # Проверяем сортировку
            self.assertEqual(sorted_array, sorted(array))
    
    def test_heapsort_inplace(self):
        """Тест in-place сортировки кучей"""
        import random
        for _ in range(10):
            array = [random.randint(1, 100) for _ in range(50)]
            array_copy = array[:]
            heapsort_inplace(array_copy)
            
            self.assertEqual(array_copy, sorted(array))


class TestPriorityQueue(unittest.TestCase):
    """Тесты для очереди с приоритетом"""
    
    def test_enqueue_dequeue(self):
        """Тест добавления и извлечения из очереди"""
        pq = PriorityQueue()
        
        pq.enqueue("Task A", 3)
        pq.enqueue("Task B", 1)  # Высший приоритет
        pq.enqueue("Task C", 2)
        
        self.assertEqual(pq.dequeue(), "Task B")  # Приоритет 1
        self.assertEqual(pq.dequeue(), "Task C")  # Приоритет 2
        self.assertEqual(pq.dequeue(), "Task A")  # Приоритет 3
        
        self.assertTrue(pq.is_empty())
    
    def test_peek(self):
        """Тест просмотра без удаления"""
        pq = PriorityQueue()
        
        pq.enqueue("Task A", 2)
        pq.enqueue("Task B", 1)
        
        self.assertEqual(pq.peek(), "Task B")  # Не удаляет
        self.assertEqual(pq.peek(), "Task B")  # Все еще там
        self.assertEqual(pq.dequeue(), "Task B")  # Теперь удаляет
    
    def test_empty_queue(self):
        """Тест пустой очереди"""
        pq = PriorityQueue()
        
        self.assertTrue(pq.is_empty())
        self.assertEqual(len(pq), 0)
        
        with self.assertRaises(IndexError):
            pq.dequeue()
        
        with self.assertRaises(IndexError):
            pq.peek()


if __name__ == "__main__":
    unittest.main(verbosity=2)