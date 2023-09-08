import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

grades = [10, 30, 50, 70, 90]
means = [15, 35, 55, 75, 95]

std = np.random.randint(5, 15, size=len(grades)) 


for i in range(len(grades)):
  x = np.linspace(means[i]-5*std[i], means[i]+5*std[i], 100)
  y = norm.pdf(x, means[i], std[i])
  
  ax.plot(x, np.full(100, grades[i]), y)

ax.set_xlabel('Y - Test Score')
ax.set_ylabel('X - Grade')
ax.set_zlabel('Z - Probability Density')
ax.set_title('Maximum likelihood estimation')

red_dotted_line = means 
ax.plot(red_dotted_line, grades, zs=0, zdir='z', color='red', linestyle='dotted')

fig.tight_layout()
plt.show()
