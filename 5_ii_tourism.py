import matplotlib.pyplot as plt

cities = ['London', 'New York', 'Tokyo', 'Sydney', 'Cairo']
lats = [51.5074, 40.7128, 35.6762, -33.8688, 30.0444]
longs = [-0.1278, -74.0060, 139.6503, 151.2093, 31.2357]

plt.scatter(longs, lats, color='red')

for i, city in enumerate(cities):
    plt.text(longs[i], lats[i], city)

plt.title('Major Cities Around the World')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
