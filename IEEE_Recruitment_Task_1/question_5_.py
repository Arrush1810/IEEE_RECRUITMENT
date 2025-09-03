import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers from normal distribution
data = np.random.randn(1000)

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(range(len(data)), data, alpha=0.5, color="blue")
plt.title("Scatter Plot of Normal Distribution")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
