# AdaptativeNeuralNetwork

Este repositório oferece uma proposta de rede neural artificial densa que pode ser adaptada para em diferentes nescessidades e diferentes tipos de algoritmos de otimização de pesos mas com o diferencial de ser capaz de se adaptar sozinha a diferentes números de variáveis e diferentes contextos de aplicação. 

Para utilizar este recurso basta utilizar a função .genesis(amostra, n) onde amostra seria um exemplo das variaveis de entrada que serão recebidos pela rede neural (em formato de lista) e n representa o número de camadas que a rede neural terá, após chamada a função, a rede neural cria um conjunto de pesos iniciais aleatórios que servirão de base para as otimizações futuras. Para executar o cálculo da rede neural deve-se utilizar a função .pensar(entrada) onde entrada seria uma lista contendo os dados de entrada com o mesmo shape da amostra dada na etapa anterior.
