import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

# Common y-axis label
fig.text(0.04, 0.5, r'$\frac{x}{m}$', va='center', ha='center', rotation='vertical', fontsize=14)

# Freundlich Isotherm (x/m vs P)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1.2)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.spines['left'].set_position(('data', 0))
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.set_xlabel(r'$P \longrightarrow$', ha='right', x=1, fontsize=12)
ax1.arrow(0, 1.1, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black') # Y-axis arrow
ax1.arrow(9, 0, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black') # X-axis arrow


P_vals_freundlich = np.linspace(0.1, 10, 100)
# Simulate (x/m) = k * P^(1/n)
k_val = 0.5
n_val = 2 # Example value for n

xm_curve = k_val * (P_vals_freundlich**(1/n_val))
ax1.plot(P_vals_freundlich, xm_curve * 0.5, color='red', linewidth=1.5) # Scale down for aesthetics

ax1.text(1, 0.2, r'$\frac{x}{m} = kP^{1/n}$', fontsize=12) # General equation
ax1.text(1, 0.5, r'$n=0 \Rightarrow \frac{x}{m} = k$', fontsize=12, va='bottom')
ax1.text(2, 0.05, r'$n=1 \Rightarrow \frac{x}{m} = kP$', fontsize=12)
ax1.text(3, 0.35, r'$(n=100)$', fontsize=10) # Annotation for the curve

# Logarithmic Freundlich Isotherm (log(x/m) vs log P)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 1.2)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.spines['left'].set_position(('data', 0))
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.set_xlabel(r'$\log P \longrightarrow$', ha='right', x=1, fontsize=12)
ax2.set_ylabel(r'$\log \frac{x}{m}$', ha='right', y=1, rotation='horizontal', fontsize=12)
ax2.arrow(0, 1.1, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black') # Y-axis arrow
ax2.arrow(9, 0, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black') # X-axis arrow

# Simulate log(x/m) = log k + (1/n) log P (straight line)
log_P_vals = np.linspace(1, 9, 100) # Start from 1 to avoid log(0)
log_k = 0.2
slope_val = 0.2 # Represents 1/n
log_xm_line = log_k + slope_val * log_P_vals
ax2.plot(log_P_vals, log_xm_line * 0.1 + 0.2, color='red', linewidth=1.5) # Scale and shift for aesthetics

ax2.text(7, 0.3, r'slope = $\frac{1}{n}$', fontsize=12)

fig.tight_layout(rect=[0.05, 0.05, 1, 1])
plt.savefig('e:/PPIT/diagram_code/diag_img_tmpez04jb9rjpeg_5.png', bbox_inches='tight', dpi=300)
plt.close()