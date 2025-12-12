import unittest
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


class TestFibonacci(unittest.TestCase):
    """Тесты для чисел Фибоначчи"""
    
    def test_fibonacci_base_cases(self):
        """Тест базовых случаев"""
        self.assertEqual(fibonacci_naive(0), 0)
        self.assertEqual(fibonacci_naive(1), 1)
        
        self.assertEqual(fibonacci_memoization(0), 0)
        self.assertEqual(fibonacci_memoization(1), 1)
        
        self.assertEqual(fibonacci_tabulation(0), 0)
        self.assertEqual(fibonacci_tabulation(1), 1)
        
        self.assertEqual(fibonacci_optimized(0), 0)
        self.assertEqual(fibonacci_optimized(1), 1)
    
    def test_fibonacci_small_values(self):
        """Тест малых значений"""
        test_cases = [
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55)
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(fibonacci_naive(n), expected)
                self.assertEqual(fibonacci_memoization(n), expected)
                self.assertEqual(fibonacci_tabulation(n), expected)
                self.assertEqual(fibonacci_optimized(n), expected)
    
    def test_fibonacci_consistency(self):
        """Проверка согласованности методов"""
        for n in range(0, 15):
            naive = fibonacci_naive(n)
            memo = fibonacci_memoization(n)
            tab = fibonacci_tabulation(n)
            opt = fibonacci_optimized(n)
            
            self.assertEqual(naive, memo)
            self.assertEqual(memo, tab)
            self.assertEqual(tab, opt)


class TestKnapsack(unittest.TestCase):
    """Тесты для задачи о рюкзаке"""
    
    def test_knapsack_empty(self):
        """Тест с пустыми входными данными"""
        self.assertEqual(knapsack_01([], [], 10), 0)
        self.assertEqual(knapsack_01_optimized([], [], 10), 0)
    
    def test_knapsack_zero_capacity(self):
        """Тест с нулевой вместимостью"""
        weights = [1, 2, 3]
        values = [10, 20, 30]
        self.assertEqual(knapsack_01(weights, values, 0), 0)
        self.assertEqual(knapsack_01_optimized(weights, values, 0), 0)
    
    def test_knapsack_simple_cases(self):
        """Тест простых случаев"""
        # Все предметы помещаются
        weights = [1, 2, 3]
        values = [10, 20, 30]
        capacity = 6
        expected = 60  # 10 + 20 + 30
        
        self.assertEqual(knapsack_01(weights, values, capacity), expected)
        self.assertEqual(knapsack_01_optimized(weights, values, capacity), expected)
        
        # Только часть предметов помещается
        capacity = 3
        expected = 40  # предметы 1 и 2 (10 + 30? ошибка в расчете)
        # Правильно: предметы 1 (10) и 3 (30) = 40, или 2 (20) и 1 (10) = 30
        # На самом деле: вес 1+3=4 > 3, вес 2+1=3, стоимость 20+10=30
        
        result1 = knapsack_01(weights, values, capacity)
        result2 = knapsack_01_optimized(weights, values, capacity)
        self.assertEqual(result1, result2)
    
    def test_knapsack_consistency(self):
        """Проверка согласованности методов"""
        import random
        
        for _ in range(10):
            n = random.randint(1, 10)
            weights = [random.randint(1, 10) for _ in range(n)]
            values = [random.randint(1, 20) for _ in range(n)]
            capacity = random.randint(1, 20)
            
            result1 = knapsack_01(weights, values, capacity)
            result2 = knapsack_01_optimized(weights, values, capacity)
            
            self.assertEqual(result1, result2)


class TestLCS(unittest.TestCase):
    """Тесты для наибольшей общей подпоследовательности"""
    
    def test_lcs_empty_strings(self):
        """Тест с пустыми строками"""
        self.assertEqual(longest_common_subsequence("", ""), 0)
        self.assertEqual(longest_common_subsequence("abc", ""), 0)
        self.assertEqual(longest_common_subsequence("", "xyz"), 0)
        
        length, lcs = lcs_with_reconstruction("", "")
        self.assertEqual(length, 0)
        self.assertEqual(lcs, "")
    
    def test_lcs_identical_strings(self):
        """Тест с одинаковыми строками"""
        str1 = "abcdef"
        str2 = "abcdef"
        
        length = longest_common_subsequence(str1, str2)
        self.assertEqual(length, len(str1))
        
        length2, lcs = lcs_with_reconstruction(str1, str2)
        self.assertEqual(length2, len(str1))
        self.assertEqual(lcs, str1)
    
    def test_lcs_no_common(self):
        """Тест без общих символов"""
        str1 = "abc"
        str2 = "def"
        
        length = longest_common_subsequence(str1, str2)
        self.assertEqual(length, 0)
        
        length2, lcs = lcs_with_reconstruction(str1, str2)
        self.assertEqual(length2, 0)
        self.assertEqual(lcs, "")
    
    def test_lcs_standard_cases(self):
        """Тест стандартных случаев"""
        test_cases = [
            ("ABCDGH", "AEDFHR", 3, "ADH"),
            ("AGGTAB", "GXTXAYB", 4, "GTAB"),
            ("ABCBDAB", "BDCABA", 4, "BCBA"),  # или BDAB
        ]
        
        for str1, str2, expected_len, expected_lcs in test_cases:
            with self.subTest(str1=str1, str2=str2):
                length = longest_common_subsequence(str1, str2)
                self.assertEqual(length, expected_len)
                
                length2, lcs = lcs_with_reconstruction(str1, str2)
                self.assertEqual(length2, expected_len)
                self.assertEqual(len(lcs), expected_len)
    
    def test_lcs_consistency(self):
        """Проверка согласованности методов"""
        str1 = "thisisatest"
        str2 = "testing123testing"
        
        length1 = longest_common_subsequence(str1, str2)
        length2, lcs = lcs_with_reconstruction(str1, str2)
        
        self.assertEqual(length1, length2)
        self.assertEqual(len(lcs), length1)


class TestCoinChange(unittest.TestCase):
    """Тесты для задачи о размене монет"""
    
    def test_coin_change_zero_amount(self):
        """Тест с нулевой суммой"""
        coins = [1, 2, 5]
        
        min_coins = coin_change_min_coins(coins, 0)
        self.assertEqual(min_coins, 0)
        
        ways = coin_change_ways(coins, 0)
        self.assertEqual(ways, 1)  # 1 способ - не брать ни одной монеты
    
    def test_coin_change_impossible(self):
        """Тест невозможного размена"""
        coins = [2, 5, 10]
        amount = 3
        
        min_coins = coin_change_min_coins(coins, amount)
        self.assertEqual(min_coins, -1)
        
        ways = coin_change_ways(coins, amount)
        self.assertEqual(ways, 0)
    
    def test_coin_change_standard_cases(self):
        """Тест стандартных случаев"""
        coins = [1, 2, 5]
        
        # Минимальное количество монет
        test_cases_min = [
            (1, 1),   # 1
            (2, 1),   # 2
            (3, 2),   # 2 + 1
            (5, 1),   # 5
            (6, 2),   # 5 + 1
            (7, 2),   # 5 + 2
            (8, 3),   # 5 + 2 + 1
            (11, 3),  # 5 + 5 + 1
        ]
        
        for amount, expected in test_cases_min:
            with self.subTest(amount=amount):
                result = coin_change_min_coins(coins, amount)
                self.assertEqual(result, expected)
        
        # Количество способов
        test_cases_ways = [
            (1, 1),   # [1]
            (2, 2),   # [2], [1,1]
            (3, 2),   # [2,1], [1,1,1]
            (4, 3),   # [2,2], [2,1,1], [1,1,1,1]
            (5, 4),   # [5], [2,2,1], [2,1,1,1], [1,1,1,1,1]
        ]
        
        for amount, expected in test_cases_ways:
            with self.subTest(amount=amount):
                result = coin_change_ways(coins, amount)
                self.assertEqual(result, expected)
    
    def test_coin_change_different_order(self):
        """Тест с разным порядком монет"""
        coins1 = [1, 2, 5]
        coins2 = [5, 2, 1]
        amount = 7
        
        result1 = coin_change_min_coins(coins1, amount)
        result2 = coin_change_min_coins(coins2, amount)
        self.assertEqual(result1, result2)
        
        ways1 = coin_change_ways(coins1, amount)
        ways2 = coin_change_ways(coins2, amount)
        self.assertEqual(ways1, ways2)


class TestEditDistance(unittest.TestCase):
    """Тесты для расстояния Левенштейна"""
    
    def test_edit_distance_empty_strings(self):
        """Тест с пустыми строками"""
        self.assertEqual(edit_distance("", ""), 0)
        self.assertEqual(edit_distance("abc", ""), 3)
        self.assertEqual(edit_distance("", "xyz"), 3)
    
    def test_edit_distance_identical_strings(self):
        """Тест с одинаковыми строками"""
        str1 = "abcdef"
        self.assertEqual(edit_distance(str1, str1), 0)
    
    def test_edit_distance_standard_cases(self):
        """Тест стандартных случаев"""
        test_cases = [
            ("kitten", "sitting", 3),
            ("sunday", "saturday", 3),
            ("intention", "execution", 5),
            ("algorithm", "logarithm", 3),
            ("cat", "cut", 1),
            ("book", "back", 2),
        ]
        
        for str1, str2, expected in test_cases:
            with self.subTest(str1=str1, str2=str2):
                result = edit_distance(str1, str2)
                self.assertEqual(result, expected)
    
    def test_edit_distance_symmetry(self):
        """Проверка симметричности"""
        str1 = "hello"
        str2 = "world"
        
        dist1 = edit_distance(str1, str2)
        dist2 = edit_distance(str2, str1)
        
        self.assertEqual(dist1, dist2)


class TestMatrixChainOrder(unittest.TestCase):
    """Тесты для перемножения матриц"""
    
    def test_matrix_chain_small(self):
        """Тест малого количества матриц"""
        # 2 матрицы: 10×20 и 20×30
        dims = [10, 20, 30]
        min_cost, split = matrix_chain_order(dims)
        self.assertEqual(min_cost, 10 * 20 * 30)  # 6000
        
        # 3 матрицы: 10×20, 20×30, 30×40
        dims = [10, 20, 30, 40]
        min_cost, split = matrix_chain_order(dims)
        # (10×20×30) + (10×30×40) = 6000 + 12000 = 18000
        # или (20×30×40) + (10×20×40) = 24000 + 8000 = 32000
        # Минимум: 18000
        self.assertEqual(min_cost, 18000)
    
    def test_matrix_chain_standard(self):
        """Тест стандартного случая"""
        # Пример из книги Кормена: A1..A6
        dims = [30, 35, 15, 5, 10, 20, 25]
        min_cost, split = matrix_chain_order(dims)
        
        # Ожидаемый результат: 15125
        self.assertEqual(min_cost, 15125)


class TestLIS(unittest.TestCase):
    """Тесты для наибольшей возрастающей подпоследовательности"""
    
    def test_lis_empty(self):
        """Тест с пустой последовательностью"""
        self.assertEqual(longest_increasing_subsequence([]), 0)
    
    def test_lis_single_element(self):
        """Тест с одним элементом"""
        self.assertEqual(longest_increasing_subsequence([5]), 1)
    
    def test_lis_sorted_ascending(self):
        """Тест с отсортированной по возрастанию последовательностью"""
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(longest_increasing_subsequence(nums), 5)
    
    def test_lis_sorted_descending(self):
        """Тест с отсортированной по убыванию последовательностью"""
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(longest_increasing_subsequence(nums), 1)
    
    def test_lis_standard_cases(self):
        """Тест стандартных случаев"""
        test_cases = [
            ([10, 22, 9, 33, 21, 50, 41, 60, 80], 6),
            ([3, 10, 2, 1, 20], 3),
            ([50, 3, 10, 7, 40, 80], 4),
            ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                result = longest_increasing_subsequence(nums)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)