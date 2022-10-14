from app import app
from flask import jsonify
import requests
import os

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from first app"})

@app.route('/api/app2')
def cross():
  x = requests.get('http://localhost:'+os.getenv('PORT2')+'/api')
  return jsonify(x.json())
