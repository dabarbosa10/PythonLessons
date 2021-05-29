import numpy as np
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,4,figsize=(14,4))
X=np.array(range(40))

for fig, b, w in zip([0, 1, 2, 3],[20, 15, 10, 5], [0.2, 0.4, 0.6, 0.8]):
    y=b+w*X
    axs[fig].plot(X,y, 'b-', label='b='+format(b)+'; w='+format(w))
    axs[fig].set_ylim(bottom=0,top=50), axs[fig].legend();
    axs[fig].legend(prop={'size':14}); axs[fig].grid();

plt.savefig('plot.pdf')