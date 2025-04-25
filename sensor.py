import csv
import random
import argparse

def generate_sensor_data(output_path):
    timestamp = 100.0  # seconds
    speed = 60.0 # km/h

    # open file for writing csv
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Speed"]) # header row of CSV file

        # time value should not exceed 160 seconds, after if reaches, data is finished
        while timestamp < 160.0:
            writer.writerow([round(timestamp, 6), round(speed, 2)]) # write row of data with rounded numbers

            # incrementing time from 100 to 160
            timestamp += 0.2 + random.uniform(-0.01, 0.01)

            # if speed exceeds 120, keep it at 120 with noise
            if speed < 120:
                speed += 0.56
            else:
                speed = 120 + random.uniform(-0.1, 0.1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="Path to output sensor_out.csv") # Accepts the file path as argument
    args = parser.parse_args()

    generate_sensor_data(args.output)