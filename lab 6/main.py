from binary_search_tree import BinarySearchTree
from tree_analysis import test_bst_operations, analyze_trees


def demonstrate_bst():
    """Демонстрация работы бинарного дерева поиска"""
    print("Лабораторная работа 6: Бинарные деревья поиска")
    print("=" * 50)
    
    # Создание дерева
    bst = BinarySearchTree()
    
    # Вставка значений
    print("1. Вставка значений в дерево:")
    values = [50, 30, 20, 40, 70, 60, 80]
    for value in values:
        bst.insert(value)
        print(f"   Вставлено: {value}")
    
    # Поиск значений
    print("\n2. Поиск значений в дереве:")
    search_values = [30, 45, 60, 100]
    for value in search_values:
        found = bst.search(value)
        print(f"   Поиск {value}: {'найден' if found else 'не найден'}")
    
    # Обход дерева
    print("\n3. Обход дерева (in-order):")
    traversal_result = bst.inorder_traversal()
    print(f"   Результат: {traversal_result}")
    
    print("\n4. Демонстрация свойств BST:")
    print("   - In-order обход возвращает отсортированные значения")
    print("   - Левые потомки меньше родителя")
    print("   - Правые потомки больше родителя")


def simple_performance_test():
    """Простой тест производительности"""
    print("\n" + "=" * 50)
    print("Простой тест производительности")
    print("-" * 30)
    
    import time
    
    # Тест сбалансированного дерева
    bst_balanced = BinarySearchTree()
    balanced_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    
    start = time.perf_counter()
    for value in balanced_values:
        bst_balanced.insert(value)
    balanced_insert_time = (time.perf_counter() - start) * 1000
    
    # Тест поиска в сбалансированном дереве
    start = time.perf_counter()
    for value in balanced_values:
        bst_balanced.search(value)
    balanced_search_time = (time.perf_counter() - start) * 1000
    
    # Тест вырожденного дерева
    bst_degenerate = BinarySearchTree()
    degenerate_values = list(range(15))  # [0, 1, 2, ..., 14]
    
    start = time.perf_counter()
    for value in degenerate_values:
        bst_degenerate.insert(value)
    degenerate_insert_time = (time.perf_counter() - start) * 1000
    
    # Тест поиска в вырожденном дереве
    start = time.perf_counter()
    for value in degenerate_values:
        bst_degenerate.search(value)
    degenerate_search_time = (time.perf_counter() - start) * 1000
    
    print(f"Сбалансированное дерево (15 элементов):")
    print(f"  Время вставки: {balanced_insert_time:.4f} мс")
    print(f"  Время поиска: {balanced_search_time:.4f} мс")
    
    print(f"\nВырожденное дерево (15 элементов):")
    print(f"  Время вставки: {degenerate_insert_time:.4f} мс")
    print(f"  Время поиска: {degenerate_search_time:.4f} мс")
    
    print("\nОтношение времен:")
    print(f"  Вставка (вырожденное/сбалансированное): {degenerate_insert_time/balanced_insert_time:.2f}")
    print(f"  Поиск (вырожденное/сбалансированное): {degenerate_search_time/balanced_search_time:.2f}")


if __name__ == "__main__":
    demonstrate_bst()
    simple_performance_test()
    print("\n" + "=" * 50)
    print("Выводы:")
    print("- Сбалансированное дерево обеспечивает O(log n) время операций")
    print("- Вырожденное дерево вырождается в связный список с O(n) временем")
    print("- Время операций в вырожденном дереве растет линейно с размером")