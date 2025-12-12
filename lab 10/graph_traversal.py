from collections import deque

def bfs_matrix(graph, start_vertex):
    """
    Поиск в ширину (BFS) для графа, представленного матрицей смежности
    
    Сложность: O(V²) где V - количество вершин
    Память: O(V) для очереди и посещенных вершин
    """
    if start_vertex not in graph.vertex_index:  # O(1)
        return [], {}
    
    visited = set()  # O(1)
    queue = deque([start_vertex])  # O(1)
    visited.add(start_vertex)  # O(1)
    
    bfs_order = []  # O(1)
    distances = {start_vertex: 0}  # O(1)
    parents = {start_vertex: None}  # O(1)
    
    while queue:  # O(V)
        current = queue.popleft()  # O(1)
        bfs_order.append(current)  # O(1)
        
        # Получаем соседей из матрицы
        i = graph.vertex_index[current]  # O(1)
        
        for j, weight in enumerate(graph.matrix[i]):  # O(V) на каждой итерации
            if weight != 0:  # O(1)
                neighbor = graph.vertices[j]  # O(1)
                
                if neighbor not in visited:  # O(1)
                    visited.add(neighbor)  # O(1)
                    queue.append(neighbor)  # O(1)
                    distances[neighbor] = distances[current] + 1  # O(1)
                    parents[neighbor] = current  # O(1)
    
    return bfs_order, distances, parents  # O(1)


def bfs_list(graph, start_vertex):
    """
    Поиск в ширину (BFS) для графа, представленного списком смежности
    
    Сложность: O(V + E) где V - вершин, E - ребер
    Память: O(V) для очереди и посещенных вершин
    """
    if start_vertex not in graph.adj_list:  # O(1)
        return [], {}
    
    visited = set()  # O(1)
    queue = deque([start_vertex])  # O(1)
    visited.add(start_vertex)  # O(1)
    
    bfs_order = []  # O(1)
    distances = {start_vertex: 0}  # O(1)
    parents = {start_vertex: None}  # O(1)
    
    while queue:  # O(V)
        current = queue.popleft()  # O(1)
        bfs_order.append(current)  # O(1)
        
        # Получаем соседей из списка смежности
        for neighbor, weight in graph.adj_list[current]:  # O(deg(current))
            if neighbor not in visited:  # O(1)
                visited.add(neighbor)  # O(1)
                queue.append(neighbor)  # O(1)
                distances[neighbor] = distances[current] + 1  # O(1)
                parents[neighbor] = current  # O(1)
    
    return bfs_order, distances, parents  # O(1)


def dfs_matrix_recursive(graph, start_vertex):
    """
    Рекурсивный поиск в глубину (DFS) для графа, представленного матрицей
    
    Сложность: O(V²) где V - количество вершин
    Память: O(V) для стека вызовов и посещенных вершин
    """
    if start_vertex not in graph.vertex_index:  # O(1)
        return [], {}
    
    visited = set()  # O(1)
    dfs_order = []  # O(1)
    parents = {start_vertex: None}  # O(1)
    
    def dfs_visit(current):  # O(V²)
        visited.add(current)  # O(1)
        dfs_order.append(current)  # O(1)
        
        # Получаем соседей из матрицы
        i = graph.vertex_index[current]  # O(1)
        
        for j, weight in enumerate(graph.matrix[i]):  # O(V)
            if weight != 0:  # O(1)
                neighbor = graph.vertices[j]  # O(1)
                
                if neighbor not in visited:  # O(1)
                    parents[neighbor] = current  # O(1)
                    dfs_visit(neighbor)  # Рекурсивный вызов
    
    dfs_visit(start_vertex)  # O(V²)
    return dfs_order, parents  # O(1)


def dfs_list_recursive(graph, start_vertex):
    """
    Рекурсивный поиск в глубину (DFS) для графа, представленного списком смежности
    
    Сложность: O(V + E) где V - вершин, E - ребер
    Память: O(V) для стека вызовов и посещенных вершин
    """
    if start_vertex not in graph.adj_list:  # O(1)
        return [], {}
    
    visited = set()  # O(1)
    dfs_order = []  # O(1)
    parents = {start_vertex: None}  # O(1)
    
    def dfs_visit(current):  # O(V + E)
        visited.add(current)  # O(1)
        dfs_order.append(current)  # O(1)
        
        # Получаем соседей из списка смежности
        for neighbor, weight in graph.adj_list[current]:  # O(deg(current))
            if neighbor not in visited:  # O(1)
                parents[neighbor] = current  # O(1)
                dfs_visit(neighbor)  # Рекурсивный вызов
    
    dfs_visit(start_vertex)  # O(V + E)
    return dfs_order, parents  # O(1)


def dfs_iterative_matrix(graph, start_vertex):
    """
    Итеративный поиск в глубину (DFS) для графа, представленного матрицей
    
    Сложность: O(V²) где V - количество вершин
    Память: O(V) для стека и посещенных вершин
    """
    if start_vertex not in graph.vertex_index:  # O(1)
        return [], {}
    
    visited = set()  # O(1)
    stack = [start_vertex]  # O(1)
    visited.add(start_vertex)  # O(1)
    
    dfs_order = []  # O(1)
    parents = {start_vertex: None}  # O(1)
    
    while stack:  # O(V)
        current = stack.pop()  # O(1)
        dfs_order.append(current)  # O(1)
        
        # Получаем соседей из матрицы (в обратном порядке для естественного обхода)
        i = graph.vertex_index[current]  # O(1)
        neighbors = []  # O(1)
        
        for j, weight in enumerate(graph.matrix[i]):  # O(V)
            if weight != 0:  # O(1)
                neighbor = graph.vertices[j]  # O(1)
                neighbors.append(neighbor)  # O(1)
        
        # Обрабатываем соседей в обратном порядке (для сравнения с рекурсивным)
        for neighbor in reversed(neighbors):  # O(V)
            if neighbor not in visited:  # O(1)
                visited.add(neighbor)  # O(1)
                stack.append(neighbor)  # O(1)
                parents[neighbor] = current  # O(1)
    
    return dfs_order, parents  # O(1)


def dfs_iterative_list(graph, start_vertex):
    """
    Итеративный поиск в глубину (DFS) для графа, представленного списком смежности
    
    Сложность: O(V + E) где V - вершин, E - ребер
    Память: O(V) для стека и посещенных вершин
    """
    if start_vertex not in graph.adj_list:  # O(1)
        return [], {}
    
    visited = set()  # O(1)
    stack = [start_vertex]  # O(1)
    visited.add(start_vertex)  # O(1)
    
    dfs_order = []  # O(1)
    parents = {start_vertex: None}  # O(1)
    
    while stack:  # O(V)
        current = stack.pop()  # O(1)
        dfs_order.append(current)  # O(1)
        
        # Получаем соседей из списка смежности
        neighbors = graph.adj_list[current]  # O(1)
        
        # Обрабатываем соседей в обратном порядке (для сравнения с рекурсивным)
        for neighbor, weight in reversed(neighbors):  # O(deg(current))
            if neighbor not in visited:  # O(1)
                visited.add(neighbor)  # O(1)
                stack.append(neighbor)  # O(1)
                parents[neighbor] = current  # O(1)
    
    return dfs_order, parents  # O(1)


def find_connected_components_matrix(graph):
    """
    Поиск компонент связности для графа, представленного матрицей
    
    Сложность: O(V²) где V - количество вершин
    Память: O(V) для посещенных вершин и компонент
    """
    visited = set()  # O(1)
    components = []  # O(1)
    
    for vertex in graph.vertices:  # O(V)
        if vertex not in visited:  # O(1)
            # Запускаем BFS для новой компоненты
            component_vertices = []  # O(1)
            queue = deque([vertex])  # O(1)
            visited.add(vertex)  # O(1)
            
            while queue:  # O(V)
                current = queue.popleft()  # O(1)
                component_vertices.append(current)  # O(1)
                
                # Получаем соседей из матрицы
                i = graph.vertex_index[current]  # O(1)
                
                for j, weight in enumerate(graph.matrix[i]):  # O(V)
                    if weight != 0:  # O(1)
                        neighbor = graph.vertices[j]  # O(1)
                        
                        if neighbor not in visited:  # O(1)
                            visited.add(neighbor)  # O(1)
                            queue.append(neighbor)  # O(1)
            
            components.append(component_vertices)  # O(1)
    
    return components  # O(1)


def find_connected_components_list(graph):
    """
    Поиск компонент связности для графа, представленного списком смежности
    
    Сложность: O(V + E) где V - вершин, E - ребер
    Память: O(V) для посещенных вершин и компонент
    """
    visited = set()  # O(1)
    components = []  # O(1)
    
    for vertex in graph.adj_list:  # O(V)
        if vertex not in visited:  # O(1)
            # Запускаем BFS для новой компоненты
            component_vertices = []  # O(1)
            queue = deque([vertex])  # O(1)
            visited.add(vertex)  # O(1)
            
            while queue:  # O(V)
                current = queue.popleft()  # O(1)
                component_vertices.append(current)  # O(1)
                
                # Получаем соседей из списка смежности
                for neighbor, weight in graph.adj_list[current]:  # O(E)
                    if neighbor not in visited:  # O(1)
                        visited.add(neighbor)  # O(1)
                        queue.append(neighbor)  # O(1)
            
            components.append(component_vertices)  # O(1)
    
    return components  # O(1)