import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.array([2, 4, 5, 7, 10])

y = np.array([1, 3, 5, 6, 8])
# Plot the data
fig = plt.figure(figsize=(6,6)) 
#g for green, o for marker, - for line
plt.plot(x, y, 'go-')
plt.title('My First Graph')
plt.xlabel("X values")
plt.ylabel("Y values")
# Add a legend
plt.legend(['Line Graph'])

# Show the plot
plt.show()






