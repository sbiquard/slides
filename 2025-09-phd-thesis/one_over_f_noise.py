# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy>2",
#   "matplotlib>3",
#   "seaborn",
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme(context='talk', style='ticks')

# Generate frequency points
f = np.logspace(-3, 2, 1000)

# Parameters
f_knee = 0.1  # knee frequency
white_noise = 1.0  # white noise level
alpha = -1.0  # slope

# Generate 1/f spectrum
spectrum = white_noise * (1 + (f / f_knee) ** alpha)

# Create log-log plot
plt.figure(figsize=(8, 6))
plt.loglog(f, spectrum)
plt.loglog(f, white_noise * (f / f_knee) ** alpha, '--', alpha=0.5)
plt.loglog(f, white_noise * np.ones_like(f), '--', alpha=0.5)
plt.grid(True)
plt.ylim(bottom=0.5)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')
plt.title('1/f Noise Spectrum')

# Add arrows pointing to key features
plt.annotate(
    'White noise\n level $\\sigma$',
    xy=(10, white_noise),
    xytext=(10, 3),
    arrowprops=dict(facecolor='black', shrink=0.05),
)
plt.annotate(
    'Knee frequency',
    xy=(f_knee, white_noise),
    xytext=(0.03, 3.0),
    arrowprops=dict(facecolor='black', shrink=0.05),
)
plt.annotate(
    r'Slope $\alpha$',
    xy=(0.01, 10),
    xytext=(0.002, 3),
    arrowprops=dict(facecolor='black', shrink=0.05),
)

plt.savefig('assets/one_over_f_spectrum.svg', dpi=300, bbox_inches='tight')
