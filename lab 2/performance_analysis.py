import timeit

# Определяем класс LinkedList прямо здесь, чтобы избежать проблем с импортом
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_from_start(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

def main():
    print("=" * 60)
    print("Лабораторная работа 2: Замеры производительности")
    print("=" * 60)
    
    # 1. Замер времени вставки в LinkedList
    print("\n1. Замер времени вставки 100 элементов в начало LinkedList:")
    
    def test_linkedlist_insert():
        ll = LinkedList()
        for i in range(100):
            ll.insert_at_start(i)
    
    linkedlist_time = timeit.timeit(
        test_linkedlist_insert,
        number=1000  # выполним 1000 раз для более точного измерения
    )
    
    print(f"   Время выполнения 1000 раз: {linkedlist_time:.4f} секунд")
    print(f"   Среднее время одной операции: {linkedlist_time/1000:.6f} секунд")
    
    # 2. Замер времени вставки в обычный list
    print("\n2. Замер времени вставки 100 элементов в начало обычного списка (list):")
    
    def test_list_insert():
        lst = []  # создаем новый список каждый раз
        for i in range(100):
            lst.insert(0, i)  # вставка в начало
    
    list_time = timeit.timeit(
        test_list_insert,
        number=1000  # выполним 1000 раз
    )
    
    print(f"   Время выполнения 1000 раз: {list_time:.4f} секунд")
    print(f"   Среднее время одной операции: {list_time/1000:.6f} секунд")
    
    # 3. Сравнение
    print("\n3. Сравнение производительности:")
    print(f"   LinkedList: {linkedlist_time:.4f} сек")
    print(f"   list:       {list_time:.4f} сек")
    
    if linkedlist_time > 0:
        ratio = list_time / linkedlist_time
        print(f"   list медленнее в {ratio:.2f} раз")
    
    # 4. Демонстрация работы LinkedList
    print("\n4. Демонстрация работы LinkedList:")
    
    ll = LinkedList()
    print("   Создаем список и добавляем элементы 1, 2, 3:")
    
    for i in [1, 2, 3]:
        ll.insert_at_start(i)
    
    # Выводим содержимое списка
    elements = []
    current = ll.head
    while current:
        elements.append(str(current.data))
        current = current.next
    
    print(f"   Содержимое: {' -> '.join(elements)}")
    
    # Удаляем элемент
    removed = ll.delete_from_start()
    print(f"   Удален элемент: {removed}")
    
    # Выводим оставшееся содержимое
    elements = []
    current = ll.head
    while current:
        elements.append(str(current.data))
        current = current.next
    
    print(f"   Осталось: {' -> '.join(elements)}")
    
    print("\n" + "=" * 60)
    print("Замеры производительности завершены успешно!")
    print("=" * 60)

if __name__ == "__main__":
    main()