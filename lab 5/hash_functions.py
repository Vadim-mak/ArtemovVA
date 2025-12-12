def simple_hash(key: str) -> int:
    """Простая хеш-функция: сумма кодов символов"""
    h = 0
    for char in key:
        h += ord(char)  # O(1) - получение кода символа
    return h  # O(1)


def polynomial_hash(key: str, p: int = 31, m: int = 10**9 + 7) -> int:
    """Полиномиальная хеш-функция"""
    h = 0
    power = 1
    for char in key:
        h = (h + (ord(char) * power)) % m  # O(1) - умножение и сложение
        power = (power * p) % m  # O(1) - умножение
    return h  # O(1)