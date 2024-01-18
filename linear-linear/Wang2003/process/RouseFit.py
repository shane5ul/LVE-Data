import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import glob, os


def plotGst():
	""" Just plot the data of a high MW, relatively monodisperse polymer, and fit the Rouse mode"""
	
	wp,  Gp  = np.loadtxt('Gp410full.dat', unpack=True)
	wpp, Gpp = np.loadtxt('Gpp410full.dat', unpack=True)

	
	plt.plot(wp, Gp, 'o')
	plt.plot(wpp, Gpp, 'o')

	plt.xscale('log')
	plt.yscale('log')

	wR = np.logspace(4,10)
	GR = lambda wR: 10.03 * wR**(0.71)

	plt.text(1e1, 5e6, r'$G^{*}_{R} = 10.03\, \omega^{0.71}$', fontsize=20)
	plt.plot(wR, GR(wR), lw=2)

	plt.xlim(0.9e-2, 1.1e10)
	plt.show()


def plotGstSansRouse():
	"""Subtract Rouse mode from G*"""
	wp,  Gp  = np.loadtxt('Gp410full.dat', unpack=True)
	wpp, Gpp = np.loadtxt('Gpp410full.dat', unpack=True)

		
	plt.plot(wp, Gp, 's')
	plt.plot(wpp, Gpp, 'o')

	plt.xscale('log')
	plt.yscale('log')

	wR = np.logspace(4,10)
	GR = lambda wR: 10.03 * wR**(0.71)

	plt.plot(wR, GR(wR), lw=2)

	cond = wpp < 0.5e5
	plt.plot(wpp[cond], Gpp[cond] - GR(wpp[cond]),'--')

	cond = wp < 0.5e5
	plt.plot(wp[cond], Gp[cond] - GR(wp[cond]),'--')

	plt.ylim(0.01, 2.e6)

	plt.xlim(0.9e-2, 1.1e10)
	plt.show()


plotGstSansRouse()

#
# if "clean subdirectory doesn't exist
#
if False:

	#subdir="410-100/"
	subdir="410-44/"
	os.chdir(subdir)

			
	if not os.path.exists('proc'):
		os.makedirs('proc')

	for file_clean in glob.glob("Gp*.dat"):

		file_proc = 'proc/' + file_clean
		print("{0:20} {1:20}".format(file_clean, file_proc))
		wo, Go = np.loadtxt(file_clean, unpack=True)

		# Rouse mode
		GR = lambda w: 10.03 * w**(0.71)

		cond = wo < 0.5e5
		wn   = wo[cond]
		Gn   = Go[cond] - GR(wn)

		# save the file
		np.savetxt(file_proc, np.c_[wn,Gn], fmt='%3.4e')	
