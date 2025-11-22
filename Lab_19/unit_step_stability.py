import numpy as np

def z_transform_unit_step():
    # Z-transform of u[n] = z / (z - 1)
    numerator = [1, 0]      # z
    denominator = [1, -1]   # (z - 1)

    poles = np.roots(denominator)
    zeros = np.roots(numerator)

    print("Z-Transform U(z) = z / (z - 1)")
    print("Zeros:", zeros)
    print("Poles:", poles)

    # Stability check
    stable = all(abs(p) < 1 for p in poles)
    print("Stability:", "Stable" if stable else "Unstable")


z_transform_unit_step()
