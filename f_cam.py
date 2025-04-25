import argparse
import csv
import random
import os

def generate_f_cam_data(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    timestamp = 100.0  # Start timestamp in seconds
    frame_id = 100
    speed = 60.0 # in km/h
    yaw_rate = 0.0 # rotation of the car in Z axis (degrees/s)
    signal1 = 0
    signal2 = 0
    signal1_fixed = None  # To hold the constant Signal1 value after FrameID > 200

    # Open the output CSV file for writing
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "FrameID", "Speed", "YawRate", "Signal1", "Signal2"])  # Header row

        for i in range(2000): # 2000 frames in total
            # Adding increment + random float between two values
            timestamp += 27.7 + random.uniform(-0.05, 0.05)

            # Speed increase in km/h
            if speed < 120:
                speed += 0.08
            else:
                speed = 120 + random.uniform(-0.05, 0.05) # if max speed, keep it around 120

            # noise +-1
            yaw_rate = random.uniform(-1,1)

            # After 200 frames, choose signal1 randomly from 1 to 15 (once) and keep it constant
            if frame_id > 200:
                if signal1_fixed is None:
                    signal1_fixed = random.randint(1,15)
                signal1 = signal1_fixed
            else:
                signal1 = 0 # if below 200 frames

            # Keep 0 when singal1 < 5, otherwise keep at 80 with noise
            if signal1 < 5:
                signal2 = 0
            else:
                signal2 = 80 + random.uniform(-10, 10)


            # write to CSV
            writer.writerow([
                round(timestamp, 6), # 6 digit precision
                frame_id,
                round(speed, 2), # 2 decimal points in km/h
                round(yaw_rate, 2), # 2 decimal point precision in deg/s
                signal1,
                signal2
            ])

            # iteration of frames
            frame_id += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="Path to output f_cam_out.csv")  # Accepts the file path as argument
    args = parser.parse_args()
    generate_f_cam_data(args.output)  # Run the function with the given path