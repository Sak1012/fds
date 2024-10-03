import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)
temps = [5, 7, 10, 15, 20, 25, 30, 28, 22, 15, 10, 5]

plt.scatter(months, temps, c=temps, cmap='coolwarm', s=100)
plt.colorbar(label="Temperature (°C)")
plt.title("Average Monthly Temperatures")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()
