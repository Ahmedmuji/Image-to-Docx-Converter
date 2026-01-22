import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrow, Circle
from matplotlib.lines import Line2D

# Create a figure with 3 rows and 2 columns for all 6 diagrams
fig, axs = plt.subplots(3, 2, figsize=(16, 18))
axs = axs.flatten() # Flatten the 2D array of axes for easier indexing

# Diagram 1: Adsorption Illustration
ax1 = axs[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

# Left Adsorbent
rect1 = Rectangle((1, 4), 3, 2, linewidth=1, edgecolor='red', facecolor='none')
ax1.add_patch(rect1)
ax1.text(2.5, 4.5, 'surface\n(adsorbent)', ha='center', va='center')
ax1.plot([1, 4], [6, 6], 'k--') # Top dashed line
ax1.text(2.5, 6.5, 'Gas (adsorbate)', ha='center', va='center')

# Adsorbate particles coming towards surface
for i in range(5):
    ax1.add_patch(Circle((0.5 + i * 0.5, 7.5 + i * 0.2), 0.1, color='gray'))

# Arrow indicating movement
arrow1 = FancyArrow(4.2, 5, 1, 0, width=0.1, head_width=0.4, head_length=0.4, fc='red', ec='red')
ax1.add_patch(arrow1)

# Right Adsorbent with adsorbed particles
rect2 = Rectangle((6, 4), 3, 2, linewidth=1, edgecolor='red', facecolor='none')
ax1.add_patch(rect2)
ax1.plot([6, 9], [6, 6], 'k--') # Top dashed line

# Adsorbed particles on the surface
for i in range(10):
    ax1.add_patch(Circle((6.2 + i * 0.28, 6), 0.1, color='gray'))

# Diagram 2: Physisorption (N/M vs P, multiple T)
ax2 = axs[1]
P = np.linspace(0, 10, 100)
T1_val = 150 # Highest temperature
T2_val = 100 # Middle temperature
T3_val = 50  # Lowest temperature

# Physisorption curves (decreasing with T)
# Using a Langmuir-like model for illustration: x/m = aP / (1 + bP), where 'a' and 'b' are temp dependent
# To show decrease with T, let's make 'a' decrease and 'b' increase with T.
# Simplified for visualization: N/M = k * P / (1 + c * P)
k_T1, c_T1 = 0.5, 0.1
k_T2, c_T2 = 0.8, 0.08
k_T3, c_T3 = 1.2, 0.05

ax2.plot(P, k_T1 * P / (1 + c_T1 * P), color='red', label='T1')
ax2.plot(P, k_T2 * P / (1 + c_T2 * P), color='darkred', label='T2')
ax2.plot(P, k_T3 * P / (1 + c_T3 * P), color='salmon', label='T3')

ax2.set_xlabel('P')
ax2.set_ylabel('N/M')
ax2.set_title('Physisorption')
ax2.text(8, 0.8, 'T$_2$ < T$_1$', fontsize=10, ha='right')
ax2.text(8, 0.5, 'T$_1$', color='red')
ax2.text(8, 0.7, 'T$_2$', color='darkred')
ax2.text(8, 1.1, 'T$_3$', color='salmon')
ax2.set_ylim(0, 1.5)
ax2.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False) # Hide ticks for aesthetic

# Diagram 3: Chemisorption (N/M vs P, multiple T)
ax3 = axs[2]
# Chemisorption curves, showing decrease with T, but with a different shape
# Maybe a slight initial increase then plateau/decrease.
# For simplicity, I'll use a modified Langmuir-like function that allows for a hump if parameters are right,
# but here, primarily show the T dependence as depicted.
ax3.plot(P, 0.7 * P / (1 + 0.5 * P + 0.05 * P**2), color='red', label='T1') # T1 (higher T, lower adsorption)
ax3.plot(P, 1.0 * P / (1 + 0.3 * P + 0.03 * P**2), color='darkred', label='T2') # T2
ax3.plot(P, 1.3 * P / (1 + 0.2 * P + 0.02 * P**2), color='salmon', label='T3') # T3 (lower T, higher adsorption)

ax3.set_xlabel('P')
ax3.set_ylabel('N/M')
ax3.set_title('Chemisorption')
ax3.text(8, 0.5, 'T$_2$ > T$_1$', fontsize=10, ha='right')
ax3.text(8, 0.3, 'T$_1$', color='red')
ax3.text(8, 0.6, 'T$_2$', color='darkred')
ax3.text(8, 1.0, 'T$_3$', color='salmon')
ax3.set_ylim(0, 1.5)
ax3.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False) # Hide ticks for aesthetic

ax2.annotate('', xy=(3.5, 1.3), xytext=(3.5, 1.0),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))
ax2.text(3.7, 1.15, r'$\frac{N}{M}$', ha='left', va='center')
ax2.text(3.7, 0.8, '↓', ha='left', va='center', fontsize=12) # Manual arrow for T

ax3.annotate('', xy=(3.5, 1.3), xytext=(3.5, 1.0),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))
ax3.text(3.7, 1.15, r'$\frac{N}{M}$', ha='left', va='center')
ax3.text(3.7, 0.8, '↓', ha='left', va='center', fontsize=12) # Manual arrow for T

# Diagram 4: Freundlich Isotherm (x/m vs P)
ax4 = axs[3]
P_freundlich = np.linspace(0.1, 10, 100)
K = 2
n = 3 # 1/n = 1/3
xm_freundlich = K * P_freundlich**(1/n)

ax4.plot(P_freundlich, xm_freundlich, color='red')
ax4.set_xlabel('P →')
ax4.set_ylabel(r'$\frac{x}{m}$', rotation=0, ha='right')
ax4.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False) # Hide ticks for aesthetic
ax4.set_ylim(0, 5)

ax4.text(1, 0.5, r'$\frac{1}{n}=1 \Rightarrow \frac{x}{m}=kP$', ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax4.text(2, 2.5, r'$\frac{x}{m}=kP^{1/n}$ (n=1 to $\infty$)', ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# Illustrate n=0 for high pressure, but keep the curve.
ax4.axvline(x=5, color='gray', linestyle='--')
ax4.plot(P_freundlich[P_freundlich > 5], [K * 5**(1/n)] * len(P_freundlich[P_freundlich > 5]), 'r--')
ax4.text(5.2, 4.5, r'n=0 $\Rightarrow \frac{x}{m}=k$', ha='left', va='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

arrow_n0 = FancyArrow(3.5, 4.0, 0.2, 0.5, width=0.05, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax4.add_patch(arrow_n0)

# Diagram 5: Freundlich Isotherm (log(x/m) vs log(P))
ax5 = axs[4]
logP_freundlich = np.linspace(0.1, 2, 100) # log(P) from ~1.2 to 100
log_K = np.log10(K)
slope_val = 1/n
log_xm_freundlich = log_K + slope_val * logP_freundlich

ax5.plot(logP_freundlich, log_xm_freundlich, color='red')
ax5.set_xlabel('logP →')
ax5.set_ylabel(r'log$\frac{x}{m}$', rotation=0, ha='right')
ax5.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False) # Hide ticks for aesthetic
ax5.set_ylim(-0.5, 1.5)

# Y-intercept for log K
ax5.plot([0, 0], [-0.5, log_K], 'k--')
ax5.plot([0, logP_freundlich[0]], [log_K, log_K], 'k--')
ax5.text(-0.2, log_K, r'log$\frac{x}{m}$', ha='right', va='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# Slope annotation
slope_x = [0.8, 1.8]
slope_y = [log_K + slope_val * 0.8, log_K + slope_val * 1.8]
ax5.plot(slope_x, slope_y, 'k-') # part of the line
ax5.plot([slope_x[0], slope_x[1]], [slope_y[0], slope_y[0]], 'k--') # horizontal guide
ax5.plot([slope_x[1], slope_x[1]], [slope_y[0], slope_y[1]], 'k--') # vertical guide
ax5.text(1.3, log_K + slope_val * 1.3 - 0.2, r'slope=$\frac{1}{n}$', ha='center', va='top')
ax5.set_aspect('equal', adjustable='box')


# Diagram 6: Langmuir Isotherm (x/m vs P)
ax6 = axs[5]
P_langmuir = np.linspace(0, 10, 100)
a_param = 1.5
b_param = 0.5
xm_langmuir = (a_param * P_langmuir) / (1 + b_param * P_langmuir)

ax6.plot(P_langmuir, xm_langmuir, color='red')
ax6.set_xlabel('P')
ax6.set_ylabel(r'$\frac{x}{m}$', rotation=0, ha='right')
ax6.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False) # Hide ticks for aesthetic
ax6.set_ylim(0, 3.5)

# Annotations for low and high pressure regions
ax6.text(2, 0.5, r'$\frac{x}{m}=aP$ (low pressure)', ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax6.text(7, 2.8, r'$\frac{x}{m}=\frac{a}{b}$ (high pressure)', ha='center', va='bottom', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax6.text(3, 1.5, 'moderate\npressure', ha='right', va='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

arrow_high_pressure = FancyArrow(6, 2.5, 0, -0.5, width=0.05, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax6.add_patch(arrow_high_pressure)


plt.tight_layout()
plt.savefig('e:/PPIT/diagram_code/diag_img_tmp591506vbjpeg_1.png')
plt.close(fig)