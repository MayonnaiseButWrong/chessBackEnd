from numpy import exp, array, random, asmatrix, matmul, add

class NeuralNetwork():
    def __init__(self,layers):
        fweights=open("Weights.txt","w+")
        fbaises=open("Baises.txt","w+")
        self.layers=layers
        if len(str(fweights.read()))<1 or len(str(fbaises.read()))<1:
            self.weights=__createFile(fweights)
            self.baises=__createFile(fbaises)
        else:
            self.weights=__fileDecomposition(fweights)
            self.baises=__fileDecomposition(fbaises)
        self.training_examples=[]
        
    def __createFile(self,f):
        out,arrays,array='',[],[]
        for i in range(len(layers)-1):
            layer1=self.layers[i]
            layer2=self.layers[i+1]
            for j in range(layer2-1):
                array.append([])
                for k in range(layer1-1):
                    out+='1.0,'
                    array[-1].append(1)
                out+='1.0;'
            for k in range(layer1-1):
                    out+='1.0,'
                    array[-1].append(1)
            out+='1.0$'
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
        self.__UpdateFiles(open("Weights.txt","w+"),weightchange)
        self.__UpdateFiles(open("Baises.txt","w+"),baischange)
        
    def __fileDecomposition(self, f):
        text=str(f.read())
        word,array,col,out=text[0],[],0,[]
        for count in range(len(text)):
            if text[count]==',':
                array[col].append(float(word))
            elif text[count]==';':
                array[col].append(float(word))
                col+=1
                array.append([])
            elif text[count]=='$':
                out.append(array)
            else:
                word+=text[count]
        return out
        
    def __sigmoid(self, x):
        return 1.0 / (1.0 + exp(-x))
    
    def __sigmoid_derivative(self, x):
        return x * (1.0 - x)
    
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
        return numpy.getA(numpy.matmul(m1,m2))
    
    def __matrixadd(self,ins1,ins2):
        m1,m2=numpy.asmatrix(ins1),numpy.asmatrix(ins2)
        return numpy.getA(numpy.add(m1,m2))
    
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
        m1,out=__encode(ins),[]
        for i in range(len(self.weights)):
            m2 = self.__matrixmul(m1,self.weights[i])
            m3 = self.__matrixadd(m2,self.baises[i])
            m1 = self.__applySigmoid(m3)
            out.append(m1)
        return out
    
    def evaluate(self, ins):
        l=self.__testevaluate(ins)
        out=l[-1]
        return self.__decode(out)
    
    def __encode(self,ins):
        out,piecedict=[],{'MT':[0,0,0,0],'WP':[0,0,0,1],'BP':[0,0,1,0],'WB':[0,0,1,1],'BB':[0,1,0,0],'WN':[0,1,0,1],'BN':[0,1,1,0],'WR':[0,1,1,1],'BR':[1,0,0,0],'WQ':[1,0,0,1],'BQ':[1,0,1,0],'WK':[1,1,0,1],'BK':[1,1,1,0]}
        for j in range(8):
            for i in range(8):
                out=piecedict[ins[j][i]]+out
        return out
    
    def __decode(self,ins):
        m=''
        for a in ins:
            m1+=str(a[0])
        exponent,mantissa=int(bin(m[0,3])),float(bin(m[4,-1])*(2^(-5)))
        out=mantissa^exponent
        if out>1.0:out=1.0
        elif out<0.001:out=0
        return out
    
    def __backprop(self,listofweights,listofbaises,activations,example):
        weights,baises,activation,activationchanges,activationchange,nextLayerExample,temp=listofweights[-1],listofbaises[-1],activations[-1],[],[],[],0
        for number in example[0]:
            error=(activation[i][0]-number)/activation[i][0]
            for j in range(len(weights)):
                for i in range(len(weights[i])):
                    temp+=error*self.__sigmoid_derivative(number)-baises[i][0]*weights[j][i]
                activationchange.append([temp])
            activationchanges.append(activationchange)
            if len(nextLayerExample)>0:
                nextLayerExample=self.__matrixadd(nextLayerExample,activationchange)
            else:
                nextLayerExample=activationchanges
                
        if len(activations)>2:
            weightchanges,baischanges=__backprop(listofweights[0:-1],listofbaises[0:-1],activations[0:-1],__matrixmul(activation[-2],nextLayerExample)+example)
            #weightchange,baischange=weightchanges[-1],baischanges[-1]
        else:
            weightchanges,baischanges=[],[]
        
        weightchange,baischange,activationchanges=activationchanges,[],nextLayerExample
        baischange=self.__matrixsub(self.__matrixmul(self.__matrixmeld(weights,activationchanges),activation[-2]),activation[-1])
        weightchanges.append(weightchange)
        baischanges.append(baischange)
        return weightchanges,baischanges
            
            
    def train(self,data):
        self.training_examples.append(data)
        if len(self.training_examples)>=50:
            weightchanges,baischanges=[],[]
            for example in self.training_examples:
                activations=__testevaluate(example[0])
                weightchange,baischange=__backprop(self.weights,self.baises,example[0]+activations,example[1])
                weightchanges.append(weightchange)
                baischanges.append(baischange)
            self.weights=self.__matrixmeld(weightchange,self.__findAverage(weightchanges))
            self.baises=self.__matrixmeld(baischanges, self.__findAverage(baischanges))
            self.__UpdateWeightsAndBaises(self.weights,self.baises)
            #translate the stockfish thing into something the nnue can understand
    