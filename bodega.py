from flask import Blueprint, render_template, request, redirect, url_for, flash

# Crear un Blueprint llamado 'bodega_bp'
bodega_bp = Blueprint('bodega', __name__, template_folder='templates')

# Lista de operadores para pasar al formulario
operators = ['Operador 1', 'Operador 2', 'Operador 3']

# Ruta para la página de bodega
@bodega_bp.route('/bodega')
def bodega():
    return render_template('bodega.html', operators=operators)

# Ruta para manejar el envío del formulario de bodega
@bodega_bp.route('/submit', methods=['POST'])
def submit_bodega():
    try:
        total_puntaje = 0
        total_items = 0

        # Procesar los datos del formulario
        for key, value in request.form.items():
            if 'requisito' in key:  # Solo procesar los campos de requisitos
                if value != 'null':  # Ignorar las opciones que son "No Aplica"
                    total_puntaje += int(value)
                    total_items += 1

        # Calcular el porcentaje de cumplimiento
        if total_items > 0:
            porcentaje_cumplimiento = (total_puntaje / total_items) * 100
        else:
            porcentaje_cumplimiento = 0

        # Clasificar el resultado
        if porcentaje_cumplimiento >= 80:
            resultado = 'Adecuado'
        elif 61 <= porcentaje_cumplimiento <= 79:
            resultado = 'Regular'
        else:
            resultado = 'Malo'

        # Mensaje de éxito
        flash(f"Porcentaje de cumplimiento: {porcentaje_cumplimiento}%, Resultado: {resultado}", 'success')
    except Exception as e:
        # Manejar cualquier error durante el procesamiento
        flash(f"Error al procesar el formulario: {str(e)}", 'error')

    return redirect(url_for('bodega.bodega'))

