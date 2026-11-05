import requests
import json

def get_matrix_from_user():
    """Модуль ввода"""
    matrix = []
    print("Введите элементы матрицы построчно (числа через пробел).")
    print("Для завершения ввода оставьте строку пустой и нажмите Enter.")
    i = 1
    while True:
        row_input = input(f"Строка {i}: ")
        if not row_input.strip():
            break
        try:
            row = list(map(float, row_input.split()))
            matrix.append(row)
            i += 1
        except ValueError:
            print("Ошибка: вводите только числа.")
    
    # Проверка на одинаковую длину строк
    if matrix:
        cols = len(matrix[0])
        if any(len(r) != cols for r in matrix):
            print("Ошибка: все строки должны быть одинаковой длины.")
            return get_matrix_from_user()
    return matrix

def print_matrix(matrix, title="Матрица"):
    """Модуль вывода"""
    print(f"\n--- {title} ---")
    for row in matrix:
        print("  ".join(f"{val:6.2f}" if isinstance(val, float) else f"{val:6}" for val in row))
    print("-------------------")

def main():
    print("=== Клиент системы обработки матриц ===")
    matrix = get_matrix_from_user()
    
    if not matrix:
        print("Матрица пуста. Завершение работы.")
        return

    print_matrix(matrix, "Исходная матрица (отправляется на сервер)")

    # Интеграция: отправка данных на сервер по REST API
    url = "http://127.0.0.1:5000/api/transpose"
    payload = {"matrix": matrix}
    headers = {"Content-Type": "application/json"}

    try:
        print("\nОтправка запроса на сервер...")
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            print("Ответ сервера получен успешно!")
            print_matrix(result['transposed_matrix'], "Транспонированная матрица (ответ сервера)")
        else:
            print(f"Ошибка сервера: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Ошибка интеграции: Сервер недоступен. Убедитесь, что api_server.py запущен.")

if __name__ == "__main__":
    main()
