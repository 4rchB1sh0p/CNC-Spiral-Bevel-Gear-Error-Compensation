import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Drawing the rectangular solid representing the working volume
rect = patches.Rectangle((0.2, 0.2), 0.6, 0.6, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Body diagonals
body_diagonals = [((0.2, 0.2), (0.8, 0.8)), ((0.2, 0.8), (0.8, 0.2))]
for diag in body_diagonals:
    ax.plot([diag[0][0], diag[1][0]], [diag[0][1], diag[1][1]], linestyle='--', color='black')

# Labels for body diagonals
ax.text(0.5, 0.5, 'ag (ppp/nnn)', horizontalalignment='center', verticalalignment='center')

# Axes
ax.annotate('', xy=(1, 0.2), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.annotate('', xy=(0.2, 1), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.text(1, 0.2, 'X', horizontalalignment='center', verticalalignment='center')
ax.text(0.2, 1, 'Y', horizontalalignment='center', verticalalignment='center')

ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.axis('off')

plt.savefig('/conventional_body_diagonal.png')
plt.show()
fig, ax = plt.subplots()

# Drawing the rectangular solid representing the working volume
rect = patches.Rectangle((0.2, 0.2), 0.6, 0.6, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Laser vector measurement path
path = [(0.2, 0.2), (0.4, 0.2), (0.4, 0.4), (0.6, 0.4), (0.6, 0.6), (0.8, 0.6), (0.8, 0.8)]
for i in range(len(path) - 1):
    ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], color='black')

# Labels for measurement path
ax.text(0.2, 0.15, 'a', horizontalalignment='center', verticalalignment='center')
ax.text(0.8, 0.85, 'g', horizontalalignment='center', verticalalignment='center')

# Axes
ax.annotate('', xy=(1, 0.2), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.annotate('', xy=(0.2, 1), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.text(1, 0.2, 'X', horizontalalignment='center', verticalalignment='center')
ax.text(0.2, 1, 'Y', horizontalalignment='center', verticalalignment='center')

ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.axis('off')

plt.savefig('/laser_vector_measurement_path.png')
plt.show()
# Conventional Body Diagonal Method Diagram
fig, ax = plt.subplots()

# Drawing the rectangular solid representing the working volume
rect = patches.Rectangle((0.2, 0.2), 0.6, 0.6, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Body diagonals
body_diagonals = [((0.2, 0.2), (0.8, 0.8)), ((0.2, 0.8), (0.8, 0.2))]
for diag in body_diagonals:
    ax.plot([diag[0][0], diag[1][0]], [diag[0][1], diag[1][1]], linestyle='--', color='black')

# Labels for body diagonals
ax.text(0.5, 0.5, 'ag (ppp/nnn)', horizontalalignment='center', verticalalignment='center')

# Axes
ax.annotate('', xy=(1, 0.2), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.annotate('', xy=(0.2, 1), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.text(1, 0.2, 'X', horizontalalignment='center', verticalalignment='center')
ax.text(0.2, 1, 'Y', horizontalalignment='center', verticalalignment='center')

ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.axis('off')

plt.savefig('/conventional_body_diagonal.png')
plt.show()

# Laser Vector Measurement Method Diagram
fig, ax = plt.subplots()

# Drawing the rectangular solid representing the working volume
rect = patches.Rectangle((0.2, 0.2), 0.6, 0.6, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Laser vector measurement path
path = [(0.2, 0.2), (0.4, 0.2), (0.4, 0.4), (0.6, 0.4), (0.6, 0.6), (0.8, 0.6), (0.8, 0.8)]
for i in range(len(path) - 1):
    ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], color='black')

# Labels for measurement path
ax.text(0.2, 0.15, 'a', horizontalalignment='center', verticalalignment='center')
ax.text(0.8, 0.85, 'g', horizontalalignment='center', verticalalignment='center')

# Axes
ax.annotate('', xy=(1, 0.2), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.annotate('', xy=(0.2, 1), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", lw=1, color='black'))
ax.text(1, 0.2, 'X', horizontalalignment='center', verticalalignment='center')
ax.text(0.2, 1, 'Y', horizontalalignment='center', verticalalignment='center')

ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.axis('off')

plt.savefig('/laser_vector_measurement_path.png')
plt.show()
