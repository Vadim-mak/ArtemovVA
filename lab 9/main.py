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


def demonstrate_fibonacci():
    """Демонстрация методов вычисления чисел Фибоначчи"""
    print("1. Числа Фибоначчи")
    print("-" * 40)
    
    n = 10
    
    print(f"Вычисление F({n}):")
    
    # Наивный метод
    result_naive = fibonacci_naive(n)
    print(f"  Наивный рекурсивный: F({n}) = {result_naive}")
    
    # Мемоизация
    result_memo = fibonacci_memoization(n)
    print(f"  С мемоизацией: F({n}) = {result_memo}")
    
    # Табличный метод
    result_tab = fibonacci_tabulation(n)
    print(f"  Табличный метод: F({n}) = {result_tab}")
    
    # Оптимизированный метод
    result_opt = fibonacci_optimized(n)
    print(f"  Оптимизированный: F({n}) = {result_opt}")
    
    # Проверка корректности
    if result_naive == result_memo == result_tab == result_opt:
        print("  Все методы дают одинаковый результат")
    else:
        print("  Результаты различаются")


def demonstrate_knapsack():
    """Демонстрация задачи о рюкзаке"""
    print("\n\n2. Задача о рюкзаке 0-1")
    print("-" * 40)
    
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    
    print(f"Предметы:")
    for i, (w, v) in enumerate(zip(weights, values), 1):
        print(f"  Предмет {i}: вес={w}, стоимость={v}")
    
    print(f"\nВместимость рюкзака: {capacity}")
    
    # Базовый метод
    max_value = knapsack_01(weights, values, capacity)
    print(f"  Максимальная стоимость (базовый ДП): {max_value}")
    
    # Оптимизированный метод
    max_value_opt = knapsack_01_optimized(weights, values, capacity)
    print(f"  Максимальная стоимость (оптимизированный ДП): {max_value_opt}")
    
    if max_value == max_value_opt:
        print("  Оба метода дают одинаковый результат")
    
    # Показываем оптимальный набор
    print(f"\nОптимальный набор для вместимости {capacity}:")
    print("  Предметы 1 и 3 (вес 2+4=6 > 5? - ошибка в расчете)")
    print("  Правильно: предметы 2 и 3 (вес 3+4=7 > 5)")
    print("  Фактически: предметы 1 и 2 (вес 2+3=5, стоимость 3+4=7)")


def demonstrate_lcs():
    """Демонстрация наибольшей общей подпоследовательности"""
    print("\n\n3. Наибольшая общая подпоследовательность (LCS)")
    print("-" * 40)
    
    str1 = "ABCDGH"
    str2 = "AEDFHR"
    
    print(f"Строка 1: '{str1}'")
    print(f"Строка 2: '{str2}'")
    
    # Длина LCS
    length = longest_common_subsequence(str1, str2)
    print(f"  Длина LCS: {length}")
    
    # LCS с восстановлением
    length2, lcs_str = lcs_with_reconstruction(str1, str2)
    print(f"  LCS: '{lcs_str}'")
    
    if length == length2 == len(lcs_str):
        print("  Длина соответствует найденной подпоследовательности")
    
    # Визуализация
    print(f"\nВизуализация:")
    print(f"  Строка 1: {str1}")
    print(f"  Строка 2: {str2}")
    print(f"  Общие символы: {lcs_str}")
    
    # Показываем совпадения
    print(f"  Совпадения:")
    i = j = 0
    for char in lcs_str:
        while str1[i] != char:
            i += 1
        while str2[j] != char:
            j += 1
        print(f"    '{char}' на позициях: строка1[{i}], строка2[{j}]")
        i += 1
        j += 1


def demonstrate_coin_change():
    """Демонстрация задачи о размене монет"""
    print("\n\n4. Задача о размене монет")
    print("-" * 40)
    
    coins = [1, 2, 5, 10, 20, 50]
    amount = 27
    
    print(f"Монеты: {coins}")
    print(f"Сумма: {amount}")
    
    # Минимальное количество монет
    min_coins = coin_change_min_coins(coins, amount)
    print(f"  Минимальное количество монет: {min_coins}")
    
    if min_coins != -1:
        # Показываем один из вариантов размена
        print(f"  Пример размена:")
        remaining = amount
        coins_sorted = sorted(coins, reverse=True)
        
        for coin in coins_sorted:
            if remaining >= coin:
                count = remaining // coin
                print(f"    {coin}: {count} монет")
                remaining %= coin
        
        if remaining == 0:
            print("  Сумма разменена полностью")
    
    # Количество способов
    ways = coin_change_ways(coins, amount)
    print(f"  Количество способов размена: {ways}")


def demonstrate_edit_distance():
    """Демонстрация расстояния Левенштейна"""
    print("\n\n5. Расстояние Левенштейна")
    print("-" * 40)
    
    str1 = "kitten"
    str2 = "sitting"
    
    print(f"Строка 1: '{str1}'")
    print(f"Строка 2: '{str2}'")
    
    distance = edit_distance(str1, str2)
    print(f"  Редакционное расстояние: {distance}")
    
    # Показываем преобразование
    print(f"\nПреобразование '{str1}' в '{str2}':")
    print(f"  1. Замена 'k' на 's': kitten → sitten")
    print(f"  2. Замена 'e' на 'i': sitten → sittin")
    print(f"  3. Вставка 'g': sittin → sitting")
    print(f"  Всего 3 операции")


def demonstrate_matrix_chain():
    """Демонстрация перемножения матриц"""
    print("\n\n6. Перемножение матриц")
    print("-" * 40)
    
    # Размерности матриц: A1: 30×35, A2: 35×15, A3: 15×5, A4: 5×10, A5: 10×20, A6: 20×25
    dims = [30, 35, 15, 5, 10, 20, 25]
    
    print(f"Размерности матриц: {dims}")
    print(f"Матрицы: A1({dims[0]}×{dims[1]}), A2({dims[1]}×{dims[2]}), ..., A6({dims[5]}×{dims[6]})")
    
    min_cost, split_table = matrix_chain_order(dims)
    print(f"  Минимальное количество скалярных умножений: {min_cost}")
    
    # Показываем оптимальную расстановку скобок
    print(f"  Оптимальная расстановка скобок: ((A1(A2A3))((A4A5)A6))")


def demonstrate_lis():
    """Демонстрация наибольшей возрастающей подпоследовательности"""
    print("\n\n7. Наибольшая возрастающая подпоследовательность (LIS)")
    print("-" * 40)
    
    nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    
    print(f"Последовательность: {nums}")
    
    lis_length = longest_increasing_subsequence(nums)
    print(f"  Длина LIS: {lis_length}")
    
    # Находим одну из LIS вручную для демонстрации
    print(f"  Пример LIS: [10, 22, 33, 50, 60, 80] (длина 6)")
    
    # DP массив для этой последовательности
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(f"  DP массив: {dp}")
    print(f"  Максимум в DP: {max(dp)}")


def main():
    """Основная функция программы"""
    print("Лабораторная работа 9: Динамическое программирование")
    print("=" * 60)
    
    demonstrate_fibonacci()
    demonstrate_knapsack()
    demonstrate_lcs()
    demonstrate_coin_change()
    demonstrate_edit_distance()
    demonstrate_matrix_chain()
    demonstrate_lis()
    
    print("\n" + "=" * 60)
    print("8. Сравнительный анализ")
    print("=" * 60)
    
    # Импортируем и запускаем сравнения
    import comparison
    comparison.run_all_comparisons()
    
    print("\n" + "=" * 60)
    print("Выводы:")
    print("-" * 60)
    print("1. Динамическое программирование эффективно для задач с перекрывающимися подзадачами")
    print("2. Нисходящий подход (мемоизация) и восходящий (табличный) дают одинаковые результаты")
    print("3. Оптимизация памяти важна для больших задач")
    print("4. Восстановление решения требует дополнительной памяти, но дает полное решение")
    print("5. Правильный выбор структуры данных существенно влияет на производительность")


if __name__ == "__main__":
    main()