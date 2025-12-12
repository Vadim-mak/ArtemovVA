def interval_scheduling(intervals):
    """
    Задача о выборе заявок (Interval Scheduling).
    Выбирает максимальное количество непересекающихся интервалов.
    
    Жадный выбор: сортировка по времени окончания и выбор следующего
    рано заканчивающегося непересекающегося интервала.
    
    Сложность: O(n log n) из-за сортировки
    """
    if not intervals:
        return []
    
    # Сортируем интервалы по времени окончания
    intervals.sort(key=lambda x: x[1])  # O(n log n)
    
    selected = [intervals[0]]  # O(1)
    last_end = intervals[0][1]  # O(1)
    
    # Проходим по отсортированным интервалам
    for i in range(1, len(intervals)):  # O(n)
        start, end = intervals[i]  # O(1)
        
        # Если интервал не пересекается с последним выбранным
        if start >= last_end:  # O(1)
            selected.append(intervals[i])  # O(1)
            last_end = end  # O(1)
    
    return selected  # O(1)


def fractional_knapsack(items, capacity):
    """
    Непрерывный рюкзак (Fractional Knapsack).
    Максимизирует стоимость содержимого рюкзака,
    если можно брать дробные части предметов.
    
    Жадный выбор: сортировка по удельной стоимости (цена/вес)
    и взятие большего количества лучших предметов.
    
    Сложность: O(n log n) из-за сортировки
    """
    # Вычисляем удельную стоимость для каждого предмета
    for i in range(len(items)):  # O(n)
        weight, value = items[i]  # O(1)
        items[i] = (weight, value, value / weight)  # O(1)
    
    # Сортируем по убыванию удельной стоимости
    items.sort(key=lambda x: x[2], reverse=True)  # O(n log n)
    
    total_value = 0.0  # O(1)
    remaining_capacity = capacity  # O(1)
    selected_items = []  # O(1)
    
    for weight, value, ratio in items:  # O(n)
        if remaining_capacity <= 0:  # O(1)
            break
        
        # Берем столько, сколько можем
        take_weight = min(weight, remaining_capacity)  # O(1)
        take_value = take_weight * ratio  # O(1)
        
        total_value += take_value  # O(1)
        remaining_capacity -= take_weight  # O(1)
        
        selected_items.append((take_weight, take_value, take_weight / weight))  # O(1)
    
    return total_value, selected_items  # O(1)


def coin_change_greedy(coins, amount):
    """
    Задача о минимальном количестве монет для выдачи сдачи.
    Жадный алгоритм работает только для канонических систем монет.
    
    Сложность: O(n) где n - количество номиналов монет
    """
    # Сортируем монеты по убыванию
    coins.sort(reverse=True)  # O(n log n)
    
    result = []  # O(1)
    remaining = amount  # O(1)
    
    for coin in coins:  # O(n)
        # Сколько монет этого номинала можем взять
        count = remaining // coin  # O(1)
        
        if count > 0:  # O(1)
            result.append((coin, count))  # O(1)
            remaining -= coin * count  # O(1)
        
        if remaining == 0:  # O(1)
            break
    
    # Проверяем, удалось ли набрать нужную сумму
    if remaining > 0:  # O(1)
        return None, remaining  # Не удалось набрать сумму
    
    # Вычисляем общее количество монет
    total_coins = sum(count for _, count in result)  # O(n)
    return result, total_coins  # O(1)


def huffman_coding(frequencies):
    """
    Алгоритм Хаффмана для оптимального префиксного кодирования.
    
    Сложность: O(n log n) где n - количество символов
    """
    import heapq
    
    # Создаем очередь с приоритетом (min-heap)
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]  # O(n)
    heapq.heapify(heap)  # O(n)
    
    # Пока в куче больше одного элемента
    while len(heap) > 1:  # O(n)
        # Извлекаем два узла с наименьшей частотой
        lo = heapq.heappop(heap)  # O(log n)
        hi = heapq.heappop(heap)  # O(log n)
        
        # Добавляем '0' ко всем кодам в левом поддереве
        for pair in lo[1:]:  # O(k)
            pair[1] = '0' + pair[1]
        
        # Добавляем '1' ко всем кодам в правом поддереве
        for pair in hi[1:]:  # O(k)
            pair[1] = '1' + pair[1]
        
        # Создаем новый узел с суммой частот
        new_node = [lo[0] + hi[0]] + lo[1:] + hi[1:]  # O(1)
        heapq.heappush(heap, new_node)  # O(log n)
    
    # Извлекаем коды из корня дерева
    huffman_codes = {}  # O(1)
    for symbol, code in heap[0][1:]:  # O(n)
        huffman_codes[symbol] = code  # O(1)
    
    return huffman_codes  # O(1)


def is_canonical_coin_system(coins):
    """
    Проверяет, является ли система монет канонической
    (жадный алгоритм всегда дает оптимальное решение).
    
    Сложность: O(n³) в худшем случае, но обычно O(n²)
    """
    # Сортируем монеты по возрастанию
    coins_sorted = sorted(coins)  # O(n log n)
    n = len(coins_sorted)  # O(1)
    
    # Для каждого номинала проверяем условие каноничности
    for i in range(n):  # O(n)
        for j in range(i + 1, n):  # O(n²)
            # Проверяем, что жадный алгоритм оптимален для суммы coins_sorted[j] - 1
            amount = coins_sorted[j] - 1  # O(1)
            
            # Жадное решение
            greedy_count = 0  # O(1)
            temp_amount = amount  # O(1)
            for k in range(n - 1, -1, -1):  # O(n³)
                if coins_sorted[k] <= temp_amount:  # O(1)
                    greedy_count += temp_amount // coins_sorted[k]  # O(1)
                    temp_amount %= coins_sorted[k]  # O(1)
            
            # Динамическое программирование для оптимального решения
            dp = [float('inf')] * (amount + 1)  # O(m)
            dp[0] = 0  # O(1)
            
            for k in range(amount + 1):  # O(n*m)
                for coin in coins_sorted:  # O(n)
                    if k + coin <= amount:  # O(1)
                        dp[k + coin] = min(dp[k + coin], dp[k] + 1)  # O(1)
            
            optimal_count = dp[amount]  # O(1)
            
            # Если жадный алгоритм не оптимален, система не каноническая
            if greedy_count != optimal_count:  # O(1)
                return False, amount, greedy_count, optimal_count  # O(1)
    
    return True, None, None, None  # O(1)