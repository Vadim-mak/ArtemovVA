import unittest
from greedy_algorithms import (
    interval_scheduling,
    fractional_knapsack,
    coin_change_greedy,
    huffman_coding,
    is_canonical_coin_system
)


class TestIntervalScheduling(unittest.TestCase):
    """Тесты для задачи о выборе заявок"""
    
    def test_empty_intervals(self):
        """Тест с пустым списком интервалов"""
        self.assertEqual(interval_scheduling([]), [])
    
    def test_single_interval(self):
        """Тест с одним интервалом"""
        intervals = [(1, 3)]
        self.assertEqual(interval_scheduling(intervals), [(1, 3)])
    
    def test_non_overlapping_intervals(self):
        """Тест с непересекающимися интервалами"""
        intervals = [(1, 2), (3, 4), (5, 6)]
        result = interval_scheduling(intervals)
        self.assertEqual(len(result), 3)
        self.assertEqual(result, intervals)
    
    def test_overlapping_intervals(self):
        """Тест с пересекающимися интервалами"""
        intervals = [(1, 4), (2, 5), (3, 6), (5, 7)]
        result = interval_scheduling(intervals)
        # Должны быть выбраны (1, 4) и (5, 7)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [(1, 4), (5, 7)])
    
    def test_greedy_property(self):
        """Проверка свойства жадного выбора"""
        intervals = [(1, 3), (2, 4), (3, 5), (4, 6)]
        result = interval_scheduling(intervals)
        # Первый выбранный интервал должен заканчиваться раньше всех
        self.assertEqual(result[0][1], 3)


class TestFractionalKnapsack(unittest.TestCase):
    """Тесты для задачи о непрерывном рюкзаке"""
    
    def test_empty_items(self):
        """Тест с пустым списком предметов"""
        total_value, selected = fractional_knapsack([], 10)
        self.assertEqual(total_value, 0.0)
        self.assertEqual(selected, [])
    
    def test_zero_capacity(self):
        """Тест с нулевой вместимостью"""
        items = [(10, 60), (20, 100)]
        total_value, selected = fractional_knapsack(items, 0)
        self.assertEqual(total_value, 0.0)
        self.assertEqual(len(selected), 0)
    
    def test_single_item_fits(self):
        """Тест с одним предметом, который помещается"""
        items = [(10, 60)]
        total_value, selected = fractional_knapsack(items, 15)
        self.assertAlmostEqual(total_value, 60.0)
        self.assertEqual(len(selected), 1)
    
    def test_single_item_partial(self):
        """Тест с одним предметом, берем часть"""
        items = [(10, 60)]  # удельная стоимость: 6.0
        total_value, selected = fractional_knapsack(items, 5)
        self.assertAlmostEqual(total_value, 30.0)  # 5 * 6.0
    
    def test_multiple_items(self):
        """Тест с несколькими предметами"""
        items = [(10, 60), (20, 100), (30, 120)]
        total_value, selected = fractional_knapsack(items, 50)
        # Ожидаемый результат: взять полностью первые два предмета
        # и часть третьего
        self.assertGreater(total_value, 0)
        self.assertLessEqual(len(selected), 3)
    
    def test_greedy_property(self):
        """Проверка, что берутся предметы с наибольшей удельной стоимостью"""
        items = [(10, 20), (5, 30), (15, 25)]  # удельные: 2.0, 6.0, 1.67
        total_value, selected = fractional_knapsack(items, 15)
        # Должен быть выбран предмет с удельной стоимостью 6.0 (5,30)
        # и часть предмета с удельной стоимостью 2.0 (10,20)
        self.assertAlmostEqual(total_value, 30 + 10 * 2.0)  # 30 + 20 = 50


class TestCoinChange(unittest.TestCase):
    """Тесты для задачи о размене монет"""
    
    def test_empty_coins(self):
        """Тест с пустым списком монет"""
        result, total = coin_change_greedy([], 10)
        self.assertIsNone(result)
        self.assertEqual(total, 10)
    
    def test_zero_amount(self):
        """Тест с нулевой суммой"""
        coins = [1, 5, 10]
        result, total = coin_change_greedy(coins, 0)
        self.assertEqual(result, [])
        self.assertEqual(total, 0)
    
    def test_exact_change(self):
        """Тест точного размена"""
        coins = [1, 5, 10, 25]
        result, total = coin_change_greedy(coins, 36)
        # 25 + 10 + 1 = 36
        self.assertIsNotNone(result)
        self.assertEqual(total, 3)
    
    def test_impossible_change(self):
        """Тест невозможного размена (минимальная монета больше суммы)"""
        coins = [5, 10, 25]
        result, total = coin_change_greedy(coins, 3)
        self.assertIsNone(result)
    
    def test_canonical_system(self):
        """Тест канонической системы"""
        coins = [1, 5, 10, 25, 50, 100]
        is_canonical, _, _, _ = is_canonical_coin_system(coins)
        self.assertTrue(is_canonical)
    
    def test_non_canonical_system(self):
        """Тест неканонической системы"""
        coins = [1, 3, 4]
        is_canonical, amount, greedy_cnt, optimal_cnt = is_canonical_coin_system(coins)
        self.assertFalse(is_canonical)
        # Для суммы 6: жадный дает 4+1+1 (3 монеты), оптимальный 3+3 (2 монеты)
        self.assertEqual(amount, 6)
        self.assertEqual(greedy_cnt, 3)
        self.assertEqual(optimal_cnt, 2)


class TestHuffmanCoding(unittest.TestCase):
    """Тесты для алгоритма Хаффмана"""
    
    def test_empty_frequencies(self):
        """Тест с пустым словарем частот"""
        codes = huffman_coding({})
        self.assertEqual(codes, {})
    
    def test_single_symbol(self):
        """Тест с одним символом"""
        frequencies = {'a': 100}
        codes = huffman_coding(frequencies)
        self.assertEqual(codes, {'a': '0'})
    
    def test_two_symbols(self):
        """Тест с двумя символами"""
        frequencies = {'a': 60, 'b': 40}
        codes = huffman_coding(frequencies)
        # Должны быть коды '0' и '1' (или '1' и '0')
        self.assertEqual(len(codes), 2)
        self.assertEqual(set(codes.values()), {'0', '1'})
    
    def test_prefix_property(self):
        """Проверка свойства префиксности"""
        frequencies = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
        codes = huffman_coding(frequencies)
        
        # Проверяем, что ни один код не является префиксом другого
        all_codes = list(codes.values())
        for i, code1 in enumerate(all_codes):
            for code2 in all_codes[i+1:]:
                self.assertFalse(code1.startswith(code2))
                self.assertFalse(code2.startswith(code1))
    
    def test_optimality(self):
        """Проверка оптимальности (меньшая частота -> большая длина кода)"""
        frequencies = {'a': 50, 'b': 30, 'c': 20}
        codes = huffman_coding(frequencies)
        
        # Символ с наибольшей частотой должен иметь самый короткий код
        lengths = {symbol: len(code) for symbol, code in codes.items()}
        self.assertEqual(lengths['a'], 1)  # Наиболее частый
        self.assertGreater(lengths['b'], 1)
        self.assertGreater(lengths['c'], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)