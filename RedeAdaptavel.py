import numpy as np
import math


class RedeNeural():

    def __init__(self, gen, number, pesos = 0):
        self.gen = gen
        self.name = str(gen) + '-' + str(number)
        self.pesos = pesos
        
        
    def genesis(self, amostra, camadas = 3):
    

        
        #Lista principal, contendo o conjunto de listas de cada camada 
        layer = []
        
        for i in range(camadas):
            #Lista intermediária, contendo as listas de pesos específicos para cada variável 
            
            c = []
            for i in range(len(amostra)):
                
                #Criação de uma lista específica de pesos para cada variável presente na amostra 
                pesos = np.random.randn(len(amostra))
                
                c.append(pesos)
                
            layer.append(c)
            
        self.pesos = layer


    def pensar(self, entrada):
        
        camadaatual = []    
        for i in range(len(self.pesos)):
            camadatemporaria = []
            
            for j in range(len(entrada)):
            
                camadatemporaria.append(sum([entrada[j] * x for x in self.pesos[i][j]]))
                
            camadaatual = camadatemporaria
            
        self.saida = sum(camadaatual)        
        return sum(camadaatual)


    def sigmoid(self, step_value = False):
    
        sigm = 1 / ( 1 + np.exp(-self.saida))
        
        
        if step_value == True:
        
            if sigm >= 0.5:
                return 1
                
            else:
                return 0
                
        else:
            return sigm
                        
    
    def tanh(self):
        
        tanh = math.tanh(self.saida)
        
        return tanh
    
