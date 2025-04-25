import csv
import argparse
import os

# load sensor data from a file to make a dictionary out of it
def load_sensor_data(sensor_file):
    sensor_data = []
    with open(sensor_file, 'r') as csvfile:
        # make a dictionary reader for time and speed
        reader = csv.DictReader(csvfile)
        for row in reader:
            # add data to dictionary
            sensor_data.append({
                "Timestamp": float(row["Timestamp"]),
                "Speed": float(row["Speed"])
            })
    return sensor_data

# find the most recent value of speed between
def find_latest_sensor_speed(sensor_data, timestamp):
    latest_speed = None # base value
    for entry in sensor_data:
        if entry["Timestamp"] <= timestamp: # deciding if data from sensor is sooner
            latest_speed = entry["Speed"] # setting the latest speed
        else:
            break
    return latest_speed


# fusing camera and sensor data together
def process_resim(f_cam_path, sensor_file, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    sensor_data = load_sensor_data(sensor_file)

    with open(f_cam_path, 'r') as f_cam_csv, open(output_path, 'w', newline='') as out_csv: # opening camera data and output file for writing
        reader = csv.DictReader(f_cam_csv) # Reading from front camera data
        writer = csv.writer(out_csv) # Writing into output
        writer.writerow(["Timestamp", "FrameID", "Speed", "YawRate", "Signal1", "Signal2"]) # header row for output file

        # reading data from front camera file and sensor
        for row in reader:
            timestamp = float(row["Timestamp"])
            front_speed = float(row["Speed"])
            latest_sensor_speed = find_latest_sensor_speed(sensor_data, timestamp) # finding the latest speed from front camera and sensor

            if latest_sensor_speed is not None:
                avg_speed = round((front_speed + latest_sensor_speed) / 2, 2) #
            else:
                avg_speed = front_speed  # fallback if no earlier sensor data

            # writing the data into the final output file with appropriate rounding
            writer.writerow([
                round(timestamp, 6), # time with 6 decimal places
                int(row["FrameID"]),
                avg_speed,
                float(row["YawRate"]), # Z axis car rotation
                int(row["Signal1"]),
                float(row["Signal2"])
            ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f_cam_input", help="Path to f_cam_out.csv") # Accepts the file path as argument
    parser.add_argument("sensor_input", help="Path to sensor_out.csv") # Accepts the file path as argument
    parser.add_argument("output", help="Path to output resim_out.csv") # Accepts the file path as argument
    args = parser.parse_args()

    process_resim(args.f_cam_input, args.sensor_input, args.output) # run the main script
