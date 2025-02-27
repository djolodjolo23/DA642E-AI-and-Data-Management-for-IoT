import os
import random
import subprocess
from pydub import AudioSegment
import numpy as np

labels = ['apple', 'orange', 'cherry', 'unknown']
clips_per_label = 60
clip_duration_ms = 3000
sample_rate = 16000

# Available voices for the say command on macOS
available_voices = [
    "Albert", "Alice", "Alva", "Amélie", "Amira", "Anna", "Bad News", "Bahh", "Bells", "Boing",
    "Bubbles", "Carmit", "Cellos", "Damayanti", "Daniel", "Daria", "Eddy", "Ellen", "Flo", "Fred",
    "Good News", "Grandma", "Grandpa", "Jester", "Ioana", "Jacques", "Joana", "Junior", "Kanya",
    "Karen", "Kathy", "Kyoko", "Lana", "Laura", "Lekha", "Lesya", "Linh", "Luciana", "Majed",
    "Tünde", "Meijia", "Melina", "Milena", "Moira", "Mónica", "Montse", "Nora", "Organ", "Paulina",
    "Superstar", "Ralph", "Reed", "Rishi", "Rocko", "Samantha", "Sandy", "Sara", "Satu", "Shelley",
    "Sinji", "Tessa", "Thomas", "Tina", "Tingting", "Trinoids", "Whisper", "Xander", "Yelda",
    "Yuna", "Zarvox", "Zosia", "Zuzana"
]

voices = random.sample(available_voices, 20) 
print(voices)

speech_patterns = [
    ((0, 800), (1000, 2200), (130, 180)),  
    ((800, 1500), (300, 1000), (170, 220)),  
    ((1500, 2200), (0, 500), (150, 200)), 
]


output_dir = "audio_clips"
os.makedirs(output_dir, exist_ok=True)

for label in labels:
    label_dir = os.path.join(output_dir, label)
    os.makedirs(label_dir, exist_ok=True)

    for i in range(clips_per_label):
        out_file = os.path.join(label_dir, f"{label}_{i + 1:02d}.wav")

        if label != "unknown":
            pre_silence_range, post_silence_range, rate_range = random.choice(speech_patterns)
            voice = random.choice(voices)
            rate = random.randint(*rate_range)
            pre_silence = random.randint(*pre_silence_range)
            post_silence = random.randint(*post_silence_range)

            temp_file = os.path.join(label_dir, f"temp_{i}.aiff")
            command = ["say", "-v", voice, "-r", str(rate), label, "-o", temp_file]
            subprocess.run(command, check=True)
            audio = AudioSegment.from_file(temp_file, format="aiff")
            os.remove(temp_file)

            spoken_audio = (
                AudioSegment.silent(duration=pre_silence) +
                audio +
                AudioSegment.silent(duration=post_silence)
            )
            if len(spoken_audio) < clip_duration_ms:
                spoken_audio += AudioSegment.silent(duration=clip_duration_ms - len(spoken_audio))
            else:
                spoken_audio = spoken_audio[:clip_duration_ms]

            num_samples = int(sample_rate * (clip_duration_ms / 1000))
            noise_array = np.random.uniform(-1, 1, size=num_samples)

            fade_samples = int(sample_rate * 0.1)
            fade_in = np.linspace(0, 1, fade_samples)
            fade_out = np.linspace(1, 0, fade_samples)
            noise_array[:fade_samples] *= fade_in
            noise_array[-fade_samples:] *= fade_out

            noise_array = (noise_array * 50).astype(np.int16)
            background_noise = AudioSegment(
                noise_array.tobytes(),
                frame_rate=sample_rate,
                sample_width=noise_array.dtype.itemsize,
                channels=1
            )

            final_audio = background_noise.overlay(spoken_audio)

            if len(final_audio) < clip_duration_ms:
                final_audio += AudioSegment.silent(duration=clip_duration_ms - len(final_audio))
            else:
                final_audio = final_audio[:clip_duration_ms]

            final_audio.export(out_file, format="wav", parameters=["-ar", str(sample_rate)])
            print(f"Saved {out_file} (voice: {voice}, rate: {rate} wpm, pattern: {pre_silence}ms pre, {post_silence}ms post)")
        else:
            num_samples = int(sample_rate * (clip_duration_ms / 1000))
            noise_array = np.random.uniform(-1, 1, size=num_samples)

            fade_samples = int(sample_rate * 0.1)
            fade_in = np.linspace(0, 1, fade_samples)
            fade_out = np.linspace(1, 0, fade_samples)
            noise_array[:fade_samples] *= fade_in
            noise_array[-fade_samples:] *= fade_out

            noise_array = (noise_array * 200).astype(np.int16)
            audio = AudioSegment(
                noise_array.tobytes(),
                frame_rate=sample_rate,
                sample_width=noise_array.dtype.itemsize,
                channels=1
            )

            if len(audio) < clip_duration_ms:
                audio += AudioSegment.silent(duration=clip_duration_ms - len(audio))
            else:
                audio = audio[:clip_duration_ms]
            audio.export(out_file, format="wav")
            print(f"Saved {out_file} (unknown noise)")
