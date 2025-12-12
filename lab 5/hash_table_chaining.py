from hash_functions import simple_hash

class HashTableChaining:
    """Хеш-таблица с методом цепочек"""
    
    def __init__(self, size: int = 10):
        self.size = size  # O(1) - присваивание
        self.table = [[] for _ in range(size)]  # O(n) - создание n списков
        
    def _hash(self, key: str) -> int:
        """Вычисление хеша для ключа"""
        return simple_hash(key) % self.size  # O(k) где k - длина ключа
        
    def insert(self, key: str, value) -> None:
        """Вставка пары ключ-значение"""
        index = self._hash(key)  # O(k)
        bucket = self.table[index]  # O(1) - доступ по индексу
        
        # Проверка, не существует ли уже такой ключ
        for i, (k, v) in enumerate(bucket):  # O(m) где m - размер цепочки
            if k == key:
                bucket[i] = (key, value)  # O(1) - обновление
                return
                
        bucket.append((key, value))  # O(1) - добавление в конец списка
        
    def get(self, key: str):
        """Получение значения по ключу"""
        index = self._hash(key)  # O(k)
        bucket = self.table[index]  # O(1)
        
        for k, v in bucket:  # O(m)
            if k == key:
                return v  # O(1) - возврат значения
        return None  # O(1)
        
    def remove(self, key: str) -> bool:
        """Удаление пары ключ-значение"""
        index = self._hash(key)  # O(k)
        bucket = self.table[index]  # O(1)
        
        for i, (k, v) in enumerate(bucket):  # O(m)
            if k == key:
                del bucket[i]  # O(m) в худшем случае (удаление из середины списка)
                return True
        return False