import input_module
import process_module
import output_module

def main():
    print("=== Система обработки матриц ===")
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))
        
        # 1. Ввод данных (Модуль ввода)
        matrix = input_module.get_matrix_from_user(rows, cols)
        input_module.save_matrix_to_json(matrix)
        
        # 2. Обработка данных (Модуль обработки)
        loaded_matrix = process_module.load_matrix_from_json()
        transposed_matrix = process_module.transpose_matrix(loaded_matrix)
        
        # 3. Вывод данных (Модуль вывода)
        output_module.print_matrix(loaded_matrix, "Исходная матрица")
        output_module.print_matrix(transposed_matrix, "Транспонированная матрица")
        
    except Exception as e:
        print(f"Произошла ошибка при интеграции: {e}")

if __name__ == "__main__":
    main()
