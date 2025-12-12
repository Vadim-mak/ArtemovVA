# Задача: Проверка сбалансированности скобок
def is_balanced_brackets(expression):
    """
    Проверка сбалансированности скобок с использованием стека.
    Сложность: O(n), где n - длина строки.
    """
    stack = []  # O(1) - создание стека (списка)
    
    # Проходим по каждому символу в выражении
    for char in expression:  # O(n) - цикл по всем символам
        if char in "([{":  # O(1) - проверка открывающей скобки
            stack.append(char)  # O(1) - добавление в стек
        elif char in ")]}":  # O(1) - проверка закрывающей скобки
            if not stack:  # O(1) - проверка пустоты стека
                return False  # O(1) - несбалансированные скобки
            
            # Получаем последнюю открывающую скобку
            last_open = stack.pop()  # O(1) - удаление из стека
            
            # Проверяем соответствие скобок
            if (last_open == '(' and char != ')') or \
               (last_open == '[' and char != ']') or \
               (last_open == '{' and char != '}'):  # O(1) - проверка
                return False  # O(1) - несбалансированные скобки
    
    # Если стек пуст, все скобки сбалансированы
    return len(stack) == 0  # O(1) - проверка пустоты стека


# Тестирование функции
if __name__ == "__main__":
    # Тестовые случаи
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("((()))", True),
        ("((())", False)
    ]
    
    print("Тестирование проверки сбалансированности скобок:")
    print("-" * 50)
    
    for expression, expected in test_cases:
        result = is_balanced_brackets(expression)
        status = "✓" if result == expected else "✗"
        print(f"{status} Выражение: '{expression}'")
        print(f"  Ожидалось: {expected}, Получено: {result}")
        print()