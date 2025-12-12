# recursion_tasks.py
# Дополнительные задачи: рекурсивный бинарный поиск и Ханойские башни (печать перемещений).

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Рекурсивный бинарный поиск в отсортированном массиве.
    Сложность: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1  # не найдено
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def hanoi_moves(n, source='A', target='C', aux='B', moves=None):
    """
    Решение задачи Ханойских башен: возвращает список кортежей (from, to).
    Глубина рекурсии: O(n)
    Число перемещений: 2^n - 1
    """
    if moves is None:
        moves = []
    if n == 0:
        return moves
    # переместить n-1 дисков со source на aux
    hanoi_moves(n - 1, source, aux, target, moves)
    # переместить 1 диск source -> target
    moves.append((source, target))
    # переместить n-1 дисков с aux на target
    hanoi_moves(n - 1, aux, target, source, moves)
    return moves

if __name__ == "__main__":
    arr = list(range(0, 21))  # пример для бинарного поиска
    print("binary_search_recursive(arr, 7) ->", binary_search_recursive(arr, 7))
    moves = hanoi_moves(3)
    print("Hanoi moves for n=3 (count):", len(moves))
    for i, m in enumerate(moves, 1):
        print(f"{i}. {m[0]} -> {m[1]}")
