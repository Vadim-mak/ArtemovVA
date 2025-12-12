class GraphMatrix:
    """Представление графа с помощью матрицы смежности"""
    
    def __init__(self, directed=False):
        """
        Инициализация графа
        
        Сложность: O(1)
        Память: O(1)
        """
        self.directed = directed  # O(1)
        self.vertices = []  # O(1) - список вершин
        self.vertex_index = {}  # O(1) - словарь для быстрого доступа
        self.matrix = []  # O(1) - матрица смежности
        self.vertex_count = 0  # O(1)
    
    def add_vertex(self, vertex):
        """
        Добавление вершины в граф
        
        Сложность: O(n) где n - текущее количество вершин
        Память: O(n²) для матрицы
        """
        if vertex in self.vertex_index:  # O(1)
            return False
        
        # Добавляем вершину в список
        self.vertices.append(vertex)  # O(1)
        self.vertex_index[vertex] = self.vertex_count  # O(1)
        self.vertex_count += 1  # O(1)
        
        # Расширяем матрицу
        for row in self.matrix:  # O(n)
            row.append(0)  # O(1)
        
        # Добавляем новую строку
        new_row = [0] * self.vertex_count  # O(n)
        self.matrix.append(new_row)  # O(1)
        
        return True
    
    def add_edge(self, u, v, weight=1):
        """
        Добавление ребра между вершинами u и v
        
        Сложность: O(1)
        Память: O(1)
        """
        if u not in self.vertex_index or v not in self.vertex_index:  # O(1)
            return False
        
        i = self.vertex_index[u]  # O(1)
        j = self.vertex_index[v]  # O(1)
        
        self.matrix[i][j] = weight  # O(1)
        
        if not self.directed:  # O(1)
            self.matrix[j][i] = weight  # O(1)
        
        return True
    
    def remove_edge(self, u, v):
        """
        Удаление ребра между вершинами u и v
        
        Сложность: O(1)
        Память: O(1)
        """
        if u not in self.vertex_index or v not in self.vertex_index:  # O(1)
            return False
        
        i = self.vertex_index[u]  # O(1)
        j = self.vertex_index[v]  # O(1)
        
        self.matrix[i][j] = 0  # O(1)
        
        if not self.directed:  # O(1)
            self.matrix[j][i] = 0  # O(1)
        
        return True
    
    def has_edge(self, u, v):
        """
        Проверка наличия ребра между вершинами u и v
        
        Сложность: O(1)
        Память: O(1)
        """
        if u not in self.vertex_index or v not in self.vertex_index:  # O(1)
            return False
        
        i = self.vertex_index[u]  # O(1)
        j = self.vertex_index[v]  # O(1)
        
        return self.matrix[i][j] != 0  # O(1)
    
    def get_neighbors(self, vertex):
        """
        Получение соседей вершины
        
        Сложность: O(n) где n - количество вершин
        Память: O(n) для списка соседей
        """
        if vertex not in self.vertex_index:  # O(1)
            return []
        
        i = self.vertex_index[vertex]  # O(1)
        neighbors = []  # O(1)
        
        for j, weight in enumerate(self.matrix[i]):  # O(n)
            if weight != 0:  # O(1)
                neighbor = self.vertices[j]  # O(1)
                neighbors.append((neighbor, weight))  # O(1)
        
        return neighbors
    
    def get_edges(self):
        """
        Получение всех ребер графа
        
        Сложность: O(n²) где n - количество вершин
        Память: O(m) где m - количество ребер
        """
        edges = []  # O(1)
        
        for i in range(self.vertex_count):  # O(n)
            for j in range(self.vertex_count):  # O(n²)
                if self.matrix[i][j] != 0:  # O(1)
                    u = self.vertices[i]  # O(1)
                    v = self.vertices[j]  # O(1)
                    weight = self.matrix[i][j]  # O(1)
                    edges.append((u, v, weight))  # O(1)
        
        return edges
    
    def __str__(self):
        """Строковое представление графа"""
        result = "Матрица смежности:\n"
        result += "   " + " ".join(f"{v:2}" for v in self.vertices) + "\n"
        
        for i, row in enumerate(self.matrix):  # O(n)
            result += f"{self.vertices[i]:2} " + " ".join(f"{val:2}" for val in row) + "\n"
        
        return result


class GraphList:
    """Представление графа с помощью списка смежности"""
    
    def __init__(self, directed=False):
        """
        Инициализация графа
        
        Сложность: O(1)
        Память: O(1)
        """
        self.directed = directed  # O(1)
        self.adj_list = {}  # O(1) - словарь списков смежности
    
    def add_vertex(self, vertex):
        """
        Добавление вершины в граф
        
        Сложность: O(1)
        Память: O(1)
        """
        if vertex not in self.adj_list:  # O(1)
            self.adj_list[vertex] = []  # O(1)
            return True
        return False
    
    def add_edge(self, u, v, weight=1):
        """
        Добавление ребра между вершинами u и v
        
        Сложность: O(1)
        Память: O(1)
        """
        # Добавляем вершины, если их нет
        self.add_vertex(u)  # O(1)
        self.add_vertex(v)  # O(1)
        
        # Добавляем ребро
        self.adj_list[u].append((v, weight))  # O(1)
        
        if not self.directed:  # O(1)
            self.adj_list[v].append((u, weight))  # O(1)
        
        return True
    
    def remove_edge(self, u, v):
        """
        Удаление ребра между вершинами u и v
        
        Сложность: O(k) где k - степень вершины u (и v для неориентированного)
        Память: O(1)
        """
        if u not in self.adj_list or v not in self.adj_list:  # O(1)
            return False
        
        # Удаляем ребро из списка u
        for i, (neighbor, weight) in enumerate(self.adj_list[u]):  # O(k)
            if neighbor == v:  # O(1)
                del self.adj_list[u][i]  # O(k)
                break
        
        if not self.directed:  # O(1)
            # Удаляем ребро из списка v
            for i, (neighbor, weight) in enumerate(self.adj_list[v]):  # O(k)
                if neighbor == u:  # O(1)
                    del self.adj_list[v][i]  # O(k)
                    break
        
        return True
    
    def has_edge(self, u, v):
        """
        Проверка наличия ребра между вершинами u и v
        
        Сложность: O(k) где k - степень вершины u
        Память: O(1)
        """
        if u not in self.adj_list:  # O(1)
            return False
        
        for neighbor, weight in self.adj_list[u]:  # O(k)
            if neighbor == v:  # O(1)
                return True
        
        return False
    
    def get_neighbors(self, vertex):
        """
        Получение соседей вершины
        
        Сложность: O(1) для доступа к списку
        Память: O(k) для возврата списка соседей
        """
        return self.adj_list.get(vertex, [])  # O(1)
    
    def get_vertices(self):
        """
        Получение всех вершин графа
        
        Сложность: O(1) для доступа к ключам
        Память: O(n) для возврата списка вершин
        """
        return list(self.adj_list.keys())  # O(1)
    
    def get_edges(self):
        """
        Получение всех ребер графа
        
        Сложность: O(n + m) где n - вершин, m - ребер
        Память: O(m) для возврата списка ребер
        """
        edges = []  # O(1)
        visited = set()  # O(1) - для неориентированных графов
        
        for u in self.adj_list:  # O(n)
            for v, weight in self.adj_list[u]:  # O(m)
                if not self.directed:  # O(1)
                    # Для неориентированных графов добавляем каждое ребро один раз
                    edge_key = tuple(sorted((u, v)))  # O(1)
                    if edge_key not in visited:  # O(1)
                        visited.add(edge_key)  # O(1)
                        edges.append((u, v, weight))  # O(1)
                else:
                    edges.append((u, v, weight))  # O(1)
        
        return edges
    
    def __str__(self):
        """Строковое представление графа"""
        result = "Список смежности:\n"
        
        for vertex in sorted(self.adj_list.keys()):  # O(n log n)
            neighbors = self.adj_list[vertex]  # O(1)
            neighbor_str = ", ".join([f"{v}({w})" for v, w in neighbors])  # O(k)
            result += f"{vertex}: [{neighbor_str}]\n"
        
        return result