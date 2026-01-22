import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5), sharey=True)

# Common y-axis label
fig.text(0.04, 0.5, r'$N/M$', va='center', ha='center', rotation='vertical', fontsize=12)

# Common x-axis label
fig.text(0.5, 0.0, r'$P \longrightarrow$', ha='center', fontsize=12)

# Physisorption Plot (Left)
ax1.set_title('Physisorption ' + r'$\propto \frac{1}{temp}$', fontsize=12)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1.2)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.spines['left'].set_position(('data', 0))
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.arrow(0, 1.1, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black')
ax1.arrow(9, 0, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black')

P_vals = np.linspace(0.1, 10, 100)
# T1 (lowest adsorption at higher P)
curve1 = 1 - np.exp(-0.2 * P_vals) * 0.9
ax1.plot(P_vals, curve1 * 0.7, color='red', linewidth=1.5)
ax1.text(7.5, curve1[-1]*0.7 + 0.05, r'$T_1$', color='red', fontsize=10)

# T2 (medium adsorption)
curve2 = 1 - np.exp(-0.2 * P_vals) * 0.9
ax1.plot(P_vals, curve2 * 0.9, color='red', linewidth=1.5)
ax1.text(7.5, curve2[-1]*0.9 + 0.05, r'$T_2$', color='red', fontsize=10)

# T3 (highest adsorption)
curve3 = 1 - np.exp(-0.2 * P_vals) * 0.9
ax1.plot(P_vals, curve3 * 1.1, color='red', linewidth=1.5)
ax1.text(7.5, curve3[-1]*1.1 + 0.05, r'$T_3$', color='red', fontsize=10)

ax1.text(6, 0.2, r'$T_2 < T_1$', fontsize=10)
ax1.text(7.7, 0.1, r'$T_3$', fontsize=10, alpha=0) # Placeholder for T3 label placement relative to T1/T2

# Chemisorption Plot (Right)
ax2.set_title('Chemisorption ' + r'$\propto temp$', fontsize=12)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 1.2)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.spines['left'].set_position(('data', 0))
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.arrow(0, 1.1, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black')
ax2.arrow(9, 0, 0, 0, head_width=0.2, head_length=0.1, fc='black', ec='black')

P_vals_chem = np.linspace(0.1, 10, 100)
# T1 (lowest peak)
curve_chem1 = P_vals_chem * np.exp(-0.1 * P_vals_chem) * 1.5
ax2.plot(P_vals_chem, curve_chem1 * 0.7, color='red', linewidth=1.5)
ax2.text(7.5, curve_chem1[-1]*0.7 + 0.05, r'$T_1$', color='red', fontsize=10)

# T2 (medium peak)
curve_chem2 = P_vals_chem * np.exp(-0.1 * P_vals_chem) * 1.5
ax2.plot(P_vals_chem, curve_chem2 * 0.9, color='red', linewidth=1.5)
ax2.text(7.5, curve_chem2[-1]*0.9 + 0.05, r'$T_2$', color='red', fontsize=10)

# T3 (highest peak)
curve_chem3 = P_vals_chem * np.exp(-0.1 * P_vals_chem) * 1.5
ax2.plot(P_vals_chem, curve_chem3 * 1.1, color='red', linewidth=1.5)
ax2.text(7.5, curve_chem3[-1]*1.1 + 0.05, r'$T_3$', color='red', fontsize=10)

ax2.text(6, 0.2, r'$T_2 > T_1$', fontsize=10)
ax2.text(7.7, 0.1, r'$T_3$', fontsize=10, alpha=0) # Placeholder for T3 label placement relative to T1/T2

fig.tight_layout(rect=[0.05, 0.05, 1, 1])
plt.savefig('e:/PPIT/diagram_code/diag_img_tmpez04jb9rjpeg_3.png', bbox_inches='tight', dpi=300)
plt.close()