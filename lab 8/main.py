from greedy_algorithms import (
    interval_scheduling,
    fractional_knapsack,
    coin_change_greedy,
    huffman_coding,
    is_canonical_coin_system
)
import analysis


def demonstrate_interval_scheduling():
    """Демонстрация задачи о выборе заявок"""
    print("1. Задача о выборе заявок (Interval Scheduling)")
    print("-" * 40)
    
    # Пример интервалов (начало, конец)
    intervals = [
        (1, 4), (3, 5), (0, 6), (5, 7),
        (3, 8), (5, 9), (6, 10), (8, 11),
        (8, 12), (2, 13), (12, 14)
    ]
    
    print("Все интервалы (начало, конец):")
    for i, (start, end) in enumerate(intervals, 1):
        print(f"  Заявка {i:2d}: {start:2d} - {end:2d}")
    
    # Применяем жадный алгоритм
    selected = interval_scheduling(intervals)
    
    print("\nВыбранные интервалы (жадный алгоритм):")
    for i, (start, end) in enumerate(selected, 1):
        print(f"  Заявка {i:2d}: {start:2d} - {end:2d}")
    
    print(f"\nВсего выбрано: {len(selected)} заявок из {len(intervals)}")
    
    # Визуализация
    print("\nВизуализация интервалов:")
    max_time = max(end for _, end in intervals)
    
    for time in range(max_time + 1):
        line = f"Время {time:2d}: "
        for start, end in intervals:
            if start <= time < end:
                line += "[---]"
            else:
                line += "     "
        print(line)


def demonstrate_fractional_knapsack():
    """Демонстрация задачи о непрерывном рюкзаке"""
    print("\n\n2. Непрерывный рюкзак (Fractional Knapsack)")
    print("-" * 40)
    
    # Предметы: (вес, стоимость)
    items = [
        (10, 60),  # удельная стоимость: 6.0
        (20, 100), # удельная стоимость: 5.0
        (30, 120), # удельная стоимость: 4.0
        (15, 75),  # удельная стоимость: 5.0
        (25, 90),  # удельная стоимость: 3.6
    ]
    
    capacity = 50
    
    print(f"Предметы (вес, стоимость):")
    for i, (weight, value) in enumerate(items, 1):
        ratio = value / weight
        print(f"  Предмет {i}: вес={weight}, стоимость={value}, удельная={ratio:.2f}")
    
    print(f"\nВместимость рюкзака: {capacity}")
    
    # Применяем жадный алгоритм
    total_value, selected = fractional_knapsack(items, capacity)
    
    print("\nВыбранные предметы (жадный алгоритм):")
    for i, (weight, value, fraction) in enumerate(selected, 1):
        print(f"  Предмет {i}: взято {weight:.1f} кг ({(fraction*100):.1f}%)")
    
    print(f"\nОбщая стоимость: {total_value:.2f}")
    
    # Проверяем вес
    total_weight = sum(weight for weight, _, _ in selected)
    print(f"Общий вес: {total_weight:.1f} кг (максимум {capacity} кг)")


def demonstrate_coin_change():
    """Демонстрация задачи о размене монет"""
    print("\n\n3. Задача о размене монет (Coin Change)")
    print("-" * 40)
    
    # Каноническая система монет
    canonical_coins = [1, 5, 10, 25, 50, 100]
    amount = 137
    
    print(f"Каноническая система монет: {canonical_coins}")
    print(f"Сумма для размена: {amount}")
    
    # Проверяем, является ли система канонической
    is_canonical, test_amount, greedy_cnt, optimal_cnt = is_canonical_coin_system(canonical_coins)
    
    if is_canonical:
        print(" Система является канонической (жадный алгоритм всегда оптимален)")
    else:
        print(f" Система НЕ является канонической")
        print(f"  Пример: сумма {test_amount}")
        print(f"  Жадный алгоритм: {greedy_cnt} монет")
        print(f"  Оптимальное решение: {optimal_cnt} монет")
    
    # Применяем жадный алгоритм
    result, total_coins = coin_change_greedy(canonical_coins, amount)
    
    print(f"\nРазмен суммы {amount} (жадный алгоритм):")
    if result is None:
        print("  Невозможно разменять данную сумму")
    else:
        for coin, count in result:
            print(f"  Монета {coin:3d}: {count} шт.")
        print(f"\n  Всего монет: {total_coins}")
    
    # Пример неканонической системы
    print("\n" + "="*40)
    non_canonical_coins = [1, 3, 4]
    amount2 = 6
    
    print(f"Неканоническая система монет: {non_canonical_coins}")
    print(f"Сумма для размена: {amount2}")
    
    is_canonical2, test_amount2, greedy_cnt2, optimal_cnt2 = is_canonical_coin_system(non_canonical_coins)
    
    if not is_canonical2:
        print("Система НЕ является канонической")
        print(f"  Пример: сумма {test_amount2}")
        print(f"  Жадный алгоритм: {greedy_cnt2} монет")
        print(f"  Оптимальное решение: {optimal_cnt2} монет")
    
    result2, total_coins2 = coin_change_greedy(non_canonical_coins, amount2)
    
    print(f"\nРазмен суммы {amount2} (жадный алгоритм):")
    if result2 is None:
        print("  Невозможно разменять данную сумму")
    else:
        for coin, count in result2:
            print(f"  Монета {coin:3d}: {count} шт.")
        print(f"\n  Всего монет: {total_coins2}")
        
        # Показываем оптимальное решение
        print(f"\n  Оптимальное решение для {amount2}:")
        print(f"    {amount2} = 3 + 3 (2 монеты)")


def demonstrate_huffman_coding():
    """Демонстрация алгоритма Хаффмана"""
    print("\n\n4. Алгоритм Хаффмана (Huffman Coding)")
    print("-" * 40)
    
    # Частоты символов
    frequencies = {
        'a': 45,    # Наиболее частый
        'b': 13,
        'c': 12,
        'd': 16,
        'e': 9,     # Наименее частый
        'f': 5,
    }
    
    print("Частоты символов:")
    total = sum(frequencies.values())
    for symbol, freq in frequencies.items():
        percentage = (freq / total) * 100
        print(f"  '{symbol}': {freq} ({percentage:.1f}%)")
    
    # Строим коды Хаффмана
    codes = huffman_coding(frequencies)
    
    print("\nКоды Хаффмана:")
    for symbol, code in sorted(codes.items(), key=lambda x: len(x[1])):
        print(f"  '{symbol}': {code}")
    
    # Пример кодирования строки
    test_string = "abacab"
    print(f"\nПример кодирования строки: '{test_string}'")
    
    encoded = ""
    for char in test_string:
        encoded += codes[char]
    
    print(f"Закодированная строка: {encoded}")
    
    # Вычисляем среднюю длину кода
    avg_length = 0
    for symbol, freq in frequencies.items():
        code_length = len(codes[symbol])
        probability = freq / total
        avg_length += code_length * probability
    
    print(f"\nСтатистика:")
    print(f"  Средняя длина кода: {avg_length:.3f} бит/символ")
    print(f"  Длина при равномерном кодировании: {len(bin(len(frequencies)-1))-2} бит/символ")
    print(f"  Эффективность сжатия: {((len(bin(len(frequencies)-1))-2 - avg_length) / (len(bin(len(frequencies)-1))-2))*100:.1f}%")


def main():
    """Основная функция программы"""
    print("Лабораторная работа 8: Жадные алгоритмы")
    print("=" * 60)
    
    # Демонстрация всех алгоритмов
    demonstrate_interval_scheduling()
    demonstrate_fractional_knapsack()
    demonstrate_coin_change()
    demonstrate_huffman_coding()
    
    print("\n" + "=" * 60)
    print("5. Анализ производительности и корректности")
    print("=" * 60)
    
    # Запуск анализа
    import analysis
    analysis.compare_knapsack_solutions()
    analysis.test_interval_scheduling_performance()
    analysis.test_huffman_performance()
    analysis.test_coin_systems()
    
    # Визуализация дерева Хаффмана
    frequencies = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
    codes = huffman_coding(frequencies)
    analysis.visualize_huffman_tree(codes)
    
    # Анализ корректности
    analysis.analyze_greedy_correctness()
    
    print("\n" + "=" * 60)
    print("Выводы:")
    print("-" * 60)
    print("1. Жадные алгоритмы эффективны для задач с оптимальной подструктурой")
    print("2. Задача о выборе заявок и непрерывный рюкзак - примеры задач,")
    print("   где жадный подход всегда дает оптимальное решение")
    print("3. Задача о размене монет демонстрирует ограничения жадных алгоритмов")
    print("4. Алгоритм Хаффмана - классический пример оптимального жадного алгоритма")
    print("5. Для проверки корректности жадного алгоритма необходимо:")
    print("   - Доказать свойство жадного выбора")
    print("   - Доказать свойство оптимальной подструктуры")


if __name__ == "__main__":
    main()