from app import app
from flask import jsonify
import requests
import os

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from App2!"})


