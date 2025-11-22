import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

# Load your audio file
audio, sample_rate = sf.read(r"C:\Users\saloni\Music\DEV2.wav")

# Write audio file (optional)
sf.write("new_audio_file.wav", audio, sample_rate)

# Create time axis
time = np.arange(0, len(audio)) / sample_rate

# Plot audio signal
plt.plot(time, audio)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Audio Waveform of DEV2.wav")
plt.grid()
plt.show()
