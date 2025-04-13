"""
https://chatgpt.com/share/67f9a7f4-78cc-800c-a63c-46f139054af7
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada
tareas = [
    {'id': 1, 'titulo': 'Estudiar Flask', 'hecho': False},
    {'id': 2, 'titulo': 'Hacer compras', 'hecho': True}
]

# Obtener todas las tareas
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

# Obtener una tarea por ID
@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = next((t for t in tareas if t['id'] == id), None)
    if tarea:
        return jsonify(tarea)
    return jsonify({'error': 'Tarea no encontrada'}), 404

# Crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    datos = request.get_json()
    nueva_tarea = {
        'id': tareas[-1]['id'] + 1 if tareas else 1,
        'titulo': datos['titulo'],
        'hecho': False
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

# Marcar una tarea como hecha
@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = next((t for t in tareas if t['id'] == id), None)
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404

    datos = request.get_json()
    tarea['titulo'] = datos.get('titulo', tarea['titulo'])
    tarea['hecho'] = datos.get('hecho', tarea['hecho'])
    return jsonify(tarea)

# Eliminar una tarea
@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t['id'] != id]
    return jsonify({'resultado': True})

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
