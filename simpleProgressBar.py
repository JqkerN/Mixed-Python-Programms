import time
import numpy as np


MIN = 0
MAX = 99
list = np.linspace(MIN,MAX,100)

for elm in list:
    progressBar = int(elm)*'#' + int(99-elm)*'-'
    procents = " {0:.2f}%".format(100*elm/MAX)
    print( progressBar + procents, end='\r', flush = True)
    time.sleep(0.1)