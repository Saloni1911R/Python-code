#e.	Generate a 5 Hz sine wave and reverse it in time. Plot the original and reversed signals on the same graph. 
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_5Hz = np.sin(2 * np.pi * 5 * t)
sine_reversed = sine_5Hz[::-1]

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, sine_5Hz, label="Original")
plt.plot(t, sine_reversed, label="Reversed", linestyle="--")
plt.title("Time-Reversed 5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
