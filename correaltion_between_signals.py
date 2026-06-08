import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Define the Time Axis and Signals from the image
dt = 0.01
t = np.arange(-2, 5, dt)

# Signal A: Rectangular pulse from t=1 to 2, height 2
sigA = np.where((t >= 1) & (t <= 2), 2.0, 0.0)

# Signal B: Ramp from t=1 (height 2) to t=2 (height 0)
# Equation: y = -2t + 4 for 1 <= t <= 2
sigB = np.where((t >= 1) & (t <= 2), -2*t + 4, 0.0)

# --- CONFIGURATION ---
# Options: 'convolution', 'cross_correlation', 'auto_correlation_A'
MODE = 'Auto-Correlation' 

if MODE == 'convolution':
    f = sigA
    g = sigB[::-1]  # Flip for convolution
    title_text = "Convolution: (A * B)"
elif MODE == 'cross_correlation':
    f = sigA
    g = sigB        # No flip for correlation
    title_text = "Cross-Correlation: (A \u2605 B)"
else: # auto_correlation_A
    f = sigA
    g = sigA        # Self-correlation
    title_text = "Auto-Correlation: (A \u2605 A)"

# Calculate the actual mathematical result for the bottom plot
result = np.convolve(f, g, mode='full') * dt
# Time axis for the result
res_t = np.linspace(t[0] + t[0], t[-1] + t[-1], len(result))

# 2. Setup Figure
fig, (ax_in, ax_ani, ax_out) = plt.subplots(3, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=0.4)

# Top Plot: Static Inputs
ax_in.plot(t, sigA, 'b', label='Signal A (Rect)')
ax_in.plot(t, sigB, 'r', ls='--', label='Signal B (Ramp)')
ax_in.set_title("Input Signals from Image")
ax_in.legend(loc='upper right')
ax_in.grid(True, alpha=0.3)

# Middle Plot: Animation
ax_ani.set_title(f"Animation: {title_text}")
line_f, = ax_ani.plot(t, f, 'b', lw=2, label='Fixed Signal')
line_g, = ax_ani.plot([], [], 'r', lw=2, label='Sliding Signal')
fill = ax_ani.fill_between([], [], color='purple', alpha=0.3)
ax_ani.set_xlim(-2, 5)
ax_ani.set_ylim(-0.5, 2.5)
ax_ani.legend(loc='upper right')

# Bottom Plot: Result Output
ax_out.set_title("Resulting Output Signal")
line_out, = ax_out.plot([], [], 'g', lw=2)
ax_out.set_xlim(min(res_t), max(res_t))
ax_out.set_ylim(-0.1, max(result) + 0.5)
ax_out.grid(True, alpha=0.3)

# 3. Animation Update Logic
def update(frame):
    # Calculate shift for the sliding signal
    shift_idx = frame - len(t)//2
    shift_val = shift_idx * dt
    
    # Update sliding signal position
    shifted_t = t + shift_val
    line_g.set_data(shifted_t, g)
    
    # Update output plot up to current frame
    # (Mapping frame index to result index)
    out_idx = int((frame / len(t)) * len(result))
    line_out.set_data(res_t[:out_idx], result[:out_idx])
    
    return line_g, line_out

ani = FuncAnimation(fig, update, frames=len(t), interval=10, blit=True)

plt.show()