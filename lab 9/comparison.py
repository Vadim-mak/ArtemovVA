import time
import sys
from dynamic_programming import (
    fibonacci_naive,
    fibonacci_memoization,
    fibonacci_tabulation,
    fibonacci_optimized,
    knapsack_01,
    knapsack_01_optimized,
    longest_common_subsequence,
    lcs_with_reconstruction,
    coin_change_min_coins,
    coin_change_ways,
    longest_increasing_subsequence,
    edit_distance,
    matrix_chain_order
)


def compare_fibonacci_methods():
    """Сравнение методов вычисления чисел Фибоначчи"""
    print("Сравнение методов вычисления чисел Фибоначчи")
    print("=" * 60)
    
    test_values = [5, 10, 20, 30, 40]
    
    print(f"{'n':<10} {'Наивный (мс)':<15} {'Мемоизация (мс)':<18} {'Таблица (мс)':<15} {'Оптимизир. (мс)':<15}")
    print("-" * 70)
    
    for n in test_values:
        results = []
        
        # Наивный метод (только для небольших n)
        if n <= 30:
            start = time.perf_counter()
            result = fibonacci_naive(n)
            naive_time = (time.perf_counter() - start) * 1000
            results.append(naive_time)
        else:
            results.append("N/A")
        
        # Мемоизация
        start = time.perf_counter()
        result = fibonacci_memoization(n)
        memo_time = (time.perf_counter() - start) * 1000
        results.append(memo_time)
        
        # Табличный метод
        start = time.perf_counter()
        result = fibonacci_tabulation(n)
        tab_time = (time.perf_counter() - start) * 1000
        results.append(tab_time)
        
        # Оптимизированный метод
        start = time.perf_counter()
        result = fibonacci_optimized(n)
        opt_time = (time.perf_counter() - start) * 1000
        results.append(opt_time)
        
        # Вывод результатов
        print(f"{n:<10} ", end="")
        for time_val in results:
            if isinstance(time_val, str):
                print(f"{time_val:<15}", end="")
            else:
                print(f"{time_val:<15.4f}", end="")
        print()
    
    print("\nВыводы:")
    print("1. Наивный метод экспоненциально медленнее уже для n=30")
    print("2. Мемоизация и табличный метод имеют линейную сложность")
    print("3. Оптимизированный метод имеет O(1) память при той же скорости")


def compare_knapsack_methods():
    """Сравнение методов решения задачи о рюкзаке"""
    print("\n\nСравнение методов решения задачи о рюкзаке 0-1")
    print("=" * 60)
    
    # Тестовые данные
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacities = [5, 7, 10]
    
    print("Предметы (вес, стоимость):")
    for i, (w, v) in enumerate(zip(weights, values), 1):
        print(f"  Предмет {i}: вес={w}, стоимость={v}")
    
    print("\nРезультаты:")
    print(f"{'Вместимость':<12} {'Базовый ДП':<15} {'Оптимизированный ДП':<20} {'Результат':<10}")
    print("-" * 60)
    
    for capacity in capacities:
        # Базовый ДП
        start = time.perf_counter()
        result1 = knapsack_01(weights, values, capacity)
        time1 = (time.perf_counter() - start) * 1000
        
        # Оптимизированный ДП
        start = time.perf_counter()
        result2 = knapsack_01_optimized(weights, values, capacity)
        time2 = (time.perf_counter() - start) * 1000
        
        print(f"{capacity:<12} {time1:<15.4f} {time2:<20.4f} {result1:<10}")
    
    print("\nВыводы:")
    print("1. Оба метода дают одинаковый результат")
    print("2. Оптимизированный метод использует меньше памяти")
    print("3. Разница во времени незначительна для небольших задач")


def compare_coin_change_methods():
    """Сравнение различных задач на размен монет"""
    print("\n\nСравнение задач на размен монет")
    print("=" * 60)
    
    coins = [1, 2, 5, 10, 20, 50, 100]
    amounts = [5, 10, 27, 50, 100, 200]
    
    print(f"Монеты: {coins}")
    print("\nРезультаты:")
    print(f"{'Сумма':<10} {'Мин. монет':<12} {'Способов':<12} {'Время мин. (мс)':<18} {'Время способов (мс)':<20}")
    print("-" * 70)
    
    for amount in amounts:
        # Минимальное количество монет
        start = time.perf_counter()
        min_coins = coin_change_min_coins(coins, amount)
        time_min = (time.perf_counter() - start) * 1000
        
        # Количество способов
        start = time.perf_counter()
        ways = coin_change_ways(coins, amount)
        time_ways = (time.perf_counter() - start) * 1000
        
        print(f"{amount:<10} {min_coins:<12} {ways:<12} {time_min:<18.4f} {time_ways:<20.4f}")


def compare_lcs_methods():
    """Сравнение методов LCS"""
    print("\n\nСравнение методов LCS")
    print("=" * 60)
    
    test_cases = [
        ("ABCDGH", "AEDFHR"),
        ("AGGTAB", "GXTXAYB"),
        ("ABCBDAB", "BDCABA"),
        ("longest_common", "common_subsequence")
    ]
    
    print(f"{'Строка 1':<20} {'Строка 2':<20} {'Длина LCS':<10} {'Время (мс)':<15} {'LCS':<20}")
    print("-" * 90)
    
    for str1, str2 in test_cases:
        # Базовый LCS
        start = time.perf_counter()
        length = longest_common_subsequence(str1, str2)
        time_basic = (time.perf_counter() - start) * 1000
        
        # LCS с восстановлением
        start = time.perf_counter()
        length2, lcs_str = lcs_with_reconstruction(str1, str2)
        time_recon = (time.perf_counter() - start) * 1000
        
        print(f"{str1:<20} {str2:<20} {length:<10} {time_basic:<15.4f} {lcs_str:<20}")


def test_lis_performance():
    """Тестирование производительности LIS"""
    print("\n\nТестирование производительности LIS")
    print("=" * 60)
    
    import random
    
    sizes = [100, 200, 500, 1000, 2000]
    
    print(f"{'Размер':<10} {'Время O(n²) (мс)':<20} {'Длина LIS':<12}")
    print("-" * 45)
    
    for size in sizes:
        # Генерируем случайную последовательность
        nums = [random.randint(1, 1000) for _ in range(size)]
        
        # Измеряем время
        start = time.perf_counter()
        lis_length = longest_increasing_subsequence(nums)
        exec_time = (time.perf_counter() - start) * 1000
        
        print(f"{size:<10} {exec_time:<20.4f} {lis_length:<12}")


def test_edit_distance():
    """Тестирование расстояния Левенштейна"""
    print("\n\nТестирование расстояния Левенштейна")
    print("=" * 60)
    
    test_cases = [
        ("kitten", "sitting"),  # 3 операции
        ("sunday", "saturday"),  # 3 операции
        ("intention", "execution"),  # 5 операций
        ("algorithm", "logarithm")  # 3 операции
    ]
    
    print(f"{'Строка 1':<15} {'Строка 2':<15} {'Расстояние':<12} {'Время (мс)':<15}")
    print("-" * 60)
    
    for str1, str2 in test_cases:
        start = time.perf_counter()
        distance = edit_distance(str1, str2)
        exec_time = (time.perf_counter() - start) * 1000
        
        print(f"{str1:<15} {str2:<15} {distance:<12} {exec_time:<15.4f}")


def test_matrix_chain_multiplication():
    """Тестирование перемножения матриц"""
    print("\n\nТестирование перемножения матриц")
    print("=" * 60)
    
    test_cases = [
        [10, 20, 30],  # 2 матрицы: 10x20 и 20x30
        [10, 20, 30, 40, 30],  # 4 матрицы
        [30, 35, 15, 5, 10, 20, 25],  # 6 матриц (классический пример)
        [5, 10, 3, 12, 5, 50, 6]  # 6 матриц
    ]
    
    print(f"{'Размерности':<30} {'Мин. умножений':<20} {'Время (мс)':<15}")
    print("-" * 70)
    
    for dims in test_cases:
        start = time.perf_counter()
        min_cost, split_table = matrix_chain_order(dims)
        exec_time = (time.perf_counter() - start) * 1000
        
        dims_str = "×".join(str(d) for d in dims)
        print(f"{dims_str:<30} {min_cost:<20} {exec_time:<15.4f}")
        
        # Выводим оптимальное расстановку скобок для небольших случаев
        if len(dims) <= 4:
            print(f"  Оптимальное расстановка: ", end="")
            print_optimal_parens(split_table, 1, len(dims) - 1)
            print()


def print_optimal_parens(s, i, j):
    """Вспомогательная функция для вывода расстановки скобок"""
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


def measure_memory_usage():
    """Измерение использования памяти различными методами"""
    print("\n\nИзмерение использования памяти")
    print("=" * 60)
    
    print("Для n=30:")
    
    # Используем sys.getsizeof для приблизительной оценки
    import sys
    
    # Создаем объекты для оценки
    n = 30
    
    # Мемоизация
    memo = {}
    fibonacci_memoization(n, memo)
    memo_size = sys.getsizeof(memo)
    for key, value in memo.items():
        memo_size += sys.getsizeof(key) + sys.getsizeof(value)
    
    # Табличный метод
    dp_fib = [0] * (n + 1)
    dp_size = sys.getsizeof(dp_fib) + sum(sys.getsizeof(x) for x in dp_fib)
    
    # Оптимизированный метод
    prev2, prev1 = 0, 1
    opt_size = sys.getsizeof(prev2) + sys.getsizeof(prev1)
    
    print(f"  Мемоизация: ~{memo_size} байт")
    print(f"  Табличный метод: ~{dp_size} байт")
    print(f"  Оптимизированный метод: ~{opt_size} байт")
    print(f"  Отношение (мемоизация/оптимизированный): {memo_size/opt_size:.1f} раз")


def run_all_comparisons():
    """Запуск всех сравнений"""
    compare_fibonacci_methods()
    compare_knapsack_methods()
    compare_coin_change_methods()
    compare_lcs_methods()
    test_lis_performance()
    test_edit_distance()
    test_matrix_chain_multiplication()
    measure_memory_usage()


if __name__ == "__main__":
    print("Сравнительный анализ методов динамического программирования")
    print("=" * 70)
    run_all_comparisons()