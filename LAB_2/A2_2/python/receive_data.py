import serial
import csv
import time

"""
This script reads data from the serial port and writes it to a CSV file.
The data is expected to be in the following format:
Date: 2021-03-01 | Time: 12:34:56 | Acc: 1.23, 4.56, 7.89 | Gyro: 0.12, 3.45, 6.78
"""

SERIAL_PORT = '/dev/cu.usbmodem13201'
BAUD_RATE = 9600

CSV_FILENAME = "data.csv"
NUM_ENTRIES = 1200

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    except Exception as e:
        print(f"Failed to open serial port {SERIAL_PORT}: {e}")
        return

    print(f"Listening on {SERIAL_PORT} at {BAUD_RATE} baud...")

    time.sleep(2)
    with open(CSV_FILENAME, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Date", "Time", "Acc", "Gyro"])
        
        entry_count = 0

        while entry_count < NUM_ENTRIES:
            try:
                line = ser.readline().decode('utf-8').strip()
                if not line:
                    continue

                if line.startswith("Date:"):
                    try:
                        parts = line.split(" | ")
                        date_str = parts[0].split("Date: ")[1].strip()
                        time_str = parts[1].split("Time: ")[1].strip()
                        acc_str = parts[2].split("Acc: ")[1].strip()
                        gyro_str = parts[3].split("Gyro: ")[1].strip()
                        
                        csv_writer.writerow([date_str, time_str, acc_str, gyro_str])
                        entry_count += 1
                        print(f"Recorded entry {entry_count}: Date = {date_str}, Time = {time_str}, Acc = {acc_str}, Gyro = {gyro_str}")
                    except Exception as parse_err:
                        print(f"Parsing error on line: '{line}'. Error: {parse_err}")
                        continue
                else:
                    print(f"Ignored: {line}")
            except Exception as e:
                print(f"Error reading from serial: {e}")
                break

    ser.close()
    print("Finished capturing data.")

if __name__ == '__main__':
    main()
