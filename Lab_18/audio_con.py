import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt

rate_x, x = wavfile.read(r"C:\Users\saloni\Music\DEV1.wav")
rate_h, h = wavfile.read(r"C:\Users\saloni\Music\DEV2.wav")

# Convert to mono if stereo
if len(x.shape) > 1:
    x = x[:, 0]
if len(h.shape) > 1:
    h = h[:, 0]

# Normalize signals
x = x / np.max(np.abs(x))
h = h / np.max(np.abs(h))

linear_conv = fftconvolve(x, h, mode='full')
linear_conv = linear_conv / np.max(np.abs(linear_conv))  # normalize
'o'
N = max(len(x), len(h))  # length for circular convolution
X = np.fft.fft(x, N)
H = np.fft.fft(h, N)
circular_conv = np.real(np.fft.ifft(X * H))
circular_conv = circular_conv / np.max(np.abs(circular_conv))  # normalize

# wavfile.write(r"C:\Users\saloni\Music\output_linear.wav", rate_x, (linear_conv * 32767).astype(np.int16))
# wavfile.write(r"C:\Users\saloni\Music\output_circular.wav", rate_x, (circular_conv * 32767).astype(np.int16))

print("✅ Convolution completed successfully!")
print("Saved as output_linear.wav and output_circular.wav")

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(linear_conv)
plt.title("Linear Convolution Result")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(circular_conv, color='orange')
plt.title("Circular Convolution Result")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()