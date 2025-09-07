#d.	Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. Plot the original and scaled signals together.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_10Hz = np.sin(2 * np.pi * 10 * t)
sine_scaled = 3 * sine_10Hz

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, sine_10Hz, label="Original")
plt.plot(t, sine_scaled, label="Scaled (×3)", linestyle="--")
plt.title("Amplitude Scaling of 10 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
