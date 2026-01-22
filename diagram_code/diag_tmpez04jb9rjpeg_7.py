import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4))

ax.set_xlim(0, 10)
ax.set_ylim(0, 1.2)
ax.set_xticks([])
ax.set_yticks([])
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_xlabel(r'Pressure $\longrightarrow$', ha='right', x=1, fontsize=12)
ax.set_ylabel(r'$\frac{x}{m}$', ha='right', y=1, rotation='horizontal', fontsize=14)

ax.arrow(0, 1.1, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black') # Y-axis arrow
ax.arrow(9, 0, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black') # X-axis arrow

# Langmuir Isotherm curve: (x/m) = aP / (1 + bP)
P_vals_langmuir = np.linspace(0.1, 10, 100)
a = 0.5
b = 0.5
xm_langmuir = (a * P_vals_langmuir) / (1 + b * P_vals_langmuir)

ax.plot(P_vals_langmuir, xm_langmuir * 1.5, color='red', linewidth=1.5) # Scale for aesthetics

# Low pressure approximation: x/m = aP
ax.text(1, 0.1, r'$\frac{x}{m} = aP$ (low pressure)', fontsize=12)

# High pressure approximation: x/m = a/b
ax.text(6.5, 0.9, r'$\frac{x}{m} = \frac{a}{b}$', fontsize=12, ha='center')
ax.arrow(7, 0.9, 0, -0.1, head_width=0.1, head_length=0.05, fc='black', ec='black')

# Labels for pressure regions
ax.text(3, 0.7, 'moderate\npressure', fontsize=10, ha='center')
ax.text(7.5, 1.0, '(High pressure)', fontsize=10, ha='center')


plt.savefig('e:/PPIT/diagram_code/diag_img_tmpez04jb9rjpeg_7.png', bbox_inches='tight', dpi=300)
plt.close()