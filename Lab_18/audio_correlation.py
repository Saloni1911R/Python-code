import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load the audio files
# -------------------------------
files = {
    "DEV1": r"C:\Users\saloni\Music\DEV1.wav",
    "DEV2": r"C:\Users\saloni\Music\DEV2.wav"
}

signals = {}
rates = {}

for key, path in files.items():
    rate, sig = wavfile.read(path)
    rates[key] = rate
    # Convert stereo to mono if needed
    if len(sig.shape) > 1:
        sig = sig[:, 0]
    # Normalize
    sig = sig / np.max(np.abs(sig))
    signals[key] = sig

# -------------------------------
# Step 2: Autocorrelation
# -------------------------------
autocorr_results = {}
for key, sig in signals.items():
    autocorr = correlate(sig, sig, mode='full')
    autocorr = autocorr / np.max(np.abs(autocorr))  # normalize
    autocorr_results[key] = autocorr

# -------------------------------
# Step 3: Cross-correlation
# -------------------------------
crosscorr_results = {
    "DEV1_DEV2": correlate(signals["DEV1"], signals["DEV2"], mode='full')
}
# Normalize cross-correlation
crosscorr_results["DEV1_DEV2"] = crosscorr_results["DEV1_DEV2"] / np.max(np.abs(crosscorr_results["DEV1_DEV2"]))

# -------------------------------
# Step 4: Visualization
# -------------------------------

# Autocorrelation plots
plt.figure(figsize=(12, 6))
for idx, (key, autocorr) in enumerate(autocorr_results.items(), start=1):
    plt.subplot(2, 1, idx)
    plt.plot(autocorr)
    plt.title(f"Autocorrelation of {key}")
    plt.xlabel("Lag")
    plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

# Cross-correlation plot
plt.figure(figsize=(10, 4))
plt.plot(crosscorr_results["DEV1_DEV2"], color='orange')
plt.title("Cross-correlation: DEV1 vs DEV2")
plt.xlabel("Lag")
plt.ylabel("Amplitude")
plt.show()