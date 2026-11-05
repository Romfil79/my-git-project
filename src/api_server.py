from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/transpose', methods=['POST'])
def transpose():
    data = request.get_json()
    
    if not data or 'matrix' not in data:
        return jsonify({"error": "Неверный формат данных. Ожидается JSON с ключом 'matrix'"}), 400
    
    matrix = data['matrix']
    
    # Валидация матрицы
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return jsonify({"error": "Матрица должна быть списком списков"}), 400
        
    try:
        # Логика транспонирования (Модуль обработки)
        transposed = [list(row) for row in zip(*matrix)]
        
        # Возвращаем результат в формате JSON
        return jsonify({
            "status": "success",
            "original_rows": len(matrix),
            "original_cols": len(matrix[0]) if matrix else 0,
            "transposed_matrix": transposed
        })
    except Exception as e:
        return jsonify({"error": f"Ошибка обработки: {str(e)}"}), 500

if __name__ == '__main__':
    # Запускаем сервер на localhost, порт 5000
    app.run(debug=True, port=5000)
