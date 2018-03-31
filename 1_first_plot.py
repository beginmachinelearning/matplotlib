import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.array([2, 4, 5, 7, 10])

y = np.array([1, 3, 5, 6, 8])
# Plot the data
#g for green, o for marker, - for line
plt.plot(x, y, 'go-', label='Line Graph')

# Add a legend
plt.legend()

# Show the plot
plt.show()


