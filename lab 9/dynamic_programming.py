def fibonacci_naive(n):
    """
    Наивное рекурсивное вычисление чисел Фибоначчи.
    Сложность: O(2^n) - экспоненциальная
    Память: O(n) - глубина рекурсии
    """
    if n <= 1:  # O(1)
        return n  # O(1)
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)  # O(2^n)


def fibonacci_memoization(n, memo=None):
    """
    Вычисление чисел Фибоначчи с мемоизацией (нисходящее ДП).
    Сложность: O(n) - линейная
    Память: O(n) - для хранения мемоизированных значений
    """
    if memo is None:  # O(1)
        memo = {}  # O(1)
    
    if n in memo:  # O(1)
        return memo[n]  # O(1)
    
    if n <= 1:  # O(1)
        result = n  # O(1)
    else:
        result = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)  # O(n)
    
    memo[n] = result  # O(1)
    return result  # O(1)


def fibonacci_tabulation(n):
    """
    Вычисление чисел Фибоначчи табличным методом (восходящее ДП).
    Сложность: O(n) - линейная
    Память: O(n) - для хранения таблицы
    """
    if n <= 1:  # O(1)
        return n  # O(1)
    
    dp = [0] * (n + 1)  # O(n)
    dp[1] = 1  # O(1)
    
    for i in range(2, n + 1):  # O(n)
        dp[i] = dp[i-1] + dp[i-2]  # O(1)
    
    return dp[n]  # O(1)


def fibonacci_optimized(n):
    """
    Оптимизированное вычисление чисел Фибоначчи.
    Сложность: O(n) - линейная
    Память: O(1) - константная
    """
    if n <= 1:  # O(1)
        return n  # O(1)
    
    prev2, prev1 = 0, 1  # O(1)
    
    for i in range(2, n + 1):  # O(n)
        current = prev1 + prev2  # O(1)
        prev2, prev1 = prev1, current  # O(1)
    
    return prev1  # O(1)


def knapsack_01(weights, values, capacity):
    """
    Задача о рюкзаке 0-1 (восходящее ДП).
    Сложность: O(n * capacity) - псевдополиномиальная
    Память: O(n * capacity) - для таблицы ДП
    """
    n = len(weights)  # O(1)
    
    # Создаем таблицу ДП
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # O(n * capacity)
    
    # Заполняем таблицу
    for i in range(1, n + 1):  # O(n)
        for w in range(capacity + 1):  # O(capacity)
            if weights[i-1] <= w:  # O(1)
                # Максимум из двух вариантов:
                # 1. Не брать текущий предмет
                # 2. Брать текущий предмет + оптимальное решение для оставшейся вместимости
                dp[i][w] = max(dp[i-1][w],  # O(1)
                              dp[i-1][w - weights[i-1]] + values[i-1])  # O(1)
            else:
                dp[i][w] = dp[i-1][w]  # O(1)
    
    return dp[n][capacity]  # O(1)


def knapsack_01_optimized(weights, values, capacity):
    """
    Задача о рюкзаке 0-1 с оптимизацией памяти.
    Сложность: O(n * capacity)
    Память: O(capacity) - только один ряд таблицы
    """
    n = len(weights)  # O(1)
    
    # Используем только два ряда вместо всей таблицы
    dp_prev = [0] * (capacity + 1)  # O(capacity)
    dp_curr = [0] * (capacity + 1)  # O(capacity)
    
    for i in range(1, n + 1):  # O(n)
        for w in range(capacity + 1):  # O(capacity)
            if weights[i-1] <= w:  # O(1)
                dp_curr[w] = max(dp_prev[w],  # O(1)
                                dp_prev[w - weights[i-1]] + values[i-1])  # O(1)
            else:
                dp_curr[w] = dp_prev[w]  # O(1)
        
        # Обновляем ряды для следующей итерации
        dp_prev, dp_curr = dp_curr, dp_prev  # O(1)
    
    return dp_prev[capacity]  # O(1)


def longest_common_subsequence(text1, text2):
    """
    Наибольшая общая подпоследовательность (LCS).
    Сложность: O(n * m) где n,m - длины строк
    Память: O(n * m) для таблицы ДП
    """
    n, m = len(text1), len(text2)  # O(1)
    
    # Создаем таблицу ДП
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # O(n * m)
    
    # Заполняем таблицу
    for i in range(1, n + 1):  # O(n)
        for j in range(1, m + 1):  # O(m)
            if text1[i-1] == text2[j-1]:  # O(1)
                dp[i][j] = dp[i-1][j-1] + 1  # O(1)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # O(1)
    
    return dp[n][m]  # O(1)


def lcs_with_reconstruction(text1, text2):
    """
    LCS с восстановлением подпоследовательности.
    Сложность: O(n * m)
    Память: O(n * m)
    """
    n, m = len(text1), len(text2)  # O(1)
    
    # Таблицы для значений и направлений
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # O(n * m)
    directions = [[None] * (m + 1) for _ in range(n + 1)]  # O(n * m)
    
    # Заполняем таблицы
    for i in range(1, n + 1):  # O(n)
        for j in range(1, m + 1):  # O(m)
            if text1[i-1] == text2[j-1]:  # O(1)
                dp[i][j] = dp[i-1][j-1] + 1  # O(1)
                directions[i][j] = 'diag'  # O(1) - совпадение
            else:
                if dp[i-1][j] >= dp[i][j-1]:  # O(1)
                    dp[i][j] = dp[i-1][j]  # O(1)
                    directions[i][j] = 'up'  # O(1) - из строки выше
                else:
                    dp[i][j] = dp[i][j-1]  # O(1)
                    directions[i][j] = 'left'  # O(1) - из столбца слева
    
    # Восстанавливаем подпоследовательность
    lcs = []  # O(1)
    i, j = n, m  # O(1)
    
    while i > 0 and j > 0:  # O(n + m)
        if directions[i][j] == 'diag':  # O(1)
            lcs.append(text1[i-1])  # O(1)
            i -= 1  # O(1)
            j -= 1  # O(1)
        elif directions[i][j] == 'up':  # O(1)
            i -= 1  # O(1)
        else:  # 'left'
            j -= 1  # O(1)
    
    lcs.reverse()  # O(L) где L - длина LCS
    return dp[n][m], ''.join(lcs)  # O(1)


def coin_change_min_coins(coins, amount):
    """
    Минимальное количество монет для суммы (размен).
    Сложность: O(n * amount) где n - количество номиналов
    Память: O(amount) - для таблицы ДП
    """
    # Инициализируем таблицу ДП
    dp = [float('inf')] * (amount + 1)  # O(amount)
    dp[0] = 0  # O(1) - для суммы 0 нужно 0 монет
    
    # Заполняем таблицу
    for coin in coins:  # O(n)
        for i in range(coin, amount + 1):  # O(amount)
            dp[i] = min(dp[i], dp[i - coin] + 1)  # O(1)
    
    return dp[amount] if dp[amount] != float('inf') else -1  # O(1)


def coin_change_ways(coins, amount):
    """
    Количество способов разменять сумму.
    Сложность: O(n * amount)
    Память: O(amount)
    """
    # Инициализируем таблицу ДП
    dp = [0] * (amount + 1)  # O(amount)
    dp[0] = 1  # O(1) - 1 способ разменять сумму 0 (ничего не брать)
    
    # Заполняем таблицу
    for coin in coins:  # O(n)
        for i in range(coin, amount + 1):  # O(amount)
            dp[i] += dp[i - coin]  # O(1)
    
    return dp[amount]  # O(1)


def longest_increasing_subsequence(nums):
    """
    Наибольшая возрастающая подпоследовательность (LIS).
    Сложность: O(n²) - можно оптимизировать до O(n log n)
    Память: O(n)
    """
    if not nums:  # O(1)
        return 0  # O(1)
    
    n = len(nums)  # O(1)
    dp = [1] * n  # O(n) - каждый элемент сам по себе является подпоследовательностью длины 1
    
    for i in range(n):  # O(n)
        for j in range(i):  # O(n²)
            if nums[j] < nums[i]:  # O(1)
                dp[i] = max(dp[i], dp[j] + 1)  # O(1)
    
    return max(dp)  # O(n)


def edit_distance(str1, str2):
    """
    Расстояние Левенштейна (редакционное расстояние).
    Сложность: O(n * m)
    Память: O(n * m)
    """
    n, m = len(str1), len(str2)  # O(1)
    
    # Создаем таблицу ДП
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # O(n * m)
    
    # Инициализируем первую строку и первый столбец
    for i in range(n + 1):  # O(n)
        dp[i][0] = i  # O(1) - i удалений
    
    for j in range(m + 1):  # O(m)
        dp[0][j] = j  # O(1) - j вставок
    
    # Заполняем таблицу
    for i in range(1, n + 1):  # O(n)
        for j in range(1, m + 1):  # O(m)
            if str1[i-1] == str2[j-1]:  # O(1)
                dp[i][j] = dp[i-1][j-1]  # O(1) - символы совпадают
            else:
                # Минимум из трех операций:
                # 1. Удаление (dp[i-1][j] + 1)
                # 2. Вставка (dp[i][j-1] + 1)
                # 3. Замена (dp[i-1][j-1] + 1)
                dp[i][j] = 1 + min(dp[i-1][j],    # O(1)
                                   dp[i][j-1],    # O(1)
                                   dp[i-1][j-1])  # O(1)
    
    return dp[n][m]  # O(1)


def matrix_chain_order(dims):
    """
    Задача о перемножении матриц (минимальное количество скалярных умножений).
    Сложность: O(n³) где n - количество матриц
    Память: O(n²)
    """
    n = len(dims) - 1  # Количество матриц
    if n <= 1:  # O(1)
        return 0, []  # O(1)
    
    # Таблицы для стоимости и разбиений
    m = [[0] * (n + 1) for _ in range(n + 1)]  # O(n²)
    s = [[0] * (n + 1) for _ in range(n + 1)]  # O(n²)
    
    # l - длина цепочки
    for l in range(2, n + 1):  # O(n)
        for i in range(1, n - l + 2):  # O(n²)
            j = i + l - 1  # O(1)
            m[i][j] = float('inf')  # O(1)
            
            for k in range(i, j):  # O(n³)
                # Стоимость перемножения цепочек (i..k) и (k+1..j)
                cost = m[i][k] + m[k+1][j] + dims[i-1] * dims[k] * dims[j]  # O(1)
                
                if cost < m[i][j]:  # O(1)
                    m[i][j] = cost  # O(1)
                    s[i][j] = k  # O(1)
    
    return m[1][n], s  # O(1)