from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import pymysql

# Creamos un Blueprint para la infraestructura
infraestructura_bp = Blueprint('infraestructura', __name__)

def obtener_operador():
    conexion = pymysql.connect(host='localhost', user='root', password='', db='pae_2')
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM operadores")
    operadores = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return operadores

def obtener_institucion():
    conexion = pymysql.connect(host='localhost', user='root', password='', db='pae_2')
    cursor = conexion.cursor()
    cursor.execute("SELECT id_institucion, sede_educativa FROM instituciones")
    instituciones = [{'id': row[0], 'nombre': row[1]} for row in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return instituciones

def obtener_sedes_por_institucion(institucion_id):
    conexion = pymysql.connect(host='localhost', user='root', password='', db='pae_2')
    cursor = conexion.cursor()
    cursor.execute("SELECT id_sede, nombre_sede FROM sedes WHERE id_institucion = %s", (institucion_id,))
    sedes = [{'id': row[0], 'nombre': row[1]} for row in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return sedes

def obtener_tipo_racion():
    conexion = pymysql.connect(host='localhost', user='root', password='', db='pae_2')
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT descripcion FROM tiporacion")
    tipo_racion = [row[0] for row in cursor.fetchall()]
    cursor.close()  
    conexion.close()
    return tipo_racion

def insertar_visita_infraestructura(data):
    conexion = pymysql.connect(host='localhost', user='root', password='', db='pae_2')
    cursor = conexion.cursor()

    sql = """INSERT INTO visitas_infraestructura (
            fecha, municipio, corregimiento, vereda, operador, institucion, sede,
            direccion, barrio, comuna, zona, tipo_racion, focalizacion,
            verificacion_1_1, observacion_1_1, verificacion_1_2, observacion_1_2,
            verificacion_1_3, observacion_1_3, verificacion_1_4, observacion_1_4,
            verificacion_2_1, observacion_2_1, verificacion_2_2, observacion_2_2,
            verificacion_2_3, observacion_2_3, verificacion_2_4, observacion_2_4,
            verificacion_2_5, observacion_2_5, verificacion_2_6, observacion_2_6,
            verificacion_2_7, observacion_2_7, verificacion_2_8, observacion_2_8,
            verificacion_2_9, observacion_2_9, verificacion_2_10, observacion_2_10,
            verificacion_2_11, observacion_2_11,
            verificacion_3_1, observacion_3_1, verificacion_3_2, observacion_3_2,
            verificacion_3_3, observacion_3_3, verificacion_3_4, observacion_3_4,
            verificacion_3_5, observacion_3_5, verificacion_3_6, observacion_3_6,
            verificacion_3_7, observacion_3_7, verificacion_3_8, observacion_3_8,
            verificacion_3_9, observacion_3_9, verificacion_3_10, observacion_3_10,
            verificacion_4_1, observacion_4_1, verificacion_4_2, observacion_4_2,
            verificacion_4_3, observacion_4_3, verificacion_4_4, observacion_4_4,
            verificacion_4_5, observacion_4_5, verificacion_4_6, observacion_4_6,
            verificacion_4_7, observacion_4_7, verificacion_4_8, observacion_4_8,
            verificacion_5_1, observacion_5_1, verificacion_5_2, observacion_5_2,
            verificacion_5_3, observacion_5_3, verificacion_5_4, observacion_5_4,
            verificacion_5_5, observacion_5_5, verificacion_5_6, observacion_5_6,
            verificacion_6_1, observacion_6_1, verificacion_6_2, observacion_6_2,
            verificacion_6_3, observacion_6_3, verificacion_6_4, observacion_6_4,
            verificacion_6_5, observacion_6_5, verificacion_6_6, observacion_6_6,
            cantidad_7_1, estado_7_1, propiedad_7_1,
            cantidad_7_4, estado_7_4, propiedad_7_4,
            codigo_sede
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s)"""

    try:
        cursor.execute(sql, (
            data['fecha'], data['municipio'], data['corregimiento'], data['vereda'], data['operador'],
            data['institucion'], data['sede'], data['direccion'], data['barrio'],
            data['comuna'], data['zona'], data['tipo_racion'], data['focalizacion'],
            data['verificacion_1_1'], data['observacion_1_1'], data['verificacion_1_2'], data['observacion_1_2'],
            data['verificacion_1_3'], data['observacion_1_3'], data['verificacion_1_4'], data['observacion_1_4'],
            data['verificacion_2_1'], data['observacion_2_1'], data['verificacion_2_2'], data['observacion_2_2'],
            data['verificacion_2_3'], data['observacion_2_3'], data['verificacion_2_4'], data['observacion_2_4'],
            data['verificacion_2_5'], data['observacion_2_5'], data['verificacion_2_6'], data['observacion_2_6'],
            data['verificacion_2_7'], data['observacion_2_7'], data['verificacion_2_8'], data['observacion_2_8'],
            data['verificacion_2_9'], data['observacion_2_9'], data['verificacion_2_10'], data['observacion_2_10'],
            data['verificacion_2_11'], data['observacion_2_11'],
            data['verificacion_3_1'], data['observacion_3_1'], data['verificacion_3_2'], data['observacion_3_2'],
            data['verificacion_3_3'], data['observacion_3_3'], data['verificacion_3_4'], data['observacion_3_4'],
            data['verificacion_3_5'], data['observacion_3_5'], data['verificacion_3_6'], data['observacion_3_6'],
            data['verificacion_3_7'], data['observacion_3_7'], data['verificacion_3_8'], data['observacion_3_8'],
            data['verificacion_3_9'], data['observacion_3_9'], data['verificacion_3_10'], data['observacion_3_10'],
            data['verificacion_4_1'], data['observacion_4_1'], data['verificacion_4_2'], data['observacion_4_2'],
            data['verificacion_4_3'], data['observacion_4_3'], data['verificacion_4_4'], data['observacion_4_4'],
            data['verificacion_4_5'], data['observacion_4_5'], data['verificacion_4_6'], data['observacion_4_6'],
            data['verificacion_4_7'], data['observacion_4_7'], data['verificacion_4_8'], data['observacion_4_8'],
            data['verificacion_5_1'], data['observacion_5_1'], data['verificacion_5_2'], data['observacion_5_2'],
            data['verificacion_5_3'], data['observacion_5_3'], data['verificacion_5_4'], data['observacion_5_4'],
            data['verificacion_5_5'], data['observacion_5_5'], data['verificacion_5_6'], data['observacion_5_6'],
            data['verificacion_6_1'], data['observacion_6_1'], data['verificacion_6_2'], data['observacion_6_2'],
            data['verificacion_6_3'], data['observacion_6_3'], data['verificacion_6_4'], data['observacion_6_4'],
            data['verificacion_6_5'], data['observacion_6_5'], data['verificacion_6_6'], data['observacion_6_6'],
            data['cantidad_7_1'], data['estado_7_1'], data['propiedad_7_1'],
            data['cantidad_7_4'], data['estado_7_4'], data['propiedad_7_4'],
            data['codigo_sede']
        ))


        conexion.commit()
    except pymysql.MySQLError as e:
        print(f"Error al ejecutar la consulta SQL: {e.args}")
    finally:
        cursor.close()
        conexion.close()



@infraestructura_bp.route('/infraestructura', methods=['GET'])
def mostrar_formulario_infraestructura():
    operadores = obtener_operador()
    instituciones = obtener_institucion()
    tipo_racion = obtener_tipo_racion()
    return render_template('infraestructura.html', operadores=operadores, instituciones=instituciones, tipo_racion=tipo_racion)

@infraestructura_bp.route('/get_sede/<int:institucion_id>', methods=['GET'])
def get_sede(institucion_id):
    try:
        sedes = obtener_sedes_por_institucion(institucion_id)
        return jsonify({'sedes': sedes})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@infraestructura_bp.route('/get_sede_details/<int:sede_id>', methods=['GET'])
def get_sede_details(sede_id):
    conexion = pymysql.connect(host='localhost', user='root', password='', db='pae_2')
    cursor = conexion.cursor()
    cursor.execute("SELECT codigo, direccion, comuna, zona FROM sedes WHERE id_sede = %s", (sede_id,))
    sede = cursor.fetchone()
    cursor.close()
    conexion.close()
    
    if sede:
        return jsonify({
            'codigo': sede[0],
            'direccion': sede[1],
            'comuna': sede[2],
            'zona': sede[3]
        })
    else:
        return jsonify({}), 404  # Añadir un código de estado 404 si no se encuentra la sede

@infraestructura_bp.route('/guardar_infraestructura', methods=['POST'])
def guardar_infraestructura():
    try:
        data = {
        'fecha': request.form.get('fecha', ''),
        'municipio': request.form.get('municipio', ''),
        'corregimiento': request.form.get('corregimiento', ''),
        'vereda': request.form.get('vereda', ''),
        'operador': request.form.get('operador', ''),
        'institucion': request.form.get('institucion', ''),
        'sede': request.form.get('sede', ''),
        'direccion': request.form.get('direccion', ''),
        'barrio': request.form.get('barrio', ''),
        'comuna': request.form.get('comuna', ''),
        'zona': request.form.get('zona', ''),
        'tipo_racion': request.form.get('tipo_racion', ''),
        'focalizacion': request.form.get('focalizacion', ''),
        'verificacion_1_1': int(request.form.get('verificacion_1_1', 0)),
        'observacion_1_1': request.form.get('observacion_1_1', ''),
        'verificacion_1_2': int(request.form.get('verificacion_1_2', 0)),
        'observacion_1_2': request.form.get('observacion_1_2', ''),
        'verificacion_1_3': int(request.form.get('verificacion_1_3', 0)),
        'observacion_1_3': request.form.get('observacion_1_3', ''),
        'verificacion_1_4': int(request.form.get('verificacion_1_4', 0)),
        'observacion_1_4': request.form.get('observacion_1_4', ''),
        'verificacion_2_1': int(request.form.get('verificacion_2_1', 0)),
        'observacion_2_1': request.form.get('observacion_2_1', ''),
        'verificacion_2_2': int(request.form.get('verificacion_2_2', 0)),
        'observacion_2_2': request.form.get('observacion_2_2', ''),
        'verificacion_2_3': int(request.form.get('verificacion_2_3', 0)),
        'observacion_2_3': request.form.get('observacion_2_3', ''),
        'verificacion_2_4': int(request.form.get('verificacion_2_4', 0)),
        'observacion_2_4': request.form.get('observacion_2_4', ''),
        'verificacion_2_5': int(request.form.get('verificacion_2_5', 0)),
        'observacion_2_5': request.form.get('observacion_2_5', ''),
        'verificacion_2_6': int(request.form.get('verificacion_2_6', 0)),
        'observacion_2_6': request.form.get('observacion_2_6', ''),
        'verificacion_2_7': int(request.form.get('verificacion_2_7', 0)),
        'observacion_2_7': request.form.get('observacion_2_7', ''),
        'verificacion_2_8': int(request.form.get('verificacion_2_8', 0)),
        'observacion_2_8': request.form.get('observacion_2_8', ''),
        'verificacion_2_9': int(request.form.get('verificacion_2_9', 0)),
        'observacion_2_9': request.form.get('observacion_2_9', ''),
        'verificacion_2_10': int(request.form.get('verificacion_2_10', 0)),
        'observacion_2_10': request.form.get('observacion_2_10', ''),
        'verificacion_2_11': int(request.form.get('verificacion_2_11', 0)),
        'observacion_2_11': request.form.get('observacion_2_11', ''),
        'verificacion_3_1': int(request.form.get('verificacion_3_1', 0)),
        'observacion_3_1': request.form.get('observacion_3_1', ''),
        'verificacion_3_2': int(request.form.get('verificacion_3_2', 0)),
        'observacion_3_2': request.form.get('observacion_3_2', ''),
        'verificacion_3_3': int(request.form.get('verificacion_3_3', 0)),
        'observacion_3_3': request.form.get('observacion_3_3', ''),
        'verificacion_3_4': int(request.form.get('verificacion_3_4', 0)),
        'observacion_3_4': request.form.get('observacion_3_4', ''),
        'verificacion_3_5': int(request.form.get('verificacion_3_5', 0)),
        'observacion_3_5': request.form.get('observacion_3_5', ''),
        'verificacion_3_6': int(request.form.get('verificacion_3_6', 0)),
        'observacion_3_6': request.form.get('observacion_3_6', ''),
        'verificacion_3_7': int(request.form.get('verificacion_3_7', 0)),
        'observacion_3_7': request.form.get('observacion_3_7', ''),
        'verificacion_3_8': int(request.form.get('verificacion_3_8', 0)),
        'observacion_3_8': request.form.get('observacion_3_8', ''),
        'verificacion_3_9': int(request.form.get('verificacion_3_9', 0)),
        'observacion_3_9': request.form.get('observacion_3_9', ''),
        'verificacion_3_10': int(request.form.get('verificacion_3_10', 0)),
        'observacion_3_10': request.form.get('observacion_3_10', ''),
        'verificacion_4_1': int(request.form.get('verificacion_4_1', 0)),
        'observacion_4_1': request.form.get('observacion_4_1', ''),
        'verificacion_4_2': int(request.form.get('verificacion_4_2', 0)),
        'observacion_4_2': request.form.get('observacion_4_2', ''),
        'verificacion_4_3': int(request.form.get('verificacion_4_3', 0)),
        'observacion_4_3': request.form.get('observacion_4_3', ''),
        'verificacion_4_4': int(request.form.get('verificacion_4_4', 0)),
        'observacion_4_4': request.form.get('observacion_4_4', ''),
        'verificacion_4_5': int(request.form.get('verificacion_4_5', 0)),
        'observacion_4_5': request.form.get('observacion_4_5', ''),
        'verificacion_4_6': int(request.form.get('verificacion_4_6', 0)),
        'observacion_4_6': request.form.get('observacion_4_6', ''),
        'verificacion_4_7': int(request.form.get('verificacion_4_7', 0)),
        'observacion_4_7': request.form.get('observacion_4_7', ''),
        'verificacion_4_8': int(request.form.get('verificacion_4_8', 0)),
        'observacion_4_8': request.form.get('observacion_4_8', ''),
        'verificacion_5_1': int(request.form.get('verificacion_5_1', 0)),
        'observacion_5_1': request.form.get('observacion_5_1', ''),
        'verificacion_5_2': int(request.form.get('verificacion_5_2', 0)),
        'observacion_5_2': request.form.get('observacion_5_2', ''),
        'verificacion_5_3': int(request.form.get('verificacion_5_3', 0)),
        'observacion_5_3': request.form.get('observacion_5_3', ''),
        'verificacion_5_4': int(request.form.get('verificacion_5_4', 0)),
        'observacion_5_4': request.form.get('observacion_5_4', ''),
        'verificacion_5_5': int(request.form.get('verificacion_5_5', 0)),
        'observacion_5_5': request.form.get('observacion_5_5', ''),
        'verificacion_5_6': int(request.form.get('verificacion_5_6', 0)),
        'observacion_5_6': request.form.get('observacion_5_6', ''),
        'verificacion_6_1': int(request.form.get('verificacion_6_1', 0)),
        'observacion_6_1': request.form.get('observacion_6_1', ''),
        'verificacion_6_2': int(request.form.get('verificacion_6_2', 0)),
        'observacion_6_2': request.form.get('observacion_6_2', ''),
        'verificacion_6_3': int(request.form.get('verificacion_6_3', 0)),
        'observacion_6_3': request.form.get('observacion_6_3', ''),
        'verificacion_6_4': int(request.form.get('verificacion_6_4', 0)),
        'observacion_6_4': request.form.get('observacion_6_4', ''),
        'verificacion_6_5': int(request.form.get('verificacion_6_5', 0)),
        'observacion_6_5': request.form.get('observacion_6_5', ''),
        'verificacion_6_6': int(request.form.get('verificacion_6_6', 0)),
        'observacion_6_6': request.form.get('observacion_6_6', ''),
        'cantidad_7_1': request.form.get('cantidad_7_1', ''),
        'estado_7_1': request.form.get('estado_7_1', ''),
        'propiedad_7_1': request.form.getlist('propiedad_7_1[]'),
        'cantidad_7_4': request.form.get('cantidad_7_4', ''),
        'estado_7_4': request.form.get('estado_7_4', ''),
        'propiedad_7_4': request.form.getlist('propiedad_7_4[]'),
        'codigo_sede': request.form.get('codigo_sede', '')
    }

        print('Datos recibidos:', data)  # Para depurar

        if not data['codigo_sede']:
            return "Error: Código de sede no proporcionado", 400

        insertar_visita_infraestructura(data)
        return redirect(url_for('index'))
    
    except KeyError as e:
        return f"Error: Faltan datos del formulario - {e}", 400
    except Exception as e:
        return f"Error inesperado: {e}", 500

