class TreeNode:
    """Узел бинарного дерева поиска"""
    def __init__(self, value: int):
        self.value = value  # O(1) - присваивание
        self.left = None    # O(1) - присваивание
        self.right = None   # O(1) - присваивание


class BinarySearchTree:
    """Бинарное дерево поиска (BST)"""
    
    def __init__(self):
        self.root = None  # O(1) - инициализация корня
        
    def insert(self, value: int) -> None:
        """Вставка значения в дерево (итеративная версия)"""
        new_node = TreeNode(value)  # O(1) - создание узла
        
        if self.root is None:  # O(1) - проверка
            self.root = new_node  # O(1) - присваивание
            return
        
        current = self.root  # O(1)
        parent = None  # O(1)
        
        while current is not None:  # O(h) где h - высота дерева
            parent = current  # O(1)
            if value < current.value:  # O(1) - сравнение
                current = current.left  # O(1)
            elif value > current.value:  # O(1) - сравнение
                current = current.right  # O(1)
            else:
                # Значение уже существует, ничего не делаем
                return
        
        # Определяем, куда вставить новый узел
        if value < parent.value:  # O(1)
            parent.left = new_node  # O(1)
        else:
            parent.right = new_node  # O(1)
        
    def search(self, value: int) -> bool:
        """Поиск значения в дереве (итеративная версия)"""
        current = self.root  # O(1)
        
        while current is not None:  # O(h)
            if value == current.value:  # O(1)
                return True  # O(1)
            elif value < current.value:  # O(1)
                current = current.left  # O(1)
            else:
                current = current.right  # O(1)
                
        return False  # O(1)
            
    def inorder_traversal(self) -> list:
        """Обход дерева в порядке in-order (левый-корень-правый)"""
        result = []  # O(1) - создание списка
        self._inorder_recursive(self.root, result)  # O(n) - обход всех узлов
        return result  # O(1) - возврат
        
    def _inorder_recursive(self, node: TreeNode, result: list) -> None:
        """Рекурсивный in-order обход"""
        if node is not None:  # O(1) - проверка
            self._inorder_recursive(node.left, result)  # O(n) рекурсия
            result.append(node.value)  # O(1) - добавление в список
            self._inorder_recursive(node.right, result)  # O(n) рекурсия