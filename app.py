from flask import Flask, render_template
from infraestructura import infraestructura_bp  # Importamos el Blueprint de infraestructura
from bodega import bodega_bp  # Importamos el Blueprint de bodega
from tecnica import tecnica_bp  # Importamos el Blueprint de técnica
from intercambio import intercambio_bp  # Importamos el Blueprint de intercambio

app = Flask(__name__)

# Registramos los Blueprints
app.register_blueprint(infraestructura_bp)
app.register_blueprint(bodega_bp)
app.register_blueprint(tecnica_bp)
app.register_blueprint(intercambio_bp)  # Asegúrate de registrar el blueprint de intercambio

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
