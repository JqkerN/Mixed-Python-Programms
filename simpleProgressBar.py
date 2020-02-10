import numpy as np


MIN = 0
MAX = 99000
list = np.linspace(MIN,MAX,100000)

for elm in list:
    progressBar = int(100*elm/MAX)*'#' + int(100-100*elm/MAX)*'-'
    procents = "    {0:.2f}%".format(100*elm/MAX)
    print( progressBar + procents, end='\r', flush = True)