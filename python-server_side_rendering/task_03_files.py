from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filename):
    with open(filename) as f:
        data = json.load(f)
        products = [
            product for product in data
            if "id" in product and "name" in product and "category" in product and "price" in product
        ]
    return products

def read_csv_file(filename):
    products = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "id" in row and "name" in row and "category" in row and "price" in row:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error_message="Wrong source")

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error_message="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
