# intercambio.py
from flask import Blueprint, render_template

# Crear un Blueprint llamado 'intercambio'
intercambio_bp = Blueprint('intercambio', __name__, template_folder='templates')

# Ruta para el formulario de intercambio
@intercambio_bp.route('/intercambio')
def intercambio():
    return render_template('intercambio.html')
