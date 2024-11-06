from flask import Flask, render_template
from flask import request
import json
import csv

app = Flask(__name__)

def json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

@app.route("/products")
def product_display():
    source = request.args.get('source', 'products.csv')
    product_id = request.args.get('product_id')
    products = []
    
    if source == 'json':
        products = json_file('products.json')
    elif source == 'csv':
        products = csv_file('products.csv')
    else:
        return render_template('product_display.html', products=products)

    if product_id:
        for product in products:
            if product.get('product_id') == product_id:
                return render_template('product_display.html', product=product)
        return 'Product not found', 404
    return render_template('product_display.html', products=products)

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)