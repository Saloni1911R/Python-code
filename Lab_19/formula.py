import numpy as np

def analyze_Hz():
    # coefficients of H(z)
    num = [0.5, -0.8, 0.315]
    den = [1, -1.0, 0.24]

    zeros = np.roots(num)
    poles = np.roots(den)

    print("H(z) = 0.5(z-0.7)(z-0.9)/(z-0.6)(z-0.4)")
    print("Zeros:", zeros)
    print("Poles:", poles)

    # Stability check
    stable = all(abs(p) < 1 for p in poles)
    print("Stability:", "Stable" if stable else "Unstable")


analyze_Hz()
