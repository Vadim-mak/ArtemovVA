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
    topological_sort_matrix, topological_sort_list,
    reconstruct_path
)
import performance_analysis


def demonstrate_graph_representations():
    """Демонстрация различных представлений графов"""
    print("1. Представления графов")
    print("-" * 40)
    
    # Создаем граф с матрицей смежности
    print("Матрица смежности:")
    graph_matrix = GraphMatrix(directed=False)
    
    # Добавляем вершины
    vertices = ["A", "B", "C", "D", "E"]
    for v in vertices:
        graph_matrix.add_vertex(v)
    
    # Добавляем ребра
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    for u, v in edges:
        graph_matrix.add_edge(u, v)
    
    print(graph_matrix)
    
    # Создаем тот же граф со списком смежности
    print("\nСписок смежности:")
    graph_list = GraphList(directed=False)
    
    for v in vertices:
        graph_list.add_vertex(v)
    
    for u, v in edges:
        graph_list.add_edge(u, v)
    
    print(graph_list)
    
    print("\nСравнение:")
    print("  Матрица: быстрая проверка ребра O(1), память O(V²)")
    print("  Список: эффективная память O(V+E), быстрый обход соседей")


def demonstrate_bfs_dfs():
    """Демонстрация обходов графов"""
    print("\n\n2. Обход графов (BFS и DFS)")
    print("-" * 40)
    
    # Создаем граф
    graph_matrix = GraphMatrix(directed=False)
    graph_list = GraphList(directed=False)
    
    vertices = ["A", "B", "C", "D", "E", "F", "G"]
    for v in vertices:
        graph_matrix.add_vertex(v)
        graph_list.add_vertex(v)
    
    edges = [
        ("A", "B"), ("A", "C"),
        ("B", "D"), ("B", "E"),
        ("C", "F"), ("C", "G")
    ]
    
    for u, v in edges:
        graph_matrix.add_edge(u, v)
        graph_list.add_edge(u, v)
    
    start_vertex = "A"
    
    # BFS
    print("Поиск в ширину (BFS):")
    bfs_order_matrix, bfs_dist_matrix, bfs_parents_matrix = bfs_matrix(graph_matrix, start_vertex)
    bfs_order_list, bfs_dist_list, bfs_parents_list = bfs_list(graph_list, start_vertex)
    
    print(f"  Порядок обхода (матрица): {bfs_order_matrix}")
    print(f"  Расстояния (матрица): {bfs_dist_matrix}")
    print(f"  Порядок обхода (список): {bfs_order_list}")
    print(f"  Расстояния (список): {bfs_dist_list}")
    
    # DFS
    print("\nПоиск в глубину (DFS):")
    dfs_order_matrix, dfs_parents_matrix = dfs_matrix_recursive(graph_matrix, start_vertex)
    dfs_order_list, dfs_parents_list = dfs_list_recursive(graph_list, start_vertex)
    
    print(f"  Порядок обхода рекурсивный (матрица): {dfs_order_matrix}")
    print(f"  Порядок обхода рекурсивный (список): {dfs_order_list}")
    
    dfs_order_iter_matrix, _ = dfs_iterative_matrix(graph_matrix, start_vertex)
    dfs_order_iter_list, _ = dfs_iterative_list(graph_list, start_vertex)
    
    print(f"  Порядок обхода итеративный (матрица): {dfs_order_iter_matrix}")
    print(f"  Порядок обхода итеративный (список): {dfs_order_iter_list}")


def demonstrate_shortest_paths():
    """Демонстрация алгоритмов поиска кратчайших путей"""
    print("\n\n3. Поиск кратчайших путей")
    print("-" * 40)
    
    # Создаем взвешенный граф
    graph_matrix = GraphMatrix(directed=False)
    graph_list = GraphList(directed=False)
    
    vertices = ["A", "B", "C", "D", "E"]
    for v in vertices:
        graph_matrix.add_vertex(v)
        graph_list.add_vertex(v)
    
    # Добавляем взвешенные ребра
    weighted_edges = [
        ("A", "B", 4), ("A", "C", 2),
        ("B", "C", 1), ("B", "D", 5),
        ("C", "D", 8), ("C", "E", 10),
        ("D", "E", 2)
    ]
    
    for u, v, w in weighted_edges:
        graph_matrix.add_edge(u, v, w)
        graph_list.add_edge(u, v, w)
    
    start_vertex = "A"
    
    # Алгоритм Дейкстры
    print("Алгоритм Дейкстры:")
    dijkstra_dist_matrix, dijkstra_parents_matrix = dijkstra_matrix(graph_matrix, start_vertex)
    dijkstra_dist_list, dijkstra_parents_list = dijkstra_list(graph_list, start_vertex)
    
    print(f"  Расстояния (матрица): {dijkstra_dist_matrix}")
    print(f"  Расстояния (список): {dijkstra_dist_list}")
    
    # Восстанавливаем путь до E
    end_vertex = "E"
    path_matrix = reconstruct_path(dijkstra_parents_matrix, start_vertex, end_vertex)
    path_list = reconstruct_path(dijkstra_parents_list, start_vertex, end_vertex)
    
    print(f"  Кратчайший путь от {start_vertex} до {end_vertex} (матрица): {' -> '.join(path_matrix)}")
    print(f"  Кратчайший путь от {start_vertex} до {end_vertex} (список): {' -> '.join(path_list)}")
    print(f"  Длина пути: {dijkstra_dist_matrix[end_vertex]}")
    
    # Алгоритм Беллмана-Форда
    print("\nАлгоритм Беллмана-Форда:")
    bf_dist_matrix, bf_parents_matrix, bf_cycle_matrix = bellman_ford_matrix(graph_matrix, start_vertex)
    bf_dist_list, bf_parents_list, bf_cycle_list = bellman_ford_list(graph_list, start_vertex)
    
    print(f"  Расстояния (матрица): {bf_dist_matrix}")
    print(f"  Отрицательный цикл (матрица): {bf_cycle_matrix}")
    print(f"  Расстояния (список): {bf_dist_list}")
    print(f"  Отрицательный цикл (список): {bf_cycle_list}")


def demonstrate_connected_components():
    """Демонстрация поиска компонент связности"""
    print("\n\n4. Компоненты связности")
    print("-" * 40)
    
    # Создаем несвязный граф
    graph_matrix = GraphMatrix(directed=False)
    graph_list = GraphList(directed=False)
    
    # Компонента 1: A-B-C
    for v in ["A", "B", "C"]:
        graph_matrix.add_vertex(v)
        graph_list.add_vertex(v)
    
    graph_matrix.add_edge("A", "B")
    graph_matrix.add_edge("B", "C")
    
    graph_list.add_edge("A", "B")
    graph_list.add_edge("B", "C")
    
    # Компонента 2: D-E
    for v in ["D", "E"]:
        graph_matrix.add_vertex(v)
        graph_list.add_vertex(v)
    
    graph_matrix.add_edge("D", "E")
    graph_list.add_edge("D", "E")
    
    # Изолированная вершина F
    graph_matrix.add_vertex("F")
    graph_list.add_vertex("F")
    
    print("Граф содержит 3 компоненты связности:")
    print("  1. A-B-C")
    print("  2. D-E")
    print("  3. F (изолированная)")
    
    # Поиск компонент
    components_matrix = find_connected_components_matrix(graph_matrix)
    components_list = find_connected_components_list(graph_list)
    
    print(f"\nНайдено компонент (матрица): {len(components_matrix)}")
    for i, comp in enumerate(components_matrix, 1):
        print(f"  Компонента {i}: {sorted(comp)}")
    
    print(f"\nНайдено компонент (список): {len(components_list)}")
    for i, comp in enumerate(components_list, 1):
        print(f"  Компонента {i}: {sorted(comp)}")


def demonstrate_topological_sort():
    """Демонстрация топологической сортировки"""
    print("\n\n5. Топологическая сортировка")
    print("-" * 40)
    
    # Создаем ориентированный ациклический граф (DAG)
    graph_matrix = GraphMatrix(directed=True)
    graph_list = GraphList(directed=True)
    
    # Вершины представляют задачи
    tasks = ["Изучить теорию", "Написать код", "Протестировать", "Документировать", "Сдать работу"]
    for task in tasks:
        graph_matrix.add_vertex(task)
        graph_list.add_vertex(task)
    
    # Зависимости между задачами
    dependencies = [
        ("Изучить теорию", "Написать код"),
        ("Написать код", "Протестировать"),
        ("Протестировать", "Документировать"),
        ("Документировать", "Сдать работу")
    ]
    
    for u, v in dependencies:
        graph_matrix.add_edge(u, v)
        graph_list.add_edge(u, v)
    
    print("Задачи и их зависимости:")
    for u, v in dependencies:
        print(f"  {u} -> {v}")
    
    # Топологическая сортировка
    topo_order_matrix = topological_sort_matrix(graph_matrix)
    topo_order_list = topological_sort_list(graph_list)
    
    print(f"\nТопологический порядок (матрица):")
    for i, task in enumerate(topo_order_matrix, 1):
        print(f"  {i}. {task}")
    
    print(f"\nТопологический порядок (список):")
    for i, task in enumerate(topo_order_list, 1):
        print(f"  {i}. {task}")


def demonstrate_maze_solution():
    """Демонстрация решения лабиринта"""
    print("\n\n6. Решение лабиринта")
    print("-" * 40)
    
    # Простой лабиринт 4x4
    print("Лабиринт 4x4:")
    print("  S - начальная точка")
    print("  E - конечная точка")
    print("  # - стена")
    print("  . - проход")
    
    maze = [
        ["S", ".", "#", "."],
        [".", "#", ".", "."],
        [".", ".", ".", "#"],
        [".", "#", ".", "E"]
    ]
    
    # Визуализация лабиринта
    print("\nВизуализация:")
    for row in maze:
        print("  " + " ".join(row))
    
    # Создаем граф для лабиринта
    graph_matrix = GraphMatrix(directed=False)
    graph_list = GraphList(directed=False)
    
    # Добавляем вершины (клетки-проходы)
    for i in range(4):
        for j in range(4):
            if maze[i][j] != "#":
                vertex = f"({i},{j})"
                graph_matrix.add_vertex(vertex)
                graph_list.add_vertex(vertex)
    
    # Добавляем ребра между соседними клетками-проходами
    for i in range(4):
        for j in range(4):
            if maze[i][j] == "#":
                continue
            
            current = f"({i},{j})"
            
            # Проверяем соседей
            if i > 0 and maze[i-1][j] != "#":  # Верхний сосед
                neighbor = f"({i-1},{j})"
                graph_matrix.add_edge(current, neighbor)
                graph_list.add_edge(current, neighbor)
            
            if j > 0 and maze[i][j-1] != "#":  # Левый сосед
                neighbor = f"({i},{j-1})"
                graph_matrix.add_edge(current, neighbor)
                graph_list.add_edge(current, neighbor)
    
    # Находим путь
    start = "(0,0)"  # S
    end = "(3,3)"    # E
    
    _, _, parents_matrix = bfs_matrix(graph_matrix, start)
    path_matrix = reconstruct_path(parents_matrix, start, end)
    
    print(f"\nПуть от {start} до {end}:")
    if path_matrix:
        print(f"  Найден путь: {' -> '.join(path_matrix)}")
        print(f"  Длина пути: {len(path_matrix) - 1} шагов")
    else:
        print("  Путь не найден")


def main():
    """Основная функция программы"""
    print("Лабораторная работа 10: Графы")
    print("=" * 60)
    
    demonstrate_graph_representations()
    demonstrate_bfs_dfs()
    demonstrate_shortest_paths()
    demonstrate_connected_components()
    demonstrate_topological_sort()
    demonstrate_maze_solution()
    
    print("\n" + "=" * 60)
    print("7. Анализ производительности")
    print("=" * 60)
    
    # Запуск анализа производительности
    import performance_analysis
    
    performance_analysis.compare_representations()
    performance_analysis.compare_bfs_performance()
    performance_analysis.compare_dfs_performance()
    performance_analysis.compare_shortest_path_algorithms()
    performance_analysis.test_connected_components()
    performance_analysis.test_topological_sort()
    performance_analysis.run_maze_simulation()
    
    print("\n" + "=" * 60)
    print("Выводы:")
    print("-" * 60)
    print("1. Выбор представления графа зависит от плотности графа и операций")
    print("2. Матрица смежности эффективна для плотных графов и проверки ребер")
    print("3. Список смежности эффективен для разреженных графов и обхода соседей")
    print("4. BFS находит кратчайшие пути в невзвешенных графах")
    print("5. DFS полезен для поиска компонент, проверки циклов, топологической сортировки")
    print("6. Алгоритм Дейкстры эффективен для графов с неотрицательными весами")
    print("7. Беллман-Форд работает с отрицательными весами, но медленнее")
    print("8. Топологическая сортировка применима только к ориентированным ациклическим графам")


if __name__ == "__main__":
    main()