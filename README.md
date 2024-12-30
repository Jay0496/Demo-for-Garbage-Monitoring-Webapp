# Demo for Garbage Monitoring Webapp

This repository contains a demo web application for monitoring garbage bin levels and battery statuses of sensors. The application provides a visual representation of the bin's fullness, last three sensor readings, and warning notifications based on predefined thresholds. It is built using Flask for the backend and HTML/CSS for the frontend.

---

## Features

- **Real-Time Monitoring**: Refreshes every 5 seconds to display updated sensor data.
- **Sensor Selection**: Easily switch between sensors using the sidebar.
- **Warning Notifications**: Displays alerts for low battery levels, high bin fullness, or a combination of both.
- **Interactive UI**: Visual representation of bin fullness and a table of recent readings.

---

## Project Structure

```
.
├── templates/
│   └── index_demo.html   # HTML template for the web interface
├── demo_app.py           # Flask application logic
└── sensor_data.txt       # Simulated sensor data file (not included in the repository)
```

---

## Prerequisites

1. **Python 3.7+**
2. **Flask**: Install via pip:
   ```bash
   pip install flask
   ```

---

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/garbage-bin-monitoring.git
cd garbage-bin-monitoring
```

### 2. Prepare Sensor Data
- Create a `sensor_data.txt` file in the project root directory.
- Format: `sensor_id,fullness,battery`  
  Example:
  ```
  sensor_id,fullness,battery
  1,30,90
  2,50,80
  ```

### 3. Run the Application
```bash
python demo_app.py
```

- Access the application at `http://127.0.0.1:5000/`.

---

## File Descriptions

### `templates/index_demo.html`
- The frontend interface of the application.
- Includes a sidebar for sensor selection, a bin visualization area, and a table of recent readings.
- Implements a light green and forest green theme.

### `demo_app.py`
- Backend logic for loading sensor data, rendering the template, and handling user input.
- Updates the displayed data every 5 seconds.
- Simulates warnings for low battery and high fullness.

---

## How It Works

1. **Data Handling**:
   - The `sensor_data.txt` file is read at startup.
   - The file contains sensor readings, including bin fullness (%) and battery level (%).

2. **Visualization**:
   - A visual bin representation shows the current fullness.
   - The table lists the last three readings for the selected sensor.

3. **Warnings**:
   - Alerts are displayed based on:
     - **Low Battery**: Battery level ≤ 5%.
     - **High Fullness**: Fullness ≥ 95%.
     - **Combined Warning**: Both conditions are true.

---

## Note on `sensor_data.txt`
The `sensor_data.txt` file is required for the application to function but is not included in this repository. Create this file manually following the described format to test the application.

---

## Future Enhancements
- Integrate real sensor data via IoT devices.
- Add user authentication for secure access.
- Extend functionality to track multiple locations.
