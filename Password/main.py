## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import (ContactInterface, DigitalIOInterface,
    EthernetClientInterface, EthernetServerInterfaceEx, FlexIOInterface,
    IRInterface, RelayInterface, SerialInterface, SWPowerInterface,
    VolumeInterface)
from extronlib.ui import Button, Knob, Label, Level
from extronlib.system import Clock, MESet, Wait
from password import Password

print(Version())
## End ControlScript Import ----------------------------------------------------
## Begin Device/Processor Definition -------------------------------------------
IPCPPro555 = ProcessorDevice('IPCPPro555')
TLPPro520M = UIDevice('TLPPro1022M')
## End Device/Processor Definition ---------------------------------------------
##
## Begin Device/User Interface Definition --------------------------------------
kp0 = Button(TLPPro520M, 600)
kp1 = Button(TLPPro520M, 601)
kp2 = Button(TLPPro520M, 602)
kp3 = Button(TLPPro520M, 603)
kp4 = Button(TLPPro520M, 604)
kp5 = Button(TLPPro520M, 605)
kp6 = Button(TLPPro520M, 606)
kp7 = Button(TLPPro520M, 607)
kp8 = Button(TLPPro520M, 608)
kp9 = Button(TLPPro520M, 609)
passcodeEnterBtn = Button(TLPPro520M, 610)
passcodeClearBtn = Button(TLPPro520M, 611, repeatTime = 1)
passCodeLabel = Label(TLPPro520M, 65000)
kpList = [kp0, kp1, kp2, kp3, kp4, kp5, kp6, kp7, kp8, kp9]

mainPassword = Password('8080', kpList, '1234', 4, True, passCodeLabel)

## Event Definitions -----------------------------------------------------------
def Initialize():
    pass

@event(kpList, 'Pressed')
def kpBtnEvent(button, state):
    
    mainPassword.buildPassword(button)

@event(passcodeClearBtn, ['Pressed', 'Repeated'])
def passcodeClearBtnEvent(button, state):
    
    if state == 'Pressed':
        mainPassword.backspace()
    elif state == 'Repeated':
        mainPassword.clearPassword()

@event(passcodeEnterBtn, 'Pressed')
def passcodeEnterBtnEvent(button, state):

    passwordValidate = mainPassword.enterPassword()
    if passwordValidate == 1:
        passCodeLabel.SetText('Correct')
    elif passwordValidate == 2:
        passCodeLabel.SetText('Admin Password Correct')
    else:
        passCodeLabel.SetText('Incorrect')
        
## End Events Definitions-------------------------------------------------------

Initialize()
