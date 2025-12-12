import time
import random
import sys
from binary_search_tree import BinarySearchTree

# Увеличиваем лимит рекурсии для больших деревьев
sys.setrecursionlimit(10000)

def generate_balanced_tree(size: int) -> BinarySearchTree:
    """Генерация сбалансированного дерева (случайные значения)"""
    bst = BinarySearchTree()  # O(1)
    # Используем больше значений для уменьшения вероятности дубликатов
    values = random.sample(range(size * 10), size)  # O(n) - генерация уникальных значений
    for value in values:  # O(n) вставок
        bst.insert(value)  # O(log n) каждая вставка
    return bst  # O(1)


def generate_degenerate_tree(size: int) -> BinarySearchTree:
    """Генерация вырожденного дерева (отсортированные значения)"""
    bst = BinarySearchTree()  # O(1)
    # Вставляем значения в порядке возрастания для создания вырожденного дерева
    for i in range(size):  # O(n) итераций
        bst.insert(i)  # O(n) каждая вставка в худшем случае
    return bst  # O(1)


def measure_search_time(tree: BinarySearchTree, search_values: list) -> float:
    """Измерение времени поиска значений в дереве"""
    start_time = time.perf_counter()  # O(1)
    
    for value in search_values:  # O(k) где k - количество поисков
        tree.search(value)  # O(log n) в среднем, O(n) в худшем
    
    end_time = time.perf_counter()  # O(1)
    return (end_time - start_time) * 1000  # O(1) - конвертация в мс


def analyze_trees():
    """Анализ производительности сбалансированного и вырожденного деревьев"""
    print("Анализ производительности бинарных деревьев поиска")
    print("=" * 60)
    
    # Уменьшаем размеры для избежания рекурсии
    sizes = [100, 200, 300, 400]  # Более мелкие размеры
    search_count = 50  # Уменьшаем количество поисков
    
    print(f"{'Размер':<10} {'Тип дерева':<20} {'Время поиска (мс)':<20}")
    print("-" * 60)
    
    for size in sizes:  # O(m) где m - количество размеров
        # Сбалансированное дерево
        print(f"Генерация сбалансированного дерева размером {size}...")
        balanced_tree = generate_balanced_tree(size)  # O(n log n)
        search_values = random.sample(range(size * 10), search_count)  # O(k)
        
        balanced_time = measure_search_time(balanced_tree, search_values)  # O(k log n)
        print(f"{size:<10} {'Сбалансированное':<20} {balanced_time:<20.4f}")
        
        # Вырожденное дерево
        print(f"Генерация вырожденного дерева размером {size}...")
        degenerate_tree = generate_degenerate_tree(size)  # O(n²)
        degenerate_time = measure_search_time(degenerate_tree, search_values)  # O(kn)
        print(f"{size:<10} {'Вырожденное':<20} {degenerate_time:<20.4f}")
        print()


def test_bst_operations():
    """Тестирование основных операций BST"""
    print("\nТестирование операций BST")
    print("-" * 40)
    
    bst = BinarySearchTree()  # O(1)
    
    # Вставка значений
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:  # O(n)
        bst.insert(value)  # O(log n)
    
    print("Вставленные значения:", values)
    
    # Поиск значений
    test_values = [30, 45, 70, 100]
    print("\nРезультаты поиска:")
    for value in test_values:  # O(k)
        found = bst.search(value)  # O(log n)
        print(f"  {value}: {'найдено' if found else 'не найдено'}")
    
    # In-order обход (должен вернуть отсортированные значения)
    sorted_values = bst.inorder_traversal()  # O(n)
    print(f"\nIn-order обход (отсортированные): {sorted_values}")
    
    # Проверка правильности сортировки
    is_sorted = all(sorted_values[i] <= sorted_values[i+1] 
                   for i in range(len(sorted_values)-1))  # O(n)
    print(f"Корректность BST: {'Да' if is_sorted else 'Нет'}")


if __name__ == "__main__":
    test_bst_operations()
    print("\n" + "=" * 60)
    analyze_trees()