## Begin ControlScript Import --------------------------------------------------
from extronlib import event
from extronlib.ui import Button, Label

class Password:
          
    def __init__(self, password, passwordLimit=4, kpList, useStarText=False, passwordLabel=None):
    
        self._password = password
        self._passwordLimit = passwordLimit
        self.kpList = kpList
        self.kpMap = {}
        for i in range(len(kpList)):
            self.kpMap[kpList[i]] = str(i)
        self.enteredPassword = ''
        self.useStarText = useStarText
        self.starText = ''
        self.passwordLabel = passwordLabel
        
    def buildPassword(digitBtn):
    
        if len(self.enteredPassword) < self._passwordLimit:
            self.enteredPassword += kpMap[digitBtn]
            if useStarText:
                buildStarText()
            else:
                self.passwordLabel.SetText(self.enteredPassword)
                
    @classmethod
    def buildStarText(cls):

        self.starText += '*'
    
    def enterPassword():
        
        if useStarText:
            self.starText = ''
        self.passwordLabel.SetText('')
        self._password = ''
        self.enteredPassword = ''
        if self.enteredPassword != self._password:
            return False
       return True
    
    def clearPassword():
    
        self.enteredPassword = ''

    def backspace():
    
        if len(self.enteredPassword) != 0:
            self.enteredPassword = self.enteredPassword[:len(self.enteredPassword)-1]
            if useStarText:
                self.starText = self.starText[:len(self.starText)-1]
                self.passwordLabel.SetText(self.starText)
           self.passwordLabel.SetText(self.enteredPassword)
                 