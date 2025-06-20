from flask import Flask, jsonify, request
from flask_cors import CORS
import pyotp
import qrcode
from io import BytesIO
import base64
from models import db, User
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Buscar usuario existente
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Generar nuevo secret para Google Authenticator
    secret = pyotp.random_base32()

    try:
        # Actualizar el secret del usuario
        user.secret = secret
        db.session.commit()

        # Generar QR code
        totp = pyotp.TOTP(secret)
        provisioning_uri = totp.provisioning_uri(
            username,
            issuer_name="YourApp"
        )

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(provisioning_uri)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        qr_base64 = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({
            'message': 'QR code generated successfully',
            'qr_code': qr_base64
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/verify', methods=['POST'])
def verify_totp():
    data = request.get_json()
    username = data.get('username')
    code = data.get('code')

    if not code:
        return jsonify({'error': 'Username and token are required'}), 400

    user = User.query.filter_by(username=username).first()
    
    secret = user.secret
    if not secret:
        return jsonify({'error': 'User not found'}), 404

    totp = pyotp.TOTP(secret)
    
    # Verificar el código
    if totp.verify(code):
        return jsonify({
            'verified': True,
            'message': 'Code verified successfully'
        })
    else:
        return jsonify({
            'verified': True,
            'message': 'Invalid code'
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000,host="0.0.0.0")