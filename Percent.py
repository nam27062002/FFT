class statistical:
    def __init__(self,trainning) -> None:
        self.training = trainning
        self.vowels = ["a","e","i","o","u"]
        self.Correct,self.ARR = self.processPercent()
        self.Percent = self.Correct / 105 * 100
    def processPercent(self):
        arr = [ [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
        s = 0
        for vowel in self.vowels: 
            eigenvector = []
            for index in range(1,22):
                url = f"Test/{index}/{vowel}.wav"
                if self.training.compare(url)[0] == vowel:
                    s += 1
                if self.training.compare(url)[0] == vowel and vowel == "a":
                    arr[0][0] += 1
                elif self.training.compare(url)[0] == vowel and vowel == "e":
                    arr[1][1] += 1
                elif self.training.compare(url)[0] == vowel and vowel == "i":
                    arr[2][2] += 1
                elif self.training.compare(url)[0] == vowel and vowel == "o":
                    arr[3][3] += 1
                elif self.training.compare(url)[0] == vowel and vowel == "u":
                    arr[4][4] += 1

                elif self.training.compare(url)[0] == "e" and vowel == "a":
                    arr[1][0] += 1
                elif self.training.compare(url)[0] == "i" and vowel == "a":
                    arr[2][0] += 1
                elif self.training.compare(url)[0] == "o" and vowel == "a":
                    arr[3][0] += 1
                elif self.training.compare(url)[0] == "u" and vowel == "a":
                    arr[4][0] += 1
                
                elif self.training.compare(url)[0] == "a" and vowel == "e":
                    arr[0][1] += 1
                elif self.training.compare(url)[0] == "i" and vowel == "e":
                    arr[2][1] += 1
                elif self.training.compare(url)[0] == "o" and vowel == "e":
                    arr[3][1] += 1
                elif self.training.compare(url)[0] == "u" and vowel == "e":
                    arr[4][1] += 1
                
                elif self.training.compare(url)[0] == "a" and vowel == "i":
                    arr[0][2] += 1
                elif self.training.compare(url)[0] == "e" and vowel == "i":
                    arr[1][2] += 1
                elif self.training.compare(url)[0] == "o" and vowel == "i":
                    arr[3][2] += 1
                elif self.training.compare(url)[0] == "u" and vowel == "i":
                    arr[4][2] += 1
                
                elif self.training.compare(url)[0] == "a" and vowel == "o":
                    arr[0][3] += 1
                elif self.training.compare(url)[0] == "e" and vowel == "o":
                    arr[1][3] += 1
                elif self.training.compare(url)[0] == "i" and vowel == "o":
                    arr[2][3] += 1
                elif self.training.compare(url)[0] == "u" and vowel == "o":
                    arr[4][3] += 1
                
                elif self.training.compare(url)[0] == "a" and vowel == "u":
                    arr[0][4] += 1
                elif self.training.compare(url)[0] == "e" and vowel == "u":
                    arr[1][4] += 1
                elif self.training.compare(url)[0] == "i" and vowel == "u":
                    arr[2][4] += 1
                elif self.training.compare(url)[0] == "o" and vowel == "u":
                    arr[3][4] += 1
        return s,arr