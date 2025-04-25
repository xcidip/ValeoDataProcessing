import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run full simulation pipeline.")
    parser.add_argument("--f_cam_out", default="f_cam_out.csv", help="Output path for f_cam_out.csv")
    parser.add_argument("--sensor_out", default="sensor_out.csv", help="Output path for sensor_out.csv")
    parser.add_argument("--resim_out", default="resim_out.csv", help="Output path for resim_out.csv")
    args = parser.parse_args()

    # Run f_cam.py
    print("Generating f_cam output...")
    subprocess.run(["python", "f_cam.py", args.f_cam_out], check=True)

    # Run sensor.py
    print("Generating sensor output...")
    subprocess.run(["python", "sensor.py", args.sensor_out], check=True)

    # Run resim.py
    print("Running resim processing...")
    subprocess.run(["python", "resim.py", args.f_cam_out, args.sensor_out, args.resim_out], check=True)

    print("All steps completed successfully!")

if __name__ == "__main__":
    main()