from flask import Flask, render_template, jsonify, request as flask_request
import json
import os
import MySQLdb

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_metadata():
    """Charge les métadonnées depuis le fichier JSON dans deploy"""
    metadata_path = os.path.join(os.path.dirname(__file__), '..', 'deploy', 'metadata.json')
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "site": {"name": "CyberCTF Library", "description": "A Capture The Flag platform"},
            "navigation": {"main": [], "auth": []},
            "footer": {"links": [], "social": []},
            "challenge": {"title": "Challenge", "description": "Description", "skills": [], "points": 0},
            "cta": {"label": "Start", "link": "/"}
        }

DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'appuser'),
    'passwd': os.environ.get('DB_PASSWORD', 'apppass'),
    'db': os.environ.get('DB_NAME', 'shopdb'),
    'charset': 'utf8mb4'
}

def get_db_connection():
    return MySQLdb.connect(**DB_CONFIG)

@app.route('/')
def home():
    metadata = load_metadata()
    return render_template('home.html', metadata=metadata)

@app.route('/api/metadata')
def api_metadata():
    return jsonify(load_metadata())

@app.route('/lab')
def lab():
    metadata = load_metadata()
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('SELECT id, name, price FROM products')
        products = cur.fetchall()
        cur.close()
        db.close()
    except Exception as e:
        products = []
    return render_template('lab.html', metadata=metadata, products=products)

@app.route('/lab/product')
def lab_product():
    metadata = load_metadata()
    product = None
    error = None
    id_param = flask_request.args.get('id', '')
    try:
        db = get_db_connection()
        cur = db.cursor()
        # VULNERABLE: id_param is concatenated directly
        query = f"SELECT id, name, description, price FROM products WHERE id = {id_param}"
        cur.execute(query)
        product = cur.fetchone()
        cur.close()
        db.close()
    except Exception as e:
        error = str(e)
    return render_template('lab_product.html', metadata=metadata, product=product, error=error, id_param=id_param)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 