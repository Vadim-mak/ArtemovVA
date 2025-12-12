import time
import random
import string
from hash_table_chaining import HashTableChaining

def generate_random_key(length: int = 5) -> str:
    """Генерация случайного ключа"""
    return ''.join(random.choices(string.ascii_letters, k=length))  # O(k)

def measure_performance():
    """Измерение производительности хеш-таблицы"""
    # Создаем хеш-таблицу
    ht = HashTableChaining(size=100)  # O(n)
    
    # Вставляем 1000 элементов
    insert_times = []
    print("Вставка 1000 элементов...")
    for i in range(1000):
        key = generate_random_key()  # O(k)
        value = i
        
        start = time.perf_counter()  # O(1)
        ht.insert(key, value)  # O(1) в среднем случае
        end = time.perf_counter()  # O(1)
        
        insert_times.append((end - start) * 1000)  # мс
        
    # Ищем 100 элементов
    search_times = []
    print("Поиск 100 элементов...")
    # Берем первые 100 ключей для поиска
    test_keys = [generate_random_key() for _ in range(100)]  # O(100*k)
    for key in test_keys:
        start = time.perf_counter()  # O(1)
        ht.get(key)  # O(1) в среднем случае
        end = time.perf_counter()  # O(1)
        
        search_times.append((end - start) * 1000)  # мс
        
    # Выводим результаты
    print("\nРезультаты производительности:")
    print("-" * 40)
    print(f"Среднее время вставки: {sum(insert_times)/len(insert_times):.6f} мс")
    print(f"Минимальное время вставки: {min(insert_times):.6f} мс")
    print(f"Максимальное время вставки: {max(insert_times):.6f} мс")
    print()
    print(f"Среднее время поиска: {sum(search_times)/len(search_times):.6f} мс")
    print(f"Минимальное время поиска: {min(search_times):.6f} мс")
    print(f"Максимальное время поиска: {max(search_times):.6f} мс")
    
    # Тестируем удаление
    remove_times = []
    print("\nУдаление 50 элементов...")
    for key in test_keys[:50]:  # Удаляем 50 элементов
        start = time.perf_counter()
        ht.remove(key)
        end = time.perf_counter()
        remove_times.append((end - start) * 1000)
        
    print(f"Среднее время удаления: {sum(remove_times)/len(remove_times):.6f} мс")
    
    # Дополнительная статистика
    print("\n" + "=" * 40)
    print("Дополнительная статистика:")
    
    # Считаем количество коллизий
    collisions = 0
    max_chain_length = 0
    for bucket in ht.table:
        chain_length = len(bucket)
        if chain_length > 1:
            collisions += chain_length - 1
        if chain_length > max_chain_length:
            max_chain_length = chain_length
    
    print(f"Общее количество коллизий: {collisions}")
    print(f"Максимальная длина цепочки: {max_chain_length}")
    print(f"Коэффициент заполнения: {1000 / ht.size:.2f}")