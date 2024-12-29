import time
import psutil
import requests
import json

FLASK_URL = "http://127.0.0.1:5000/metrics"
SERVER_ID = "Server1" 

while True:
    
    metrics = {
        "server_id": SERVER_ID,
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
    }

    try:
        
        response = requests.post(FLASK_URL, json=metrics)
        print(f"Sent metrics: {metrics}, Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send metrics: {e}")

    time.sleep(5)  
