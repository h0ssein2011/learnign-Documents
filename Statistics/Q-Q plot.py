
import numpy as np 
import matplotlib.pyplot as plt

n=50 #number of samples

sample_dataset=sorted(list(np.random.randint(0,100,n)))
normal_dist =sorted(list(np.random.normal(size=n)))
uniform_dist =sorted(list(np.random.uniform(size= n)))

#get i th qunatiles from each dists
quantiles_sample = [sample_dataset[int(i*n/15)] for i in range(15) ]
quantiles_normal = [normal_dist[int(i*n/15)] for i in range(15) ]
quantiles_uniform = [uniform_dist[int(i*n/15)] for i in range(15) ]


fig ,axs = plt.subplots(2,1,figsize=(16,8))
axs[0].scatter(quantiles_normal,quantiles_sample)
axs[0].set_title('q-q plot normal')

axs[1].set_title('q-q plot uniform')
axs[1].scatter(quantiles_uniform,quantiles_sample)

fig.tight_layout()
plt.show()

# this seems be a uniform distribution that is clear 