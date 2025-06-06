import numpy as np
import matplotlib.pyplot as plt

overs=np.arange(1,11)
score = [3,6,7,10,15,19,5,9,1,16]

plt.bar(overs,score)
plt.title("INDIA 'S SCORE OVER BY OVER")
plt.xlabel("OVER NUMBER")
plt.ylabel("RUNS SCORED")
plt.xticks(overs)
plt.grid(axis='y',alpha=0.7)
plt.show()
