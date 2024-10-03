import matplotlib.pyplot as plt

heights = [150, 160, 165, 170, 175, 180, 155, 165, 170, 175, 180, 190, 160, 165, 170, 175]

plt.hist(heights, bins=5, edgecolor='black')
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.show()
