#b.	Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz for 2 seconds. Multiply the two signals element-wise and plot the resulting signal.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  
t = np.linspace(0, 2, 2*fs, endpoint=False)

# Signals
sine_5Hz = np.sin(2 * np.pi * 5 * t)
cosine_10Hz = np.cos(2 * np.pi * 10 * t)

# Multiplication
product_signal = sine_5Hz * cosine_10Hz

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, product_signal, color="purple")
plt.title("Multiplication of 5 Hz Sine and 10 Hz Cosine")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
