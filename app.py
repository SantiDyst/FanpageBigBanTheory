# app.py
import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv() # Cargar variables de entorno desde .env

app = Flask(__name__)

# --- Configuración de la Base de Datos (cuando la conectes) ---
# Quita los datos de ejemplo y descomenta esto cuando tengas la DB
# DB_CONFIG = {
#     'host': os.environ.get('DB_HOST', 'localhost'),
#     'user': os.environ.get('DB_USER'),
#     'password': os.environ.get('DB_PASSWORD'),
#     'database': os.environ.get('DB_NAME')
# }

# def get_db_connection():
#     try:
#         conn = mysql.connector.connect(**DB_CONFIG)
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Error al conectar a la base de datos: {err}")
#         return None

# Función para obtener datos (simulada por ahora)
def get_data_from_db():
    # --- Datos de ejemplo para desarrollo (cuando conectes la DB, esto se eliminará) ---
    personajes = [
        {'id_personaje': 1, 'nombre': 'Sheldon Cooper', 'descripcion': 'Físico teórico excéntrico con doctorados y un intelecto prodigioso.', 'imagen_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b5/Sheldon_Cooper.jpg'},
        {'id_personaje': 2, 'nombre': 'Leonard Hofstadter', 'descripcion': 'Físico experimental y el mejor amigo de Sheldon, a menudo es la voz de la razón.', 'imagen_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e0/Leonard_Hofstadter.jpg'},
        {'id_personaje': 3, 'nombre': 'Penny', 'descripcion': 'Una aspirante a actriz y camarera, vecina y luego esposa de Leonard.', 'imagen_url': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Penny_%28Big_Bang_Theory%29.jpg'},
        {'id_personaje': 4, 'nombre': 'Howard Wolowitz', 'descripcion': 'Ingeniero aeroespacial y el único del grupo sin doctorado, pero con experiencia en el espacio.', 'imagen_url': 'https://upload.wikimedia.org/wikipedia/commons/e/e2/Howard_Wolowitz.jpg'},
        {'id_personaje': 5, 'nombre': 'Raj Koothrappali', 'descripcion': 'Astrofísico que inicialmente sufre de mutismo selectivo, incapaz de hablar con mujeres.', 'imagen_url': 'https://upload.wikimedia.org/wikipedia/commons/b/bd/Raj_Koothrappali.jpg'},
        {'id_personaje': 6, 'nombre': 'Bernadette Rostenkowski-Wolowitz', 'descripcion': 'Microbióloga con una voz peculiar, esposa de Howard.', 'imagen_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Bernadette_Rostenkowski-Wolowitz.jpg/800px-Bernadette_Rostenkowski-Wolowitz.jpg'},
        {'id_personaje': 7, 'nombre': 'Amy Farrah Fowler', 'descripcion': 'Neurobióloga, novia y luego esposa de Sheldon, con intereses científicos y sociales peculiares.', 'imagen_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Amy_Farrah_Fowler.jpg/800px-Amy_Farrah_Fowler.jpg'}
    ]
    episodios = [
        {'id_episodio': 1, 'titulo': 'Pilot', 'numero_temporada': 1, 'numero_episodio': 1, 'fecha_emision': '2007-09-24', 'resumen': 'Leonard y Sheldon conocen a su nueva vecina, Penny.', 'imagen_url': 'https://m.media-amazon.com/images/M/MV5BMjA3NTcwMTg4M15BMl5BanBnXkFtZTcwMjA3MzQ3MQ@@._V1_FMjpg_UX1000_.jpg'},
        {'id_episodio': 2, 'titulo': 'The Bath Item Gift Hypothesis', 'numero_temporada': 2, 'numero_episodio': 11, 'fecha_emision': '2008-12-15', 'resumen': 'Sheldon lucha con el concepto de regalos navideños.', 'imagen_url': 'https://images.fandango.com/ImageRenderer/0/0/rhodes_sm/redesign/static/img/default_poster.png/0/0/0/assets/no_sbox_placeholder.jpg/800/1200/overlay_image/E933075F-2AE2-40F1-A882-6DD661A05128.jpg'},
        {'id_episodio': 3, 'titulo': 'The Stockholm Syndrome', 'numero_temporada': 12, 'numero_episodio': 24, 'fecha_emision': '2019-05-16', 'resumen': 'El episodio final donde Sheldon y Amy reciben el Premio Nobel.', 'imagen_url': 'https://m.media-amazon.com/images/M/MV5BNTI0Y2UyMzYtYWE2Ny00MTY2LWIwMzItZGY3ZTcyMGRjMmYyXkEyXkFqcGdeQXVyNjg3MDAzNzA@._V1_.jpg'}
    ]
    actores = [
        {'id_actor': 1, 'nombre': 'Jim Parsons', 'fecha_nacimiento': '1973-03-24'},
        {'id_actor': 2, 'nombre': 'Johnny Galecki', 'fecha_nacimiento': '1975-04-30'}
    ]
    ubicaciones = [
        {'id_ubicacion': 1, 'nombre': 'Apartamento 4A', 'tipo': 'Residencial', 'direccion': 'Pasadena, CA'},
        {'id_ubicacion': 2, 'nombre': 'Caltech Cafeteria', 'tipo': 'Comida', 'direccion': 'California Institute of Technology'}
    ]
    relaciones_personajes = [
        {'personaje1_nombre': 'Sheldon Cooper', 'tipo_relacion': 'Compañeros de piso', 'personaje2_nombre': 'Leonard Hofstadter'},
        {'personaje1_nombre': 'Leonard Hofstadter', 'tipo_relacion': 'Pareja', 'personaje2_nombre': 'Penny'}
    ]
    # --- Fin datos de ejemplo ---

    # Cuando conectes la DB, usarías algo como esto:
    # conn = get_db_connection()
    # if conn:
    #     cursor = conn.cursor(dictionary=True)
    #     cursor.execute("SELECT ... FROM Personajes")
    #     personajes = cursor.fetchall()
    #     # ... y así para cada tabla
    #     cursor.close()
    #     conn.close()
    # return personajes, episodios, actores, ubicaciones, relaciones_personajes
    return personajes, episodios, actores, ubicaciones, relaciones_personajes


@app.route('/')
def home():
    # La página de inicio podría tener una introducción y enlaces a las secciones
    return render_template('index.html', active_page='home')

@app.route('/personajes')
def mostrar_personajes():
    personajes, _, _, _, _ = get_data_from_db() # Solo necesitamos personajes aquí
    return render_template('index.html', personajes=personajes, active_page='personajes')

@app.route('/episodios')
def mostrar_episodios():
    _, episodios, _, _, _ = get_data_from_db() # Solo necesitamos episodios aquí
    return render_template('index.html', episodios=episodios, active_page='episodios')

@app.route('/actores')
def mostrar_actores():
    _, _, actores, _, _ = get_data_from_db() # Solo necesitamos actores aquí
    return render_template('index.html', actores=actores, active_page='actores')

@app.route('/ubicaciones')
def mostrar_ubicaciones():
    _, _, _, ubicaciones, _ = get_data_from_db() # Solo necesitamos ubicaciones aquí
    return render_template('index.html', ubicaciones=ubicaciones, active_page='ubicaciones')

@app.route('/relaciones')
def mostrar_relaciones():
    _, _, _, _, relaciones_personajes = get_data_from_db() # Solo necesitamos relaciones aquí
    return render_template('index.html', relaciones_personajes=relaciones_personajes, active_page='relaciones')


if __name__ == '__main__':
    app.run(debug=True)