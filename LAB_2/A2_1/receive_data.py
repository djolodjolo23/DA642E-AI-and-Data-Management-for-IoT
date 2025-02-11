import serial
import csv
import time

"""
This script reads data from the serial port and writes it to a CSV file.
The data is expected to be in the following format:
Time: 12:34:56 | Temp: 30.6
"""

SERIAL_PORT = '/dev/cu.usbmodem1101'
BAUD_RATE = 9600

CSV_FILENAME = "python/data.csv"
NUM_ENTRIES = 900

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
        csv_writer.writerow(["Time", "Temperature"])
        
        entry_count = 0

        while entry_count < NUM_ENTRIES:
            try:
                line = ser.readline().decode('utf-8').strip()
                if not line:
                    continue

                if line.startswith("Time:"):
                    try:
                        parts = line.split(" | Temp: ")
                        time_str = parts[0].split("Time: ")[1].strip()
                        temp_str = parts[1].strip()
                        
                        csv_writer.writerow([time_str, temp_str])
                        entry_count += 1
                        print(f"Recorded entry {entry_count}: Time = {time_str}, Temp = {temp_str}")
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
