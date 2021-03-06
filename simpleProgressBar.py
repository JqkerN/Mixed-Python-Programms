import numpy as np


class progressBar():
    def __init__(self,  iterations, update_rate=0):
        self.iterations = iterations        # Maximum number of iterations
        self.update_rate = update_rate      # Update rate, numbers before update. 
        self.rate = 0                       # Internal rate controller. 

    def Progress(self, time_step):
        # Give the progress when get a time_step between [0,iterations], both in % and as a visual bar. 
        if int(100*time_step/self.iterations) == 100:
            PB= int(100*time_step/self.iterations)*'#' + int(100-100*time_step/self.iterations)*'-'
            procents = "    {0:.2f}%".format(100*time_step/self.iterations)
            print( PB + procents, end='\n', flush = True)

        elif self.rate < self.update_rate: self.rate +=1
        else:
            PB= int(100*time_step/self.iterations)*'#' + int(100-100*time_step/self.iterations)*'-'
            procents = "    {0:.2f}%".format(100*time_step/self.iterations)
            print( PB + procents, end='\r', flush = True)
            self.rate = 0


def main():
    # SHOWCASE FOR CLASS VERSION OF PROGRESS BAR:
    print("CLASS - SIMPLE PROGRESS BAR: ")
    MIN = 0
    MAX = 99000
    list = np.linspace(MIN,MAX,100000)

    prog_Bar = progressBar(MAX,5)
    for elm in list:
        prog_Bar.Progress(elm)


    # SHOWCASE FOR SIMPLE PROGRESS BAR:
    print("SIMPLE PROGRESS BAR: ")
    MIN = 0
    MAX = 99000
    list = np.linspace(MIN,MAX,100000)

    for elm in list:
        PB = int(100*elm/MAX)*'#' + int(100-100*elm/MAX)*'-'
        procents = "    {0:.2f}%".format(100*elm/MAX)
        print( PB + procents, end='\r', flush = True)


if __name__ == "__main__":
    main()