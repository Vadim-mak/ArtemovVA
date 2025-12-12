import time
import random
from greedy_algorithms import (
    interval_scheduling,
    fractional_knapsack,
    coin_change_greedy,
    huffman_coding,
    is_canonical_coin_system
)


def compare_knapsack_solutions():
    """
    Сравнение жадного алгоритма для непрерывного рюкзака
    с точным алгоритмом для дискретного рюкзака (0-1).
    """
    print("Сравнение жадного и точного алгоритмов для задачи о рюкзаке")
    print("=" * 60)
    
    # Генерируем тестовые данные
    items = []
    for i in range(10):
        weight = random.randint(1, 20)
        value = random.randint(1, 50)
        items.append((weight, value))
    
    capacity = 50
    
    print(f"Предметы (вес, стоимость): {items}")
    print(f"Вместимость рюкзака: {capacity}")
    
    # Жадный алгоритм для непрерывного рюкзака
    start = time.perf_counter()
    greedy_value, greedy_selection = fractional_knapsack(items.copy(), capacity)
    greedy_time = (time.perf_counter() - start) * 1000
    
    print(f"\nЖадный алгоритм (непрерывный рюкзак):")
    print(f"  Максимальная стоимость: {greedy_value:.2f}")
    print(f"  Время выполнения: {greedy_time:.4f} мс")
    
    # Точный алгоритм для дискретного рюкзака 0-1 (полный перебор)
    def knapsack_01_bruteforce(items, capacity):
        n = len(items)
        best_value = 0
        best_selection = []
        
        # Перебираем все возможные комбинации
        for mask in range(1 << n):
            total_weight = 0
            total_value = 0
            selection = []
            
            for i in range(n):
                if mask & (1 << i):
                    weight, value = items[i]
                    total_weight += weight
                    total_value += value
                    selection.append(i)
            
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_selection = selection
        
        return best_value, best_selection
    
    start = time.perf_counter()
    optimal_value, optimal_selection = knapsack_01_bruteforce(items, capacity)
    optimal_time = (time.perf_counter() - start) * 1000
    
    print(f"\nТочный алгоритм (дискретный рюкзак 0-1):")
    print(f"  Максимальная стоимость: {optimal_value:.2f}")
    print(f"  Время выполнения: {optimal_time:.4f} мс")
    
    # Сравнение результатов
    ratio = greedy_value / optimal_value if optimal_value > 0 else 1
    
    print(f"\nСравнение:")
    print(f"  Отношение (жадный/оптимальный): {ratio:.2%}")
    print(f"  Разница в стоимости: {optimal_value - greedy_value:.2f}")
    
    return items, capacity, greedy_value, optimal_value, ratio


def test_interval_scheduling_performance():
    """Тестирование производительности алгоритма выбора заявок"""
    print("\n\nТестирование алгоритма выбора заявок")
    print("=" * 60)
    
    sizes = [100, 500, 1000, 5000, 10000]
    
    print(f"{'Кол-во заявок':<15} {'Время (мс)':<15} {'Выбрано заявок':<15}")
    print("-" * 45)
    
    for size in sizes:
        # Генерируем случайные интервалы
        intervals = []
        for _ in range(size):
            start = random.randint(0, 1000)
            end = start + random.randint(1, 100)
            intervals.append((start, end))
        
        # Измеряем время выполнения
        start = time.perf_counter()
        selected = interval_scheduling(intervals)
        execution_time = (time.perf_counter() - start) * 1000
        
        print(f"{size:<15} {execution_time:<15.4f} {len(selected):<15}")


def test_huffman_performance():
    """Тестирование производительности алгоритма Хаффмана"""
    print("\n\nТестирование алгоритма Хаффмана")
    print("=" * 60)
    
    sizes = [10, 50, 100, 500, 1000]
    
    print(f"{'Кол-во символов':<15} {'Время (мс)':<15} {'Средняя длина кода':<20}")
    print("-" * 50)
    
    for size in sizes:
        # Генерируем случайные частоты символов
        frequencies = {}
        total_freq = 0
        
        for i in range(size):
            freq = random.randint(1, 100)
            frequencies[f"Символ_{i}"] = freq
            total_freq += freq
        
        # Измеряем время выполнения
        start = time.perf_counter()
        codes = huffman_coding(frequencies)
        execution_time = (time.perf_counter() - start) * 1000
        
        # Вычисляем среднюю длину кода
        avg_length = 0
        for symbol, freq in frequencies.items():
            code_length = len(codes[symbol])
            probability = freq / total_freq
            avg_length += code_length * probability
        
        print(f"{size:<15} {execution_time:<15.4f} {avg_length:<20.4f}")
    
    return frequencies, codes


def test_coin_systems():
    """Тестирование различных систем монет"""
    print("\n\nТестирование систем монет")
    print("=" * 60)
    
    # Различные системы монет
    coin_systems = [
        ([1, 5, 10, 25, 50, 100], "Каноническая (1, 5, 10, 25, 50, 100)"),
        ([1, 3, 4], "НЕ каноническая (1, 3, 4)"),
        ([1, 2, 5, 10, 20, 50], "Каноническая (евро)"),
        ([1, 5, 10, 20, 25], "НЕ каноническая (1, 5, 10, 20, 25)"),
    ]
    
    test_amounts = [37, 68, 99, 123, 256]
    
    for coins, description in coin_systems:
        print(f"\nСистема монет: {description}")
        print(f"Монеты: {coins}")
        
        # Проверяем, является ли система канонической
        is_canonical, amount, greedy_count, optimal_count = is_canonical_coin_system(coins)
        
        if is_canonical:
            print(f"   Система является канонической")
        else:
            print(f"   Система НЕ является канонической")
            print(f"    Пример: для суммы {amount}")
            print(f"    Жадный алгоритм: {greedy_count} монет")
            print(f"    Оптимальное решение: {optimal_count} монет")
        
        # Тестируем для нескольких сумм
        print(f"  Тестирование для разных сумм:")
        for amount in test_amounts:
            result, total_coins = coin_change_greedy(coins.copy(), amount)
            
            if result is None:
                print(f"    Сумма {amount}: невозможно выдать")
            else:
                coins_str = ", ".join([f"{count}×{coin}" for coin, count in result])
                print(f"    Сумма {amount}: {total_coins} монет ({coins_str})")


def visualize_huffman_tree(codes):
    """Визуализация дерева Хаффмана"""
    print("\n\nВизуализация дерева Хаффмана")
    print("=" * 60)
    
    # Сортируем коды по длине для удобного отображения
    sorted_codes = sorted(codes.items(), key=lambda x: (len(x[1]), x[1]))
    
    print("Коды символов:")
    for symbol, code in sorted_codes:
        print(f"  '{symbol}': {code}")
    
    # Строим простое текстовое представление дерева
    print("\nТекстовое представление дерева:")
    
    # Находим все префиксы
    prefixes = set()
    for code in codes.values():
        for i in range(1, len(code) + 1):
            prefixes.add(code[:i])
    
    # Сортируем префиксы
    sorted_prefixes = sorted(prefixes, key=lambda x: (len(x), x))
    
    for prefix in sorted_prefixes:
        # Находим символы с этим префиксом
        symbols = [s for s, c in codes.items() if c.startswith(prefix)]
        
        indent = "  " * len(prefix)
        if prefix in codes.values():
            # Это лист (символ)
            symbol = [s for s, c in codes.items() if c == prefix][0]
            print(f"{indent}└── '{symbol}' ({prefix})")
        else:
            # Это внутренний узел
            print(f"{indent}├── Узел {prefix}0.../{prefix}1...")
    
    # Вычисляем статистику
    total_symbols = len(codes)
    max_length = max(len(code) for code in codes.values())
    min_length = min(len(code) for code in codes.values())
    
    print(f"\nСтатистика:")
    print(f"  Всего символов: {total_symbols}")
    print(f"  Максимальная длина кода: {max_length}")
    print(f"  Минимальная длина кода: {min_length}")
    
    # Проверяем свойство префиксности
    is_prefix_free = True
    for i, (symbol1, code1) in enumerate(sorted_codes):
        for symbol2, code2 in sorted_codes[i+1:]:
            if code1.startswith(code2) or code2.startswith(code1):
                is_prefix_free = False
                print(f"   Нарушение префиксности: '{symbol1}' ({code1}) и '{symbol2}' ({code2})")
    
    if is_prefix_free:
        print(f"   Все коды удовлетворяют свойству префиксности")


def analyze_greedy_correctness():
    """Анализ корректности жадных алгоритмов"""
    print("\n\nАнализ корректности жадных алгоритмов")
    print("=" * 60)
    
    print("1. Задача о выборе заявок (Interval Scheduling):")
    print("   Жадный алгоритм (выбор по времени окончания) всегда оптимален.")
    print("   Доказательство: Пусть существует оптимальное решение, отличное от жадного.")
    print("   Можно заменить первую отличающуюся заявку в оптимальном решении")
    print("   на более рано заканчивающуюся из жадного, не ухудшив решение.")
    
    print("\n2. Непрерывный рюкзак (Fractional Knapsack):")
    print("   Жадный алгоритм (выбор по удельной стоимости) всегда оптимален.")
    print("   Доказательство: Предположим, существует лучшее решение.")
    print("   Тогда в нем есть предмет с меньшей удельной стоимостью, чем какой-то")
    print("   не выбранный предмет. Замена части первого на часть второго улучшит решение.")
    
    print("\n3. Задача о монетах (Coin Change):")
    print("   Жадный алгоритм оптимален только для канонических систем монет.")
    print("   Пример неканонической системы: [1, 3, 4]")
    print("   Для суммы 6: жадный алгоритм дает 3+3 (2 монеты)")
    print("   Оптимальное решение: 4+1+1 (3 монеты)")
    print("   ОШИБКА: жадный дает 4+1+1=6 (3 монеты)")
    print("   Правильный пример: сумма 6: жадный 4+1+1=3 монеты, оптимальный 3+3=2 монеты")
    
    print("\n4. Алгоритм Хаффмана:")
    print("   Всегда строит оптимальное префиксное кодирование.")
    print("   Доказательство: Индукция по количеству символов.")
    print("   На каждом шаге объединяем два символа с наименьшей частотой,")
    print("   что гарантирует минимальную среднюю длину кода.")


if __name__ == "__main__":
    print("Анализ жадных алгоритмов")
    print("=" * 60)
    
    # Запуск всех тестов
    items, capacity, greedy_val, optimal_val, ratio = compare_knapsack_solutions()
    test_interval_scheduling_performance()
    frequencies, codes = test_huffman_performance()
    test_coin_systems()
    visualize_huffman_tree(codes)
    analyze_greedy_correctness()