import SpeechAndSilence
import numpy as np
class Process:
    def __init__(self,N_FFT) -> None:
        self.F = 0
        self.N_FFT = N_FFT
        self.vowels = ["a","e","i","o","u"]
        self.eigenvectors = self.Training()

    def compare(self,url):
        audio = SpeechAndSilence.Process(url,self.N_FFT)
        eigenvector = audio.VectorFFT
        standardDeviations = []
        for i in self.eigenvectors:
            s = 0
            for j in range(len(i)):
                s += pow((i[j] - eigenvector[j]),2)
            standardDeviations.append(s)
        return [self.vowels[self.minIndex(standardDeviations)],f"Dự đoán đây là nguyên âm {self.vowels[self.minIndex(standardDeviations)].upper()}"]
    
    def minIndex(self,arr):
        index = -1
        min = 100000000000000000
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
                index = i
        return index
    
    def Training(self):
        eigenvectors = []
        s = 0
        check = True
        for vowel in self.vowels: 
            eigenvector = []
            for index in range(1,22):
                s += 1
                url = f"Training/{index}/{vowel}.wav"
                Audio = SpeechAndSilence.Process(url,self.N_FFT)
                if check:
                    self.F = Audio.F
                    self.N_FFT = Audio.N_FFT
                eigenvector.append(Audio.VectorFFT)
                check = False
            average = []
            for i in range(Audio.N_FFT):
                s = 0
                for j in range(len(eigenvector)):
                    s += abs(eigenvector[j][i])
                average.append(s/len(eigenvector))
            eigenvectors.append(average)
        return eigenvectors
    
    def getEigenvectors(self):
        x = np.linspace(0.0, self.N_FFT/self.F, self.N_FFT)
        x_f = np.linspace(0.0, 1.0/(1.0/self.F), self.N_FFT)
        ARR = []
        for i in self.eigenvectors:
            ARR.append([x_f,i])
        return ARR
