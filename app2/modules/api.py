from app import app
from flask import jsonify
import requests

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from App2!"})

@app.route('/api/app1')
def cross():
  x = requests.get('http://localhost:6969/api')
  return jsonify(x.json())

