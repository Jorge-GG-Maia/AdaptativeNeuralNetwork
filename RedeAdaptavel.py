import numpy as np



class RedeNeural():

    def __init__(self, gen, number, pesos = 0):
        self.gen = gen
        self.name = str(gen) + str(number)
        self.pesos = pesos
        
        
    def genesis(self, amostra, camadas = 3):
    

        
        #Lista principal, contendo o conjunto de listas de cada camada (x0)
        layer = []
        
        for i in range(camadas):
            #Lista intermediária, contendo as listas de pesos específicos para cada variável (x1)
            
            c = []
            for i in range(len(amostra)):
                
                #Criação de uma lista específica de pesos para cada variável presente na amostra (x2)
                pesos = np.random.randn(len(amostra))
                
                c.append(pesos)
                
            layer.append(c)
            
        self.layers = layer


    def pensar(self, entrada):
        
        camadaatual = []    
        for i in range(len(self.layers)):
            camadatemporaria = []
            
            for j in range(len(entrada)):
            
                camadatemporaria.append(sum([entrada[j] * x for x in self.layers[i][j]]))
                
            camadaatual = camadatemporaria
            
        self.saida = sum(camadaatual)        
        return sum(camadaatual)
