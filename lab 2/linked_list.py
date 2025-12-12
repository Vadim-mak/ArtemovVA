class Node:
    """Узел связного списка."""
    def __init__(self, data):
        self.data = data  # O(1) - создание узла
        self.next = None  # O(1) - инициализация ссылки


class LinkedList:
    """Односвязный список."""
    def __init__(self):
        self.head = None  # O(1) - инициализация головы списка

    def insert_at_start(self, data):
        """Вставка в начало списка. Сложность: O(1)."""
        new_node = Node(data)  # O(1) - создание нового узла
        new_node.next = self.head  # O(1) - установка ссылки
        self.head = new_node  # O(1) - обновление головы

    def delete_from_start(self):
        """Удаление из начала списка. Сложность: O(1)."""
        if self.head is None:  # O(1) - проверка на пустоту
            return None
        removed_data = self.head.data  # O(1) - сохранение данных
        self.head = self.head.next  # O(1) - перемещение головы
        return removed_data  # O(1) - возврат удаленных данных

    def traversal(self):
        """Обход списка. Сложность: O(n)."""
        current = self.head  # O(1) - начальный элемент
        elements = []  # O(1) - список для хранения элементов
        while current:  # O(n) - цикл по всем элементам
            elements.append(current.data)  # O(1) - добавление элемента
            current = current.next  # O(1) - переход к следующему
        return elements  # O(1) - возврат списка элементов

    def __str__(self):
        """Строковое представление списка. Сложность: O(n)."""
        return " -> ".join(map(str, self.traversal()))  # O(n) - преобразование в строку