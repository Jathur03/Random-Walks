import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Make a random walk, and plot the points
rw = RandomWalk()
rw.fill_walk()

# Plot the points in teh walk
plt.style.use('seaborn')
fig, ax = plt.subplots()
point_numbers = list(range(rw.num_points))
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

# Emphasize the first and last points
# ax.scatter(0, 0, c='green', edgecolors='none', s=100)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

plt.show()