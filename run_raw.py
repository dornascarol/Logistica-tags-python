from flask import Flask, request
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.route('/create_tag', method = ["POST"])
def create_tag():
    body = request.json
    product_code = body.get('product_code')
    
    tag = Code128(product_code, writer = ImageWriter())
    path_from_tag = f'{tag}'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000) 