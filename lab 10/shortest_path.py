import heapq
from collections import deque

def dijkstra_matrix(graph, start_vertex):
    """
    Алгоритм Дейкстры для графа, представленного матрицей смежности
    
    Сложность: O(V²) где V - количество вершин
    Память: O(V) для расстояний, предков и приоритетной очереди
    """
    if start_vertex not in graph.vertex_index:  # O(1)
        return {}, {}
    
    # Инициализация
    distances = {vertex: float('inf') for vertex in graph.vertices}  # O(V)
    parents = {vertex: None for vertex in graph.vertices}  # O(V)
    distances[start_vertex] = 0  # O(1)
    
    # Приоритетная очередь (мин-куча)
    pq = [(0, start_vertex)]  # O(1)
    visited = set()  # O(1)
    
    while pq:  # O(V)
        current_dist, current = heapq.heappop(pq)  # O(log V)
        
        # Пропускаем устаревшие записи
        if current in visited:  # O(1)
            continue
        
        visited.add(current)  # O(1)
        
        # Получаем соседей из матрицы
        i = graph.vertex_index[current]  # O(1)
        
        for j, weight in enumerate(graph.matrix[i]):  # O(V)
            if weight != 0:  # O(1)
                neighbor = graph.vertices[j]  # O(1)
                
                if neighbor in visited:  # O(1)
                    continue
                
                # Вычисляем новое расстояние
                new_dist = current_dist + weight  # O(1)
                
                if new_dist < distances[neighbor]:  # O(1)
                    distances[neighbor] = new_dist  # O(1)
                    parents[neighbor] = current  # O(1)
                    heapq.heappush(pq, (new_dist, neighbor))  # O(log V)
    
    return distances, parents  # O(1)


def dijkstra_list(graph, start_vertex):
    """
    Алгоритм Дейкстры для графа, представленного списком смежности
    
    Сложность: O((V + E) log V) где V - вершин, E - ребер
    Память: O(V) для расстояний, предков и приоритетной очереди
    """
    if start_vertex not in graph.adj_list:  # O(1)
        return {}, {}
    
    # Инициализация
    distances = {vertex: float('inf') for vertex in graph.adj_list}  # O(V)
    parents = {vertex: None for vertex in graph.adj_list}  # O(V)
    distances[start_vertex] = 0  # O(1)
    
    # Приоритетная очередь (мин-куча)
    pq = [(0, start_vertex)]  # O(1)
    visited = set()  # O(1)
    
    while pq:  # O(V)
        current_dist, current = heapq.heappop(pq)  # O(log V)
        
        # Пропускаем устаревшие записи
        if current in visited:  # O(1)
            continue
        
        visited.add(current)  # O(1)
        
        # Получаем соседей из списка смежности
        for neighbor, weight in graph.adj_list[current]:  # O(deg(current))
            if neighbor in visited:  # O(1)
                continue
            
            # Вычисляем новое расстояние
            new_dist = current_dist + weight  # O(1)
            
            if new_dist < distances[neighbor]:  # O(1)
                distances[neighbor] = new_dist  # O(1)
                parents[neighbor] = current  # O(1)
                heapq.heappush(pq, (new_dist, neighbor))  # O(log V)
    
    return distances, parents  # O(1)


def bellman_ford_matrix(graph, start_vertex):
    """
    Алгоритм Беллмана-Форда для графа, представленного матрицей
    
    Сложность: O(V³) где V - количество вершин
    Память: O(V) для расстояний и предков
    """
    if start_vertex not in graph.vertex_index:  # O(1)
        return {}, {}, False
    
    # Инициализация
    distances = {vertex: float('inf') for vertex in graph.vertices}  # O(V)
    parents = {vertex: None for vertex in graph.vertices}  # O(V)
    distances[start_vertex] = 0  # O(1)
    
    edges = []  # O(1)
    
    # Собираем все ребра
    for i in range(graph.vertex_count):  # O(V)
        for j in range(graph.vertex_count):  # O(V²)
            if graph.matrix[i][j] != 0:  # O(1)
                u = graph.vertices[i]  # O(1)
                v = graph.vertices[j]  # O(1)
                weight = graph.matrix[i][j]  # O(1)
                edges.append((u, v, weight))  # O(1)
    
    # Основной цикл релаксации
    for _ in range(graph.vertex_count - 1):  # O(V)
        updated = False  # O(1)
        
        for u, v, weight in edges:  # O(E) = O(V²)
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:  # O(1)
                distances[v] = distances[u] + weight  # O(1)
                parents[v] = u  # O(1)
                updated = True  # O(1)
        
        if not updated:  # O(1)
            break
    
    # Проверка на отрицательные циклы
    has_negative_cycle = False  # O(1)
    
    for u, v, weight in edges:  # O(E)
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:  # O(1)
            has_negative_cycle = True  # O(1)
            break
    
    return distances, parents, has_negative_cycle  # O(1)


def bellman_ford_list(graph, start_vertex):
    """
    Алгоритм Беллмана-Форда для графа, представленного списком смежности
    
    Сложность: O(V * E) где V - вершин, E - ребер
    Память: O(V) для расстояний и предков
    """
    if start_vertex not in graph.adj_list:  # O(1)
        return {}, {}, False
    
    # Инициализация
    distances = {vertex: float('inf') for vertex in graph.adj_list}  # O(V)
    parents = {vertex: None for vertex in graph.adj_list}  # O(V)
    distances[start_vertex] = 0  # O(1)
    
    edges = []  # O(1)
    
    # Собираем все ребра
    for u in graph.adj_list:  # O(V)
        for v, weight in graph.adj_list[u]:  # O(E)
            edges.append((u, v, weight))  # O(1)
    
    # Основной цикл релаксации
    for _ in range(len(graph.adj_list) - 1):  # O(V)
        updated = False  # O(1)
        
        for u, v, weight in edges:  # O(E)
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:  # O(1)
                distances[v] = distances[u] + weight  # O(1)
                parents[v] = u  # O(1)
                updated = True  # O(1)
        
        if not updated:  # O(1)
            break
    
    # Проверка на отрицательные циклы
    has_negative_cycle = False  # O(1)
    
    for u, v, weight in edges:  # O(E)
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:  # O(1)
            has_negative_cycle = True  # O(1)
            break
    
    return distances, parents, has_negative_cycle  # O(1)


def topological_sort_matrix(graph):
    """
    Топологическая сортировка для графа, представленного матрицей
    
    Сложность: O(V²) где V - количество вершин
    Память: O(V) для степеней входа и очереди
    """
    if graph.directed == False:  # O(1)
        return []  # Топологическая сортировка только для ориентированных графов
    
    # Вычисляем степени входа вершин
    in_degree = {vertex: 0 for vertex in graph.vertices}  # O(V)
    
    for i in range(graph.vertex_count):  # O(V)
        for j in range(graph.vertex_count):  # O(V²)
            if graph.matrix[i][j] != 0:  # O(1)
                v = graph.vertices[j]  # O(1)
                in_degree[v] += 1  # O(1)
    
    # Очередь вершин с нулевой степенью входа
    queue = deque([v for v in graph.vertices if in_degree[v] == 0])  # O(V)
    topo_order = []  # O(1)
    
    while queue:  # O(V)
        current = queue.popleft()  # O(1)
        topo_order.append(current)  # O(1)
        
        # Уменьшаем степени входа соседей
        i = graph.vertex_index[current]  # O(1)
        
        for j, weight in enumerate(graph.matrix[i]):  # O(V)
            if weight != 0:  # O(1)
                neighbor = graph.vertices[j]  # O(1)
                in_degree[neighbor] -= 1  # O(1)
                
                if in_degree[neighbor] == 0:  # O(1)
                    queue.append(neighbor)  # O(1)
    
    # Проверка на наличие цикла
    if len(topo_order) != len(graph.vertices):  # O(1)
        return []  # Граф содержит цикл
    
    return topo_order  # O(1)


def topological_sort_list(graph):
    """
    Топологическая сортировка для графа, представленного списком смежности
    
    Сложность: O(V + E) где V - вершин, E - ребер
    Память: O(V) для степеней входа и очереди
    """
    if graph.directed == False:  # O(1)
        return []  # Топологическая сортировка только для ориентированных графов
    
    # Вычисляем степени входа вершин
    in_degree = {vertex: 0 for vertex in graph.adj_list}  # O(V)
    
    for u in graph.adj_list:  # O(V)
        for v, weight in graph.adj_list[u]:  # O(E)
            in_degree[v] = in_degree.get(v, 0) + 1  # O(1)
    
    # Очередь вершин с нулевой степенью входа
    queue = deque([v for v in graph.adj_list if in_degree.get(v, 0) == 0])  # O(V)
    topo_order = []  # O(1)
    
    while queue:  # O(V)
        current = queue.popleft()  # O(1)
        topo_order.append(current)  # O(1)
        
        # Уменьшаем степени входа соседей
        for neighbor, weight in graph.adj_list.get(current, []):  # O(deg(current))
            in_degree[neighbor] -= 1  # O(1)
            
            if in_degree[neighbor] == 0:  # O(1)
                queue.append(neighbor)  # O(1)
    
    # Проверка на наличие цикла
    if len(topo_order) != len(graph.adj_list):  # O(1)
        return []  # Граф содержит цикл
    
    return topo_order  # O(1)


def reconstruct_path(parents, start, end):
    """
    Восстановление пути от start до end по словарю родителей
    
    Сложность: O(L) где L - длина пути
    Память: O(L) для пути
    """
    if end not in parents:  # O(1)
        return []  # Нет пути
    
    path = []  # O(1)
    current = end  # O(1)
    
    while current is not None:  # O(L)
        path.append(current)  # O(1)
        current = parents[current]  # O(1)
    
    path.reverse()  # O(L)
    
    # Проверяем, что путь начинается с start
    if path and path[0] == start:  # O(1)
        return path  # O(1)
    else:
        return []  # O(1)