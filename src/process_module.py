import json
import os

def load_matrix_from_json(filename="src/matrix_data.json"):
    """Загрузка матрицы из JSON-файла."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл {filename} не найден!")
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data["matrix"]

def transpose_matrix(matrix):
    """Транспонирование матрицы."""
    if not matrix:
        return []
    # Используем zip для транспонирования
    transposed = [list(row) for row in zip(*matrix)]
    return transposed
