import random
from NeuralNetwork import*

NNUE=NeuralNetwork([4*64,8*128,8*128,8*128,8*128,8*128,10])

def ratingBasedOnNeuralNetwork(boardLayout):
    num=random.randint(0, 200)
    return num/100