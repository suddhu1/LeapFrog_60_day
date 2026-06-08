import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ================= USER SETTING =================
HER_NAME = "My Love ❤️"   # ← change this
# ===============================================

fig = plt.figure(figsize=(6, 8))
ax = fig.add_subplot(111, projection="3d")

# ---------- STEM ----------
z_stem = np.linspace(-4.5, 0, 400)
x_stem_base = 0.05 * np.sin(z_stem)
y_stem = np.zeros_like(z_stem)

# ---------- FLOATING PETALS ----------
floating_petals = [
    [np.random.uniform(-1, 1),
     np.random.uniform(-1, 1),
     np.random.uniform(1, 3),
     np.random.uniform(0.01, 0.03)]
    for _ in range(14)
]

# ---------- ROSE PETAL LAYER ----------
def rose_layer(layer, open_factor):
    theta = np.linspace(0, 2*np.pi, 180)
    r = np.linspace(0.05, 1, 120)
    T, R = np.meshgrid(theta, r)

    # Spiral phyllotaxis
    T += layer * np.pi / 6

    # Shape controls
    cup = 0.7 + 0.5 * open_factor          # prevents flat start
    curl = 1 - 0.55 * R
    wave = 0.25 * np.sin(6*T + layer)

    X = R * np.cos(T) * curl
    Y = R * np.sin(T) * curl
    Z = cup * (R**2) + wave * (1 - R)

    Z += layer * 0.14  # layer stacking

    return X, Y, Z

# ---------- LEAF SHAPE ----------
u = np.linspace(0, np.pi, 40)
v = np.linspace(0, np.pi, 40)
U, V = np.meshgrid(u, v)

leaf_x = 0.7 * np.sin(U) * np.cos(V)
leaf_y = 0.35 * np.sin(U) * np.sin(V)
leaf_z = -1.4 + 0.15 * np.cos(U)

# ---------- ANIMATION ----------
def animate(frame):
    ax.clear()
    ax.set_facecolor("black")
    ax.axis("off")

    open_factor = min(frame / 90, 1)

    # 🌹 Rose bloom (layered)
    for layer in range(5):
        X, Y, Z = rose_layer(layer, open_factor)
        ax.plot_surface(
            X, Y, Z,
            color=(0.75, 0.1 + layer*0.08, 0.15),
            alpha=0.96,
            linewidth=0
        )

    # 🌱 Stem sway
    sway = 0.03 * np.sin(frame * 0.04)
    ax.plot(
        x_stem_base + sway,
        y_stem,
        z_stem,
        color="#1f7a1f",
        linewidth=4
    )

    # 🍃 Leaves gentle motion
    leaf_sway = 0.15 * np.sin(frame * 0.05)
    ax.plot_surface(
        leaf_x + leaf_sway,
        leaf_y,
        leaf_z,
        color="#2e8b57",
        alpha=0.9
    )
    ax.plot_surface(
        -leaf_x - leaf_sway,
        leaf_y,
        leaf_z - 0.6,
        color="#2e8b57",
        alpha=0.9
    )

    # 🌸 Floating petals
    for p in floating_petals:
        p[2] -= p[3]
        if p[2] < -5:
            p[2] = np.random.uniform(1, 3)
        ax.scatter(p[0], p[1], p[2], color="deeppink", s=28)

    # 💖 Text
    ax.text(
        0, 0, -5.1,
        f"Happy Rose Day\n{HER_NAME}",
        color="white",
        ha="center",
        fontsize=14
    )

    # 🎥 Camera
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_zlim(-5.5, 1.6)
    ax.view_init(elev=26, azim=frame)

# ---------- CREATE ANIMATION ----------
ani = FuncAnimation(fig, animate, frames=200, interval=50)

# ---------- EXPORT GIF ----------
ani.save(
    "realistic_rose_for_her.gif",
    writer=PillowWriter(fps=20)
)

plt.close()
