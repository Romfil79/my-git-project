def print_matrix(matrix, title="Матрица"):
    """Вывод матрицы в консоль."""
    print(f"\n--- {title} ---")
    for row in matrix:
        # Форматируем числа для красивого вывода
        print("  ".join(f"{val:6.2f}" if isinstance(val, float) else f"{val:6}" for val in row))
    print("-------------------")
