import pandas as pd
import numpy as np



entrada = [1,2,3]


class RedeNeural():

    def __init__(self, gen, sample, pesos = 0, camadas = 3):
        self.gen = gen
        
        if pesos == 0:
            
            tp = []
            for i in range(camadas):
            
            
                cp = []
            
                for i in range(len(sample)):
                
                    cp.append(np.random.randn(len(sample)))
                
                    #print(cp[-1])
                
                tp.append(cp)

a = RedeNeural(0, entrada)