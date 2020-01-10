
# want to show the central limit theorem in practice here
from random import choices

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

unif_dist = np.random.uniform(0,100,1000)

means_unif_dist = [np.mean(sample) for sample in choices(unif_dist,k=100)]
# print(means_unif_dist)
fig ,axs = plt.subplots(2,1)
axs[0].hist(unif_dist,bins=100)
axs[1].hist(means_unif_dist,bins=100)

plt.show()

# print(len(unif_dist))