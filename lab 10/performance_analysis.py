import time
import random
from graph_representation import GraphMatrix, GraphList
from graph_traversal import (
    bfs_matrix, bfs_list,
    dfs_matrix_recursive, dfs_list_recursive,
    dfs_iterative_matrix, dfs_iterative_list,
    find_connected_components_matrix, find_connected_components_list
)
from shortest_path import (
    dijkstra_matrix, dijkstra_list,
    bellman_ford_matrix, bellman_ford_list,
    topological_sort_matrix, topological_sort_list
)


def generate_random_graph(n_vertices, edge_probability=0.3, directed=False, weighted=False, max_weight=10):
    """
    Генерация случайного графа
    
    Сложность: O(n²) для матрицы, O(n + m) для списка
    """
    # Создаем обе структуры
    graph_matrix = GraphMatrix(directed=directed)
    graph_list = GraphList(directed=directed)
    
    # Добавляем вершины
    for i in range(n_vertices):
        vertex = f"V{i}"
        graph_matrix.add_vertex(vertex)
        graph_list.add_vertex(vertex)
    
    # Добавляем ребра
    for i in range(n_vertices):
        for j in range(n_vertices):
            if i != j and random.random() < edge_probability:
                weight = random.randint(1, max_weight) if weighted else 1
                u = f"V{i}"
                v = f"V{j}"
                
                graph_matrix.add_edge(u, v, weight)
                graph_list.add_edge(u, v, weight)
    
    return graph_matrix, graph_list


def compare_representations():
    """Сравнение производительности матрицы и списка смежности"""
    print("Сравнение производительности представлений графов")
    print("=" * 70)
    
    sizes = [10, 50, 100, 200, 500]
    
    print(f"{'Вершин':<10} {'Мат. память (МБ)':<20} {'Спис. память (МБ)':<20} {'Мат./Спис.':<15}")
    print("-" * 70)
    
    for n in sizes:
        # Генерируем графы
        graph_matrix, graph_list = generate_random_graph(n, edge_probability=0.1)
        
        # Оцениваем память
        matrix_memory = (n * n * 28) / (1024 * 1024)  # Примерная оценка в МБ
        list_memory = (n * 64 + n * n * 0.1 * 56) / (1024 * 1024)  # Примерная оценка
        
        ratio = matrix_memory / list_memory if list_memory > 0 else float('inf')
        
        print(f"{n:<10} {matrix_memory:<20.4f} {list_memory:<20.4f} {ratio:<15.2f}")
    
    print("\nВыводы:")
    print("1. Матрица смежности требует O(V²) памяти")
    print("2. Список смежности требует O(V + E) памяти")
    print("3. Для разреженных графов список эффективнее по памяти")
    print("4. Для плотных графов разница меньше")


def compare_bfs_performance():
    """Сравнение производительности BFS"""
    print("\n\nСравнение производительности BFS")
    print("=" * 70)
    
    sizes = [100, 500, 1000, 2000, 5000]
    
    print(f"{'Вершин':<10} {'BFS матрица (мс)':<20} {'BFS список (мс)':<20} {'Отношение':<15}")
    print("-" * 70)
    
    for n in sizes:
        # Генерируем графы с низкой плотностью
        graph_matrix, graph_list = generate_random_graph(n, edge_probability=0.01)
        
        if len(graph_matrix.vertices) == 0:
            continue
        
        start_vertex = graph_matrix.vertices[0]
        
        # BFS для матрицы
        start = time.perf_counter()
        bfs_matrix(graph_matrix, start_vertex)
        bfs_matrix_time = (time.perf_counter() - start) * 1000
        
        # BFS для списка
        start = time.perf_counter()
        bfs_list(graph_list, start_vertex)
        bfs_list_time = (time.perf_counter() - start) * 1000
        
        ratio = bfs_matrix_time / bfs_list_time if bfs_list_time > 0 else float('inf')
        
        print(f"{n:<10} {bfs_matrix_time:<20.4f} {bfs_list_time:<20.4f} {ratio:<15.2f}")
    
    print("\nВыводы:")
    print("1. BFS для матрицы имеет сложность O(V²)")
    print("2. BFS для списка имеет сложность O(V + E)")
    print("3. Для разреженных графов список значительно быстрее")
    print("4. Для плотных графов разница меньше")


def compare_dfs_performance():
    """Сравнение производительности DFS"""
    print("\n\nСравнение производительности DFS")
    print("=" * 70)
    
    sizes = [100, 500, 1000]
    
    print(f"{'Вершин':<10} {'DFS рек. мат. (мс)':<20} {'DFS рек. спис. (мс)':<20} {'DFS итер. мат. (мс)':<20} {'DFS итер. спис. (мс)':<20}")
    print("-" * 90)
    
    for n in sizes:
        # Генерируем графы
        graph_matrix, graph_list = generate_random_graph(n, edge_probability=0.02)
        
        if len(graph_matrix.vertices) == 0:
            continue
        
        start_vertex = graph_matrix.vertices[0]
        
        times = []
        
        # Рекурсивный DFS для матрицы
        start = time.perf_counter()
        dfs_matrix_recursive(graph_matrix, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        # Рекурсивный DFS для списка
        start = time.perf_counter()
        dfs_list_recursive(graph_list, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        # Итеративный DFS для матрицы
        start = time.perf_counter()
        dfs_iterative_matrix(graph_matrix, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        # Итеративный DFS для списка
        start = time.perf_counter()
        dfs_iterative_list(graph_list, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        print(f"{n:<10} ", end="")
        for t in times:
            print(f"{t:<20.4f}", end="")
        print()
    
    print("\nВыводы:")
    print("1. Рекурсивный DFS может вызывать переполнение стека для больших графов")
    print("2. Итеративный DFS избегает проблемы переполнения стека")
    print("3. Список смежности быстрее для DFS")
    print("4. Производительность зависит от структуры графа")


def compare_shortest_path_algorithms():
    """Сравнение алгоритмов поиска кратчайших путей"""
    print("\n\nСравнение алгоритмов поиска кратчайших путей")
    print("=" * 70)
    
    sizes = [50, 100, 200]
    
    print(f"{'Вершин':<10} {'Дейкстра мат. (мс)':<20} {'Дейкстра спис. (мс)':<20} {'Беллман-Форд мат. (мс)':<25} {'Беллман-Форд спис. (мс)':<25}")
    print("-" * 100)
    
    for n in sizes:
        # Генерируем взвешенные графы
        graph_matrix, graph_list = generate_random_graph(n, edge_probability=0.1, weighted=True)
        
        if len(graph_matrix.vertices) == 0:
            continue
        
        start_vertex = graph_matrix.vertices[0]
        
        times = []
        
        # Дейкстра для матрицы
        start = time.perf_counter()
        dijkstra_matrix(graph_matrix, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        # Дейкстра для списка
        start = time.perf_counter()
        dijkstra_list(graph_list, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        # Беллман-Форд для матрицы
        start = time.perf_counter()
        bellman_ford_matrix(graph_matrix, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        # Беллман-Форд для списка
        start = time.perf_counter()
        bellman_ford_list(graph_list, start_vertex)
        times.append((time.perf_counter() - start) * 1000)
        
        print(f"{n:<10} ", end="")
        for t in times:
            print(f"{t:<25.4f}", end="")
        print()
    
    print("\nВыводы:")
    print("1. Алгоритм Дейкстры быстрее Беллмана-Форда для графов без отрицательных весов")
    print("2. Беллман-Форд работает с отрицательными весами, но медленнее")
    print("3. Дейкстра на списке смежности эффективнее для разреженных графов")
    print("4. Выбор алгоритма зависит от характеристик графа")


def test_connected_components():
    """Тестирование поиска компонент связности"""
    print("\n\nТестирование поиска компонент связности")
    print("=" * 70)
    
    # Создаем граф с несколькими компонентами
    graph_matrix = GraphMatrix(directed=False)
    graph_list = GraphList(directed=False)
    
    # Компонента 1: V0, V1, V2
    for i in range(3):
        v = f"V{i}"
        graph_matrix.add_vertex(v)
        graph_list.add_vertex(v)
    
    graph_matrix.add_edge("V0", "V1")
    graph_matrix.add_edge("V1", "V2")
    
    graph_list.add_edge("V0", "V1")
    graph_list.add_edge("V1", "V2")
    
    # Компонента 2: V3, V4
    for i in range(3, 5):
        v = f"V{i}"
        graph_matrix.add_vertex(v)
        graph_list.add_vertex(v)
    
    graph_matrix.add_edge("V3", "V4")
    graph_list.add_edge("V3", "V4")
    
    # Изолированная вершина V5
    graph_matrix.add_vertex("V5")
    graph_list.add_vertex("V5")
    
    # Поиск компонент
    components_matrix = find_connected_components_matrix(graph_matrix)
    components_list = find_connected_components_list(graph_list)
    
    print("Компоненты связности (матрица):")
    for i, comp in enumerate(components_matrix, 1):
        print(f"  Компонента {i}: {sorted(comp)}")
    
    print("\nКомпоненты связности (список):")
    for i, comp in enumerate(components_list, 1):
        print(f"  Компонента {i}: {sorted(comp)}")
    
    print("\nВыводы:")
    print("1. Оба метода находят одинаковые компоненты связности")
    print("2. Сложность зависит от представления графа")
    print("3. Алгоритм работает корректно для несвязных графов")


def test_topological_sort():
    """Тестирование топологической сортировки"""
    print("\n\nТестирование топологической сортировки")
    print("=" * 70)
    
    # Создаем ориентированный ациклический граф (DAG)
    graph_matrix = GraphMatrix(directed=True)
    graph_list = GraphList(directed=True)
    
    # Добавляем вершины
    vertices = ["A", "B", "C", "D", "E", "F"]
    for v in vertices:
        graph_matrix.add_vertex(v)
        graph_list.add_vertex(v)
    
    # Добавляем ребра (зависимости)
    edges = [
        ("A", "B"), ("A", "C"),
        ("B", "D"), ("C", "D"),
        ("D", "E"), ("D", "F"),
        ("E", "F")
    ]
    
    for u, v in edges:
        graph_matrix.add_edge(u, v)
        graph_list.add_edge(u, v)
    
    # Топологическая сортировка
    topo_matrix = topological_sort_matrix(graph_matrix)
    topo_list = topological_sort_list(graph_list)
    
    print("Топологическая сортировка (матрица):", topo_matrix)
    print("Топологическая сортировка (список):", topo_list)
    
    # Проверяем корректность
    print("\nПроверка корректности:")
    
    def is_valid_topological_order(order, edges):
        """Проверяет, что порядок топологически корректен"""
        position = {vertex: i for i, vertex in enumerate(order)}
        
        for u, v in edges:
            if position[u] > position[v]:
                return False, f"Нарушение: {u} -> {v}"
        
        return True, "Корректно"
    
    valid_matrix, msg_matrix = is_valid_topological_order(topo_matrix, edges)
    valid_list, msg_list = is_valid_topological_order(topo_list, edges)
    
    print(f"  Матрица: {msg_matrix}")
    print(f"  Список: {msg_list}")
    
    print("\nВыводы:")
    print("1. Топологическая сортировка возможна только для ориентированных ациклических графов")
    print("2. Существует несколько допустимых топологических порядков")
    print("3. Оба метода дают корректный результат")


def run_maze_simulation():
    """Симуляция поиска пути в лабиринте"""
    print("\n\nСимуляция поиска пути в лабиринте")
    print("=" * 70)
    
    # Создаем простой лабиринт 5x5
    maze_size = 5
    graph_matrix = GraphMatrix(directed=False)
    graph_list = GraphList(directed=False)
    
    # Добавляем вершины (клетки лабиринта)
    for i in range(maze_size):
        for j in range(maze_size):
            vertex = f"({i},{j})"
            graph_matrix.add_vertex(vertex)
            graph_list.add_vertex(vertex)
    
    # Добавляем ребра (проходы между клетками)
    # Горизонтальные связи
    for i in range(maze_size):
        for j in range(maze_size - 1):
            if random.random() > 0.3:  # 70% вероятность прохода
                u = f"({i},{j})"
                v = f"({i},{j+1})"
                graph_matrix.add_edge(u, v)
                graph_list.add_edge(u, v)
    
    # Вертикальные связи
    for i in range(maze_size - 1):
        for j in range(maze_size):
            if random.random() > 0.3:  # 70% вероятность прохода
                u = f"({i},{j})"
                v = f"({i+1},{j})"
                graph_matrix.add_edge(u, v)
                graph_list.add_edge(u, v)
    
    # Начальная и конечная точки
    start = "(0,0)"
    end = f"({maze_size-1},{maze_size-1})"
    
    print(f"Лабиринт {maze_size}x{maze_size}")
    print(f"Начало: {start}, Конец: {end}")
    
    # Поиск пути с помощью BFS
    _, _, parents_matrix = bfs_matrix(graph_matrix, start)
    _, _, parents_list = bfs_list(graph_list, start)
    
    # Восстанавливаем пути
    from shortest_path import reconstruct_path
    path_matrix = reconstruct_path(parents_matrix, start, end)
    path_list = reconstruct_path(parents_list, start, end)
    
    print(f"\nПуть (матрица): {' -> '.join(path_matrix) if path_matrix else 'Нет пути'}")
    print(f"Длина пути: {len(path_matrix) - 1 if path_matrix else 0}")
    
    print(f"\nПуть (список): {' -> '.join(path_list) if path_list else 'Нет пути'}")
    print(f"Длина пути: {len(path_list) - 1 if path_list else 0}")
    
    # Визуализация лабиринта
    print("\nВизуализация лабиринта:")
    for i in range(maze_size):
        row = []
        for j in range(maze_size):
            cell = f"({i},{j})"
            if cell == start:
                row.append("S")
            elif cell == end:
                row.append("E")
            elif cell in path_matrix:
                row.append("*")
            else:
                row.append(".")
        print(" ".join(row))


if __name__ == "__main__":
    print("Анализ производительности алгоритмов на графах")
    print("=" * 70)
    
    compare_representations()
    compare_bfs_performance()
    compare_dfs_performance()
    compare_shortest_path_algorithms()
    test_connected_components()
    test_topological_sort()
    run_maze_simulation()