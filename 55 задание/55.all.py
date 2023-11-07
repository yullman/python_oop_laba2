class text():
    text = 'gerhj rjgeru 4534 jjh'
    def getSymb(self):
        return(len(self.text))
    def probels(self):
        g = 0
        for i in range(len(self.text)):
            if self.text[i] == " ":
                g+=1
        return g
    def bezprob(self):
        g = 0
        for i in range(len(self.text)):
            if self.text[i] == " ":
                g+=1
        return len(self.text) - g

test = text()
print(test.getSymb())
print(test.probels())
print(test.bezprob())