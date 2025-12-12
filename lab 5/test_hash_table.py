def test_hash_table():
    """Тестирование хеш-таблицы"""
    ht = HashTableChaining(size=5)
    
    # Тест 1: Вставка и получение
    print("Тест 1: Вставка и получение")
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("cherry", 30)
    
    assert ht.get("apple") == 10
    assert ht.get("banana") == 20
    assert ht.get("cherry") == 30
    print("✓ Тест 1 пройден")
    
    # Тест 2: Обновление значения
    print("\nТест 2: Обновление значения")
    ht.insert("apple", 100)  # Обновляем значение
    assert ht.get("apple") == 100
    print("✓ Тест 2 пройден")
    
    # Тест 3: Удаление
    print("\nТест 3: Удаление")
    assert ht.remove("banana") == True
    assert ht.get("banana") == None
    print("✓ Тест 3 пройден")
    
    # Тест 4: Коллизии (используем маленький размер для демонстрации)
    print("\nТест 4: Обработка коллизий")
    small_ht = HashTableChaining(size=2)
    
    # Эти ключи могут давать одинаковый хеш при размере 2
    small_ht.insert("a", 1)
    small_ht.insert("c", 3)
    small_ht.insert("e", 5)
    
    assert small_ht.get("a") == 1
    assert small_ht.get("c") == 3
    assert small_ht.get("e") == 5
    print("✓ Тест 4 пройден")
    
    print("\nВсе тесты пройдены успешно!")

if __name__ == "__main__":
    test_hash_table()