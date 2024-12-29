# Server Monitoring Application

This application provides a simple server monitoring solution, allowing you to collect and visualize CPU, memory, and disk usage metrics from multiple servers in real-time. The application consists of a Flask server that receives metrics from agents running on monitored servers and displays them on a web dashboard.

## Components

### 1. `main.py`
This is the main Flask application that serves as the backend for the monitoring system.

- **Endpoints**:
  - `POST /metrics`: Receives server metrics (CPU, memory, disk) in JSON format. The metrics are associated with a unique server ID and stored in memory.
  - `GET /dashboard`: Renders a dashboard displaying the metrics of all monitored servers.
  - `GET /`: Redirects to the `/dashboard`.

- **How to Run**:
  1. Ensure you have Flask installed:
     ```bash
     pip install Flask
     ```
  2. Run the application:
     ```bash
     python main.py
     ```
  3. Access the dashboard at `http://127.0.0.1:5000/dashboard`.

### 2. `dashboard.html`
This is the HTML template for the server monitoring dashboard.

- **Features**:
  - Displays a table of server metrics, including Server ID, CPU Usage, Memory Usage, and Disk Usage.
  - The data is populated dynamically using Flask's templating engine.

- **Styling**:
  - Basic styling is included to enhance the appearance of the dashboard, using CSS for table formatting.

### 3. `agent.py`
This script acts as an agent running on a monitored server. It collects CPU, memory, and disk usage metrics using the `psutil` library and sends them to the Flask application.

- **How It Works**:
  1. Collects metrics every 5 seconds.
  2. Sends the metrics to the Flask server via a POST request to the `/metrics` endpoint.

- **How to Run**:
  1. Ensure you have `psutil` and `requests` libraries installed:
     ```bash
     pip install psutil requests
     ```
  2. Run the agent script:
     ```bash
     python agent.py
     ```

## Requirements
- Python 3.x
- Flask
- psutil
- requests


