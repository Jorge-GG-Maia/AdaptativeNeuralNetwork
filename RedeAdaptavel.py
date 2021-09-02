import numpy as np
import math
import random


class RedeNeural():

    def __init__(self, gen, number, pesos = 0):
        self.gen = gen
        self.name = str(gen) + '-' + str(number)
        self.pesos = pesos
        self.score = 0
        
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
        
        camadaatual = entrada
        
        for i in range(len(self.pesos)):
            
            novacamada = []
            for j in range(len(self.pesos[i])):
            
            
                new_value = sum([x * y for x,y in zip(camadaatual, self.pesos[i][j])])
                novacamada.append(new_value)
                
                
            camadaatual = novacamada
        
        self.saida = sum(camadaatual)
        
        
    def evolutive_mutation(self, fator = 0.2):
        
        ngen = []
    
        for i in range(len(self.pesos)):
            
            nlayer = []
            for j in range(len(self.pesos[i])):
                npesos = []
                
                for y in range(len(self.pesos[i][j])):
                    npesos.append(self.pesos[i][j][y] * random.uniform(fator, -1 * fator))
                
                
                nlayer.append(npesos)
            ngen.append(nlayer)
        
        return ngen
        
        
    def b_retorno(self, y):
    
        if y == 0:
        
            self.score += 1
            
        else:
        
            self.score -= 1

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
    
