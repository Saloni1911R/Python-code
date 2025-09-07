#a.	Generate two sine wave signals with frequencies of 5 Hz and 10 Hz, both sampled at 1000 Hz for 1 second. Add the two signals together and plot the result.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_5Hz = np.sin(2 * np.pi * 5 * t)
sine_10Hz = np.sin(2 * np.pi * 10 * t)

# Addition
sum_signal = sine_5Hz + sine_10Hz

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, sine_5Hz, label="5 Hz Sine")
plt.plot(t, sine_10Hz, label="10 Hz Sine", linestyle="--")
plt.plot(t, sum_signal, label="Sum", linewidth=2)
plt.title("Addition of 5 Hz and 10 Hz Sine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
