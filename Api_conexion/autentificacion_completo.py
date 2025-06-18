from flask import Flask, request, jsonify  
import psycopg2
from werkzeug.security import check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite todas las solicitudes cross-origin por defecto
app.secret_key = 'tu_clave_secreta'  # Necesario para mensajes flash

def connection_user():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="myuser",
            password="mypassword",
            host="db",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error en la conexión o consulta:", e)
        return None

def authenticate(username, password):
    try:
        conn = connection_user()
        cur = conn.cursor()
        cur.execute('SELECT password FROM "user" WHERE username = %s', (username,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            stored_password = result[0]
            print(stored_password)
            # Aquí depende si la contraseña está hasheada o en texto plano:
            # Si está en texto plano (no recomendado), compara directamente:
            return stored_password == password

            # Si está hasheada (recomendado), usa:
            # return check_password_hash(stored_password, password)
        else:
            return False
    except Exception as e:
        print("Error en la conexión o consulta:", e)
        return False


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get('usuario')
    pwd = data.get('contrasena')
    if authenticate(user,pwd):
        return jsonify({'mensaje': 'Login exitoso'})
    else:
        return jsonify({'mensaje': 'Usuario o contraseña incorrectos'}), 401
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
