import os
import csv

audio_dir = "audio_clips"
csv_filename = "audio_clips/dataset.csv"

with open(csv_filename, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["filename", "label"])

    for label in os.listdir(audio_dir):
        label_dir = os.path.join(audio_dir, label)

        if os.path.isdir(label_dir):
            for filename in os.listdir(label_dir):
                if filename.endswith(".wav"):
                    writer.writerow([filename, label])

print(f"CSV file '{csv_filename}' has been created successfully.")
