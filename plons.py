import numpy as np
import matplotlib.pylab as plt

d = np.arange(0,5,1)
#for i in range(5):
for i in d:
	dat = np.loadtxt("dat{:d}.txt".format(i))
	x = dat[:,0]
	u = dat[:,1]
	plt.plot(x,u,label='tiempo{:d}'.format(i))
	plt.xlabel('X')
	plt.xlabel('Y')
	plt.title('Adveccion no lineal')
	plt.legend()


plt.savefig("Grafica.pdf")
