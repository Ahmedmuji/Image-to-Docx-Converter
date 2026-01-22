import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 2))

# Adsorbent surface (bottom rectangle)
ax.add_patch(plt.Rectangle((0.1, 0.1), 0.3, 0.7, edgecolor='black', facecolor='white', linewidth=1.5))
ax.text(0.25, 0.45, 'surface\n(adsorbent)', ha='center', va='center', fontsize=10)

# Gas molecules (top rectangle)
ax.add_patch(plt.Rectangle((0.1, 1.0), 0.3, 0.3, edgecolor='black', facecolor='white', linewidth=1.5))
ax.text(0.25, 1.15, 'Gas (adsorbate)', ha='center', va='center', fontsize=10)

# Arrows from gas to surface
ax.annotate("", xy=(0.25, 0.95), xytext=(0.25, 0.7),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0", lw=1.5))

# Second stage: Gas molecules moving towards surface
ax.add_patch(plt.Rectangle((0.45, 0.1), 0.3, 0.7, edgecolor='black', facecolor='white', linewidth=1.5))
ax.text(0.6, 0.45, 'surface\n(adsorbent)', ha='center', va='center', fontsize=10)

# Random dots above the surface (gas molecules approaching)
np.random.seed(42)
num_dots = 20
x_dots = np.random.uniform(0.48, 0.72, num_dots)
y_dots = np.random.uniform(0.85, 1.2, num_dots)
ax.scatter(x_dots, y_dots, color='black', s=10, zorder=5)

# Arrows indicating movement to the right
ax.annotate("", xy=(0.4, 0.45), xytext=(0.45, 0.45),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0", lw=1.5))

# Third stage: Adsorbed molecules (right rectangle)
ax.add_patch(plt.Rectangle((0.8, 0.1), 0.3, 0.7, edgecolor='black', facecolor='white', linewidth=1.5))
ax.text(0.95, 0.45, 'surface\n(adsorbent)', ha='center', va='center', fontsize=10)

# Adsorbed molecules on the surface
x_adsorbed = np.linspace(0.81, 1.09, 15)
y_adsorbed = np.full_like(x_adsorbed, 0.78)
ax.scatter(x_adsorbed, y_adsorbed, color='black', s=20, zorder=5)

# Arrows indicating movement to the right
ax.annotate("", xy=(0.75, 0.45), xytext=(0.8, 0.45),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0", lw=1.5))


ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.3)
ax.axis('off')

plt.savefig('e:/PPIT/diagram_code/diag_img_tmpez04jb9rjpeg_1.png', bbox_inches='tight', dpi=300)
plt.close()