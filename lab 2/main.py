from linked_list import LinkedList
from task_solutions import is_balanced_brackets

def test_linked_list():
    """Тестирование основных операций связного списка."""
    print("Тестирование связного списка:")
    print("-" * 30)
    
    ll = LinkedList()
    
    # Вставка элементов
    print("1. Вставка элементов в начало:")
    for i in range(5):
        ll.insert_at_start(i)
        print(f"   После вставки {i}: {ll}")
    
    # Обход списка
    print("\n2. Обход списка:")
    print(f"   Элементы: {ll.traversal()}")
    
    # Удаление элементов
    print("\n3. Удаление элементов из начала:")
    for i in range(3):
        removed = ll.delete_from_start()
        print(f"   Удален элемент: {removed}, Список: {ll}")
    
    print()

def test_brackets():
    """Тестирование проверки скобок."""
    print("Тестирование проверки сбалансированности скобок:")
    print("-" * 30)
    
    expressions = [
        ("()", True),
        ("({[]})", True),
        ("({[}])", False),
        ("", True)
    ]
    
    for expr, expected in expressions:
        result = is_balanced_brackets(expr)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{expr}' -> {result} (ожидалось: {expected})")

if __name__ == "__main__":
    test_linked_list()
    print("\n" + "="*50 + "\n")
    test_brackets()