#c.	Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds. Plot the original and shifted signals on the same graph for comparison.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_original = np.sin(2 * np.pi * 5 * t)
sine_shifted = np.sin(2 * np.pi * 5 * (t - 0.1))

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, sine_original, label="Original")
plt.plot(t, sine_shifted, label="Shifted by 0.1s", linestyle="--")
plt.title("Time-Shifted 5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
