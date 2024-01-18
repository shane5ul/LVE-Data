#
# 1. store raw files in directory "raw" with Gp*.csv or Gpp*.csv format
# 2. turn on dynescm2 log10ax based on data
# 3. Outputs transformed files in the "clean" bin
#
import numpy as np
import matplotlib.pyplot as plt
import glob, os

dynescm2 = False
log10ax  = False

#
# if "clean subdirectory doesn't exist
#	
if not os.path.exists("clean"):
    os.makedirs("clean")

# some IO to help user    
print("-----------------------------------------------------------")
print("oldFile              newFile                 log10   dyncm2")
print("-----------------------------------------------------------")

for file_raw in glob.glob("raw/Gp*.dat"):
	file_clean = file_raw.replace('csv','dat')
	file_clean = file_clean.replace('raw/','clean/')
	print("{0:20} {1:20} {2:8} {3:8}".format(file_raw, file_clean, log10ax, dynescm2))
	wo, Go = np.loadtxt(file_raw, unpack=True)
	
	# Transformation
	if log10ax:
		wn = 10.**wo
		Gn = 10.**Go
	else:
		wn = wo
		Gn = Go
	
	if dynescm2:
		Gn = 0.1 * Gn
		
#	plt.loglog(wn, Gn, 'o')	

	# save the file
	np.savetxt(file_clean, np.c_[wn,Gn], fmt='%3.4e')
    
    
# plt.plot(wo, Go, 'o')
#plt.show()
	
