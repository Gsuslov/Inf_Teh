from app import app
from flask import jsonify
import requests

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from App1!"})

@app.route('/api/app2')
def cross():
  x = requests.get('http://localhost:7777/api')
  return jsonify(x.json())
