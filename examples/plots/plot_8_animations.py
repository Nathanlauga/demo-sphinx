"""
Matplotlib
==========

Show a Matplotlib bar plot.

"""


######################################################################
# Import custom package
# 

from my_little_poney.datasets import load_iris_as_df

iris = load_iris_as_df()

print(iris.shape)


######################################################################
# Test matplotlib
# 

import numpy as np
import matplotlib.pyplot as plt

# Make a random dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()