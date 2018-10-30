## Begin ControlScript Import --------------------------------------------------
from extronlib import event
from extronlib.ui import Button, Label

class Password:
          
    def __init__(self, password, kpList, passwordLimit=4, useStarText=False, passwordLabel=None):
    
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
        
    def buildPassword(self, digitBtn):
    
        if len(self.enteredPassword) < self._passwordLimit:
            self.enteredPassword += self.kpMap[digitBtn]
            if self.useStarText:
                self.starText += '*'
                self.passwordLabel.SetText(self.starText)
            else:
                self.passwordLabel.SetText(self.enteredPassword)
                
    def enterPassword(self):
        
        entered, passwd = self.enteredPassword, self._password
        if self.useStarText:
            self.starText = ''
        self.passwordLabel.SetText('')
        self.enteredPassword = ''
        if entered != passwd:
            return False
        return True
    
    def clearPassword(self):
    
        self.enteredPassword = ''
        self.passwordLabel.SetText(self.enteredPassword)

    def backspace(self):
    
        if len(self.enteredPassword) != 0:
            self.enteredPassword = self.enteredPassword[:len(self.enteredPassword)-1]
            if self.useStarText:
                self.starText = self.starText[:len(self.starText)-1]
                self.passwordLabel.SetText(self.starText)
            self.passwordLabel.SetText(self.enteredPassword)
                 