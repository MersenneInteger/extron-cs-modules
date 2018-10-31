## Begin ControlScript Import --------------------------------------------------
from extronlib import event
from extronlib.ui import Button, Label

class Password:
          
    def __init__(self, password, kpList, adminPassword=None, passwordLimit=4, useStarText=False, passwordLabel=None):
    
        self._password = password
        self._adminPassword = adminPassword
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
            try:
                self.enteredPassword += self.kpMap[digitBtn]
                if self.useStarText:
                    self.starText += '*'
                    self.passwordLabel.SetText(self.starText)
                else:
                    self.passwordLabel.SetText(self.enteredPassword)
            except KeyError:
                print('Key Error in buildPassword(): Key not found in dictionary')
            except Exception as e:
                print('Exception caught in buildPassword(): {}'.format(e.args))
                
    def enterPassword(self):
        
        entered, passwd, adminPasswd = self.enteredPassword, self._password, self._adminPassword
        if self.useStarText:
            self.starText = ''
        self.passwordLabel.SetText('')
        self.enteredPassword = ''

        if entered != passwd and entered != adminPasswd:
            print('password incorrect')
            return False
        elif entered == passwd:
            print('password correct')
            return 1
        elif entered == adminPasswd:
            print('admin password correct')
            return 2
    
    def clearPassword(self):
    
        self.enteredPassword = ''
        self.passwordLabel.SetText(self.enteredPassword)

    def backspace(self):
    
        if len(self.enteredPassword) != 0:
            self.enteredPassword = self.enteredPassword[:len(self.enteredPassword)-1]
            if self.useStarText:
                self.starText = self.starText[:len(self.starText)-1]
                self.passwordLabel.SetText(self.starText)
            else:
                self.passwordLabel.SetText(self.enteredPassword)
                 