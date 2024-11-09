from app import app, jsonify

products = [
    {
        "id": 1,
        "title": "Smartphone",
        "price": 699.99,
        "description": "A modern smartphone with a sleek design and advanced features.",
        "category": "Electronics",
            "image": "http://192.168.1.7:5050/static/images/product-1.png",
        "rating": {
            "count": 120,
            "rate": 4.7
        }
    },
    {
        "id": 2,
        "title": "Leather Handbag",
        "price": 149.99,
        "description": "A stylish leather handbag perfect for any occasion.",
        "category": "Fashion",
        "image": "http://192.168.1.7:5050/static/images/product-2.png",
        "rating": {
            "count": 85,
            "rate": 4.5
        }
    },
    {
        "id": 3,
        "title": "Honey & Essential Oils Set",
        "price": 39.99,
        "description": "A natural set including honey and essential oils for wellness.",
        "category": "Health & Beauty",
        "image": "http://192.168.1.7:5050/static/images/product-3.png",
        "rating": {
            "count": 45,
            "rate": 4.8
        }
    },
    {
        "id": 4,
        "title": "Wireless Headphones",
        "price": 129.99,
        "description": "Comfortable, high-quality wireless headphones with noise-cancelling feature.",
        "category": "Electronics",
        "image": "http://192.168.1.7:5050/static/images/product-4.png",
        "rating": {
            "count": 300,
            "rate": 4.6
        }
    },
    {
        "id": 5,
        "title": "Smartwatch",
        "price": 199.99,
        "description": "A smartwatch with fitness tracking and call capabilities.",
        "category": "Electronics",
        "image": "http://192.168.1.7:5050/static/images/product-5.png",
        "rating": {
            "count": 150,
            "rate": 4.4
        }
    },
    {
        "id": 6,
        "title": "Red Smartphone",
        "price": 749.99,
        "description": "A bold, stylish smartphone with a vibrant red finish.",
        "category": "Electronics",
        "image": "http://192.168.1.7:5050/static/images/product-6.png",
        "rating": {
            "count": 170,
            "rate": 4.7
        }
    },
    {
        "id": 7,
        "title": "DSLR Camera",
        "price": 599.99,
        "description": "Capture stunning photos with this high-resolution DSLR camera.",
        "category": "Electronics",
        "image": "http://192.168.1.7:5050/static/images/product-7.png",
        "rating": {
            "count": 90,
            "rate": 4.5
        }
    },
    {
        "id": 8,
        "title": "Running Shoes",
        "price": 89.99,
        "description": "Comfortable and durable running shoes for all terrains.",
        "category": "Sportswear",
        "image": "http://192.168.1.7:5050/static/images/product-8.png",
        "rating": {
            "count": 250,
            "rate": 4.6
        }
    },
    {
        "id": 9,
        "title": "Organic Skincare Set",
        "price": 59.99,
        "description": "A complete set of organic skincare products for healthy skin.",
        "category": "Health & Beauty",
        "image": "http://192.168.1.7:5050/static/images/product-9.png",
        "rating": {
            "count": 60,
            "rate": 4.9
        }
    },
    {
        "id": 10,
        "title": "Lotion Bottle",
        "price": 12.99,
        "description": "Moisturizing lotion in a sleek, portable bottle.",
        "category": "Health & Beauty",
        "image": "http://192.168.1.7:5050/static/images/product-10.png",
        "rating": {
            "count": 40,
            "rate": 4.3
        }
    }
]


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)
