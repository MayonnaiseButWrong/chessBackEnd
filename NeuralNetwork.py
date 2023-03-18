import numpy as np
from np import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        self.weights=fileDecomposition(open("Weights.txt","rt"))
        self.baises=fileDecomposition(open("Baisess.txt","rt"))
        #this only works for one layer rn, fix it big man
        
    def fileDecomposition(self,f):
        text=str(f.read())
        word,array,col=text[0],[],0
        for count in len(text):
            if text[count]==';':
                array[col].append(float(word))
            elif text[count]=='$':
                array[col].append(float(word))
                col+=1
                array.append([])
            else:
                word+=text[count]
        return np.asmatrix(array)
        
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
    
    def __sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def evaluate(self, ins):
        