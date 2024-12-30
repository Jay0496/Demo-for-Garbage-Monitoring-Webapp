import csv
import time
from flask import Flask, render_template, request
from threading import Thread

app = Flask(__name__)

# Global variable to store sensor data and track update index
sensor_data = []
update_index = 0
selected_sensor_id = "1"  # Default sensor to display
max_updates = 5  # Stop after 5 updates

def load_sensor_data():
    global sensor_data
    # Load the entire data file into a list of dictionaries
    with open('sensor_data.txt', 'r') as file:
        reader = csv.DictReader(file, fieldnames=["sensor_id", "fullness", "battery"])
        sensor_data = list(reader)

def get_sensor_readings(sensor_id):
    # Get all readings for the specified sensor
    return [row for row in sensor_data if row['sensor_id'] == sensor_id]


@app.route('/', methods=['GET', 'POST'])
def index():
    global update_index, selected_sensor_id

    if request.method == 'POST':
        selected_sensor_id = request.form.get("sensor_id")

    # Get all readings for the selected sensor
    readings = get_sensor_readings(selected_sensor_id)
    # Get the last 3 readings for the sensor
    current_readings = readings[max(0, update_index - 2):update_index + 1]

    # Initialize warning flags
    battery_warning = any(int(r["battery"]) <= 5 for r in current_readings)
    fullness_warning = int(current_readings[-1]["fullness"]) >= 95 if current_readings else False
    combined_warning = battery_warning and fullness_warning

    # Calculate fill height for the latest reading (set to 0 if no readings are available)
    fill_height = int(current_readings[-1]["fullness"]) if current_readings else 0

    return render_template(
        'index_demo.html', 
        sensors=sorted(set(row["sensor_id"] for row in sensor_data)), 
        selected_sensor=selected_sensor_id, 
        readings=current_readings, 
        battery_warning=battery_warning,
        fullness_warning=fullness_warning,
        combined_warning=combined_warning,
        fill_height=fill_height
    )


def update_data_index():
    global update_index
    while update_index < max_updates - 1:
        time.sleep(5)  # Update every 5 seconds
        update_index += 1

if __name__ == '__main__':
    load_sensor_data()
    Thread(target=update_data_index, daemon=True).start()
    app.run(debug=True)
