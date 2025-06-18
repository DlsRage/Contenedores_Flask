from flask import Flask, request, jsonify
from models2 import db2, Product
from config2 import Config2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config2)
db2.init_app(app)

with app.app_context():
    db2.create_all()

#### PRODUCTOS

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        stock=data['stock']
    )
    db2.session.add(new_product)
    db2.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/products', methods=['GET'])
def get_products_2():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'stock': product.stock
    } for product in products])

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'stock': product.stock
    })

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.price = data['price']
    product.description = data['description']
    product.stock = data['stock']
    db2.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db2.session.delete(product)
    db2.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

