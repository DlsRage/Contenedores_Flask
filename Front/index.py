from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__,template_folder='templates')
CORS(app)

# Rutas para servir archivos HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autentificacion')
def authe():
    data = request.args.get('dato')
    return render_template('autentificacion.html', dato=data)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/productos')
def productos():
    return render_template('usuario_productos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)