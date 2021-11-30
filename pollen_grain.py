import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk using the random walk class
rw = RandomWalk()
rw.fill_walk()

# plotting the points
plt.style.use('seaborn')
fg, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth = 2)

# Set chart title and label axes
ax.set_title('Random Walk' , fontsize = 24)

# Set size of tick lablels
ax.tick_params(axis='both', labelsize = 14)

plt.show()
