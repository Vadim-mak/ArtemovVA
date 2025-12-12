import time
from hash_functions import simple_hash, polynomial_hash
from hash_table_chaining import HashTableChaining
from performance_analysis import measure_performance

def main():
    print("Лабораторная работа 5: Хеш-функции и хеш-таблицы")
    print("=" * 50)
    
    # Демонстрация хеш-функций
    print("\n1. Демонстрация хеш-функций:")
    time.sleep(1)
    
    test_strings = ["hello", "world", "python", "algorithm"]
    
    for s in test_strings:
        h1 = simple_hash(s)
        h2 = polynomial_hash(s)
        print(f"'{s}': простая хеш = {h1}, полиномиальная хеш = {h2}")
    
    # Демонстрация работы хеш-таблицы
    print("\n2. Демонстрация работы хеш-таблицы:")
    time.sleep(1)
    
    ht = HashTableChaining(size=5)
    
    # Вставляем несколько значений
    data = [
        ("apple", "фрукт"),
        ("carrot", "овощ"),
        ("dog", "животное"),
        ("house", "здание"),
        ("book", "литература")
    ]
    
    for key, value in data:
        ht.insert(key, value)
        print(f"Вставлено: {key} -> {value}")
    
    # Получаем значения
    print("\nПолучение значений:")
    time.sleep(1)
    
    for key, _ in data:
        value = ht.get(key)
        print(f"{key} -> {value}")
    
    # Удаление
    print("\nУдаление 'dog':")
    time.sleep(1)
    
    if ht.remove("dog"):
        print("Успешно удалено")
    else:
        print("Ключ не найден")
    
    print("Попытка получить 'dog':", ht.get("dog"))
    
    # Измерение производительности
    print("\n3. Измерение производительности:")
    print("-" * 30)
    time.sleep(1)
    measure_performance()

if __name__ == "__main__":
    main()