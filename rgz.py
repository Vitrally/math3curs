import numpy as np
import itertools
import time

# Матрица расстояний с пропусками заменяем на большие значения
C = [
    [float('inf'), 13, 7, 5, 2, 9],
    [8, float('inf'), 4, 7, 5, float('inf')],
    [8, 4, float('inf'), 3, 6, 2],
    [5, 8, 1, float('inf'), 0, 1],
    [float('inf'), 6, 1, 4, float('inf'), 9],
    [10, 0, 8, 3, 7, float('inf')]
]

# Функция для прямого перебора
def tsp_brute_force(matrix):
    n = len(matrix)
    best_cost = float('inf')
    best_path = None

    for perm in itertools.permutations(range(n)):
        current_cost = sum(matrix[perm[i]][perm[i+1]] for i in range(n - 1)) + matrix[perm[-1]][perm[0]]
        if current_cost < best_cost:
            best_cost = current_cost
            best_path = perm

    return best_cost, best_path

# Функция для метода ветвей и границ
def tsp_branch_and_bound(matrix):
    n = len(matrix)
    best_cost = float('inf')
    best_path = None
    visited = [False] * n
    path = [0]

    def branch(current_cost, level):
        nonlocal best_cost, best_path
        if level == n:
            current_cost += matrix[path[-1]][0]
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = list(path)
            return

        for i in range(1, n):
            if not visited[i]:
                temp_cost = current_cost + matrix[path[-1]][i]
                if temp_cost < best_cost:
                    visited[i] = True
                    path.append(i)
                    branch(temp_cost, level + 1)
                    path.pop()
                    visited[i] = False

    branch(0, 1)
    return best_cost, best_path

# Запуск алгоритмов и измерение времени
start_time = time.time()
brute_force_cost, brute_force_path = tsp_brute_force(C)
brute_force_time = time.time() - start_time

start_time = time.time()
branch_bound_cost, branch_bound_path = tsp_branch_and_bound(C)
branch_bound_time = time.time() - start_time

# Вывод результатов
print("Прямой перебор:")
print("Минимальная стоимость:", brute_force_cost)
print("Оптимальный путь:", brute_force_path)
print("Время выполнения:", brute_force_time)

print("\nМетод ветвей и границ:")
print("Минимальная стоимость:", branch_bound_cost)
print("Оптимальный путь:", branch_bound_path)
print("Время выполнения:", branch_bound_time)

# Сравнение трудоемкости
print("\nСравнение трудоемкости:")
print("Время выполнения прямого перебора:", brute_force_time)
print("Время выполнения метода ветвей и границ:", branch_bound_time)
print("Ускорение:", brute_force_time / branch_bound_time if branch_bound_time != 0 else "Неопределено")
