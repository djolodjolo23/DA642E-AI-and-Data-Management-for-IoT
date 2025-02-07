import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("python/data.csv")  
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S")

plt.figure(figsize=(8, 4))
plt.plot(df["Time"], df["Temperature"], linestyle="-", color="b", label="Temperature (°C)")

plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()
