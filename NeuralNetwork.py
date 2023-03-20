import time
import numpy
from numpy import exp, array, random, asmatrix, matmul, add

class NeuralNetwork():
    def __init__(self,layers):
        fweights=open("Weights.txt","rt")
        fbaises=open("Baises.txt","rt")
        self.layers=layers
        self.learning_rate = 1
        if len(str(fweights.read()))<1 or len(str(fbaises.read()))<1:
            self.weights=self.__createFileW(open("Weights.txt","wt"))
            self.baises=self.__createFileB(open("Baises.txt","wt"))
            print('here')
        else:
            self.weights=self.__fileDecomposition(open("Weights.txt","rt"))
            self.baises=self.__fileDecomposition(open("Baises.txt","rt"))
            print('there')
        self.training_examples=[]
        
    def __createFileW(self,f):
        out,arrays,array='',[],[]
        for i in range(len(self.layers)-1):
            layer1=self.layers[i]
            layer2=self.layers[i+1]
            for j in range(layer2-1):
                array.append([])
                for k in range(layer1-1):
                    out+='1.0,'
                    array[-1].append(1.0)
                out+='1.0;'
                array[-1].append(1.0)
            array.append([])
            for k in range(layer1-1):
                    out+='1.0,'
                    array[-1].append(1.0)
            out+='1.0$'
            array[-1].append(1.0)
            print(len(array))
            arrays.append(array)
            array=[]
        f.write(out)
        return arrays
    
    def __createFileB(self,f):
        out,arrays,array='',[],[]
        for i in range(len(self.layers)-1):
            layer=self.layers[i+1]
            for j in range(layer-1):
                array.append([1.0])
                out+='1.0;'
            out+='1.0$'
            array.append([1.0])
            arrays.append(array)
        f.write(out)
        return arrays
    
    def __UpdateFiles(self,f,l):
        out,arrays,array='',[],[]
        for i in range(len(layers)-1):
            layer1=self.layers[i]
            layer2=self.layers[i+1]
            for j in range(layer2-1):
                for k in range(layer1-1):
                    out=out+str(l[k])+','
                out+=out+str(l[k+1])+';'
            for k in range(layer1-1):
                    out=out+str(l[k])+','
            out=out+str(l[k+1])+'$'
        f.write(out)
    
    def __UpdateWeightsAndBaises(self,weightchange,baischange):
        self.__UpdateFiles(open("Weights.txt","wt"),weightchange)
        self.__UpdateFiles(open("Baises.txt","wt"),baischange)
        
    def __fileDecomposition(self, f):
        text=str(f.read())
        word,array,out=text[0],[[]],[]
        for count in range(1,len(text)):
            if text[count]==',':
                array[-1].append(float(word))
                word=''
            elif text[count]==';':
                array[-1].append(float(word))
                word=''
                array.append([])
            elif text[count]=='$':
                array[-1].append(float(word))
                word=''
                out.append(array)
                array=[[]]
            else:
                word+=text[count]
        return out
        
    def __sigmoid(self, x):
        return 1.0 / (1.0 + exp(-x))
    
    def __sigmoid_derivative(self, x):
        return x / (1.0 - x)
    
    def __applySigmoid(self, ins):
        array1,array2,count=ins,[],0
        for row in array1:
            array2.append([])
            for element in row:
                array2[count].append(self.__sigmoid(element))
            count+=1
        return array2
    
    def __matrixmul(self,ins1,ins2):
        m1,m2=numpy.asmatrix(ins1),numpy.asmatrix(ins2)
        return numpy.matrix.getA(numpy.matmul(m1,m2))
    
    def __matrixadd(self,ins1,ins2):
        m1,m2=numpy.asmatrix(ins1),numpy.asmatrix(ins2)
        return numpy.matrix.getA(numpy.add(m1,m2))
    
    def __matrixsub(self,ins1,ins2):
        for j in range(len(ins2)):
            for i in range(len(ins2)):
                ins2[j][i]=-ins2[j][i]
        return self.__matrixadd(ins1,ins2)
    
    def __matrixmeld(self,ins1,ins2):
        out=[]
        for j in range(len(ins2)):
            out.append([])
            for i in range(len(ins2[j])):
                out[j].append(ins1[j][i]*ins2[j][i])
        return out
    
    def __matrixtranspose(self,ins):
        m=numpy.asmatrix(ins)
        return numpy.matrix.getA(numpy.matrix.transpose(m))
    
    def __reduce(self,ins):
        out=self.__matrixadd(ins[0],ins[1])
        for i in range(2,len(ins)):
            out=self.__matrixadd(out,ins[i])
        return out
    
    def __matrixmulconst(self,ins1,ins2):
        out=[]
        for j in range(len(ins2)):
            out.append([])
            for i in range(len(ins2[j])):
                out[j].append(ins1*ins2[j][i])
        return out
    
    def __findAverage(self,ins):
        out=[]
        for a in range(len(ins[0])):
            templist=[]
            for element in ins:
                templist.append(element[a])
            out.append(self.__matrixmulconst((1/len(ins)),self.__reduce(templist)))
        return out
    
    def __testevaluate(self, ins):
        m1,out=self.__encode(ins),[]
        for i in range(len(self.weights)):
            m2 = self.__matrixmul(self.weights[i],m1)
            m3 = self.__matrixadd(m2,self.baises[i])
            m1 = self.__applySigmoid(m3)
            out.append(m1)
        return out
    
    def evaluate(self, ins):
        l=self.__testevaluate(ins)
        out=l[-1]
        return self.__decode(out)
    
    def __encode(self,ins):
        out,piecedict=[],{'MT':[[0],[0],[0],[0]],'WP':[[0],[0],[0],[1]],'BP':[[0],[0],[1],[0]],'WB':[[0],[0],[1],[1]],'BB':[[0],[1],[0],[0]],'WN':[[0],[1],[0],[1]],'BN':[[0],[1],[1],[0]],'WR':[[0],[1],[1],[1]],'BR':[[1],[0],[0],[0]],'WQ':[[1],[0],[0],[1]],'BQ':[[1],[0],[1],[0]],'WK':[[1],[1],[0],[1]],'BK':[[1],[1],[1],[0]]}
        for j in range(8):
            for i in range(8):
                out=piecedict[ins[j][i]]+out
        return out
    
    def __decode(self,ins):
        m=''
        for a in ins:
            m+=str(int(round(a[0])))
        if m[0]=='1':exponent=-(int(self.__bintoint(self.__twoscompliment(m[0:4]))))
        else:exponent=int(self.__bintoint(m[0:4]))
        mantissa=float(self.__bintoint(m[3:-1]))*0.03125
        out=mantissa*(2**exponent)
        if out>1.0:out=1.0
        elif out<0.001:out=0
        return out
    
    def __bintoint(self,ins):
        out,ins=0,ins[::-1]
        for i in range(len(ins)):
            x=1
            if ins[i]=='1':
                for a in range(i):
                    x*=2
                out+=(x)
        return out
    
    def __twoscompliment(self,ins):
        flag,out=False,''
        for n in range(len(ins)):
            if n>len(ins):n=0
            if ins[-n]=='1' and flag==False:
                out='1'+out
                flag=True
            elif ins[-n]=='1':
                out='0'+out
            else:
                out='1'+out
        return out
    
    def __backprop(self,listofweights,listofbaises,activations,example):#  C′(W)=(O−y)⋅R′(Z)⋅H         where C'(w) is the rate of change of the ocst function with respect to the weights, O is the output of the function, y in the expected value, R'(Z) is the sum of the previos layer's activation times their respective weights put into the derivitive of the sigmoid function, H is the previos layer's activation. explanaition: https://ml-cheatsheet.readthedocs.io/en/latest/backpropagation.html 
        weights,baises,activation,activationchanges,activationchange,nextLayerExample,temp=self.__matrixtranspose(listofweights[-1]),listofbaises[-1],activations[-1],[],[],[],0    #  W=W-ΔW       ΔW=Error of layer infront * activation of current Layer * learning rate
        #for number in example[0]:
        #    for j in range(len(weights)):
        #        for i in range(len(weights[j])):
        #            print(len(activation),len(weights[j]),len(weights),i)
        #            error=(activation[i][0]-number)/activation[i][0]
        #            temp+=error*self.__sigmoid_derivative(number)*weights[j][i]                                               <- possibly all wrong so....    redo it all
        #        activationchange.append([temp])
        #    print('here')
        #    activationchanges.append(activationchange)
        #    if len(nextLayerExample)>0:
        #        nextLayerExample=self.__matrixadd(nextLayerExample,activationchange)
        #    else:
        #        nextLayerExample=activationchanges
        #        
        #print(len(activations[-2][0]),len(activations[-2]),len(nextLayerExample),len(nextLayerExample[0]))
        #if len(activations)>2:
        #    weightchanges,baischanges=self.__backprop(listofweights[0:-1],listofbaises[0:-1],activations[0:-1],self.__matrixmul(activations[-2],nextLayerExample)+example)
        #    #weightchange,baischange=weightchanges[-1],baischanges[-1]
        #else:
        #    weightchanges,baischanges=[],[]
        #
        #weightchange,baischange,activationchanges=activationchanges,[],nextLayerExample
        #baischange=self.__matrixsub(self.__matrixmul(self.__matrixmeld(weights,activationchanges),activations[-2]),activations[-1])
        #weightchanges.append(weightchange)
        #baischanges.append(baischange)
        #return weightchanges,baischanges      
            
    def train(self,data):
        self.training_examples.append(data)
        if len(self.training_examples)>=1:
            weightchanges,baischanges=[],[]
            for example in self.training_examples:
                activations=self.__testevaluate(example[0])
                weightchange,baischange=self.__backprop(self.weights,self.baises,example[0]+activations,example[1])
                weightchanges.append(weightchange)
                baischanges.append(baischange)
            self.weights=self.__matrixmeld(weightchange,self.__findAverage(weightchanges))
            self.baises=self.__matrixmeld(baischanges, self.__findAverage(baischanges))
            self.__UpdateWeightsAndBaises(self.weights,self.baises)
            #translate the stockfish thing into something the nnue can understand


if __name__ =="__main__":
    start_time = time.time()
    NNUE=NeuralNetwork([4*64,8*128,8*128,8*128,8*128,8*128,10])
    out=NNUE.evaluate([['BR','BN','BB','BQ','BK','BB','BN','BR'],['BP','BP','BP','BP','BP','BP','BP','BP'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['MT','MT','MT','MT','MT','MT','MT','MT'],['WP','WP','WP','WP','WP','WP','WP','WP'],['WR','WN','WB','WQ','WK','WB','WN','WR']])
    print(out)
    print('done')
    print("--- %s seconds ---" % (time.time() - start_time))
