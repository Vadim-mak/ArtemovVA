# memoization.py
# Мемоизированная версия Фибоначчи и простая функция для замера времени сравнений.

import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    """
    Рекурсия с мемоизацией (LRU cache) для чисел Фибоначчи.
    Сложность времени: O(n)
    Память: O(n) для кеша
    """
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

def measure_time(func, arg, runs=3):
    """
    Измеряет среднее время выполнения func(arg) в миллисекундах.
    """
    total = 0.0
    for _ in range(runs):
        t0 = time.perf_counter()
        res = func(arg)
        t1 = time.perf_counter()
        total += (t1 - t0)
    avg_ms = (total / runs) * 1000.0
    return avg_ms, res

if __name__ == "__main__":
    n = 30
    t_naive, _ = measure_time(__import__("recursion").fib_naive, n, runs=1)
    t_memo, _ = measure_time(fib_memo, n, runs=3)
    print(f"n={n}: naive time ≈ {t_naive:.2f} ms (1 run)")
    print(f"n={n}: memo  time ≈ {t_memo:.2f} ms (avg {3} runs)")
