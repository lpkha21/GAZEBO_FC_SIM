import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("build/flight_log.csv", header=None)

df.columns = [
    "time","throttle","roll","pitch","yaw","m1","m2","m3","m4"
]

fig, ax = plt.subplots(2,1, figsize=(12,8))

# PID outputs
ax[0].plot(df["time"], df["roll"], label="roll PID")
ax[0].plot(df["time"], df["pitch"], label="pitch PID")
ax[0].plot(df["time"], df["yaw"], label="yaw PID")
ax[0].set_title("PID Outputs")
ax[0].legend()

# Motors
ax[1].plot(df["time"], df["m1"], label="m1")
ax[1].plot(df["time"], df["m2"], label="m2")
ax[1].plot(df["time"], df["m3"], label="m3")
ax[1].plot(df["time"], df["m4"], label="m4")
ax[1].set_title("Motor Outputs")
ax[1].legend()

plt.show()