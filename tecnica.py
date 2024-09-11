from flask import Blueprint, render_template

# Crear un Blueprint llamado 'tecnica'
tecnica_bp = Blueprint('tecnica', __name__)

# Ruta para la página de bodega
@tecnica_bp.route('/tecnica')
def tecnica():
    return render_template('tecnica.html')
