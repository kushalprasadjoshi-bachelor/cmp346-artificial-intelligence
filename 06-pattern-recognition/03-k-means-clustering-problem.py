"""
Question:
Solve the problem using K-Means Clustering method and analyze the results.

Given:
- Generate two sets of random data:
  x in the range [25, 100]
  y in the range [175, 255]
- Combine them into a single dataset
- Plot the histogram
- Apply K-Means clustering
- Analyze the clustering result
"""

# ------- IMPORT REQUIRED LIBRARIES --------
import numpy as np
import cv2
from matplotlib import pyplot as plt

# ---------- DATA GENERATION ----------
# Generate 25 random values between 25 and 100
x = np.random.randint(25, 100, 25)

# Generate 25 random values between 175 and 255
y = np.random.randint(175, 255, 25)

# Combine both arrays into a single array
z = np.hstack((x, y))

# Reshape data into a column vector (required by OpenCV K-Means)
z = z.reshape((50, 1))

# Convert data type to float32 (required by OpenCV)
z = np.float32(z)

# ----- HISTOGRAM OF ORIGINAL DATA ------
plt.hist(z, 256, [0, 256])
plt.title("Histogram of Original Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ------- APPLY K-MEANS CLUSTERING ------
# Define stopping criteria:
# Stop after 10 iterations or when accuracy reaches epsilon = 1.0
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
            10, 1.0)

# Number of clusters (since data has two distinct groups)
K = 2

# Apply K-Means clustering
ret, label, center = cv2.kmeans(
    z,                      # input data
    K,                      # number of clusters
    None,                   # initial labels
    criteria,               # termination criteria
    10,                     # number of attempts
    cv2.KMEANS_RANDOM_CENTERS
)

# ------ DISPLAY CLUSTER CENTERS -------
print("Cluster Centers:")
print(center)

# ------- SEPARATE DATA BASED ON CLUSTERS ------
cluster1 = z[label.ravel() == 0]
cluster2 = z[label.ravel() == 1]

# ------- PLOT CLUSTERED DATA --------
plt.hist(cluster1, 256, [0, 256], alpha=0.6, label="Cluster 1")
plt.hist(cluster2, 256, [0, 256], alpha=0.6, label="Cluster 2")

# Plot cluster centers as vertical lines
plt.axvline(center[0], color='black', linestyle='--', label='Center 1')
plt.axvline(center[1], color='red', linestyle='--', label='Center 2')

plt.title("K-Means Clustering Result (K = 2)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# ------ RESULT ANALYSIS -------
"""
Analysis:
- The histogram of the original data shows two distinct peaks.
- K-Means with K = 2 successfully separates the data into two clusters.
- One cluster corresponds to low-range values (25-100).
- The other cluster corresponds to high-range values (175-255).
- Cluster centers represent the mean value of each group.
- Since the data is well separated, K-Means converges quickly and accurately.
"""

print("K-Means clustering successfully divided the data into two distinct clusters.")
