import json
import os

def get_matrix_from_user(rows, cols):
    """Ввод матрицы вручную."""
    matrix = []
    print(f"Введите элементы матрицы {rows}x{cols} построчно (через пробел):")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != cols:
                    print(f"Ошибка: нужно ввести ровно {cols} чисел.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: вводите только числа.")
    return matrix

def save_matrix_to_json(matrix, filename="src/matrix_data.json"):
    """Сохранение матрицы в JSON-файл."""
    data = {"matrix": matrix}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Матрица сохранена в файл {filename}")
