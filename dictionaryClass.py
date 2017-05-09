##Dictionary Class

class dictionary(object):
    
    def __init__(self):
        self.charList = ['A', 'A', 'A']
        
        self.dictionaryList = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
                          'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h',
                          'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
                          'z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^',
                          '&','*','(',')','-','_','=','+','/',';',':',',','.','<','>',
                          '?')
        self.charNum = [0, 0, 0]
        
    def changeChar(self, selected, direction):
        self.charNum[selected] += direction
        if self.charNum[selected] > 83:
            self.charNum[selected] = 0
        if self.charNum[selected] < 0:
            self.charNum[selected] = 83
        self.charList[selected] = self.dictionaryList[self.charNum[selected]]
        