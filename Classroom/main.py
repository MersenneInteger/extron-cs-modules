## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait

print(Version())
## End ControlScript Import ----------------------------------------------------
##
## Begin User Import -----------------------------------------------------------
import ui
import devices
## End User Import -------------------------------------------------------------
##
## Begin Device/Processor Definition -------------------------------------------

## End Device/Processor Definition ---------------------------------------------
##
## Begin Device/User Interface Definition --------------------------------------

## End Device/User Interface Definition ----------------------------------------
##
## Begin Communication Interface Definition ------------------------------------

## End Communication Interface Definition --------------------------------------

def Initialize():
    
    ui.logoText.SetText('Classroom Example')
    ui.roomText.SetText('Classroom')
    ui.TLP_1022.ShowPage('Start')
    
    @Wait(15)
    def PrintHardwareInfo():
        print("{0}\n{1}\n{2}\n{3}",
            devices.IPCP_555_Pro.DeviceAlias,
            devices.IPCP_555_Pro.FirmwareVersion,
            devices.IPCP_555_Pro.Hostname,
            devices.IPCP_555_Pro.IPAddress)
            
        print("{0}\n{1}\n{2}\n{3}", 
            ui.TLP_1022.DeviceAlias,
            ui.TLP_1022.FirmwareVersion,
            ui.TLP_1022.Hostname,
            ui.TLP_1022.IPAddress)
        
    #TLP_1022.SetWakeOnMotion('On')
    
    
def powerOnDisplay():
    devices.ProjectorSerialPort.Send('PWR ON\r')
    ui.displayGroup.SetCurrent(ui.displayOnBtn)
    
    
def powerOffDisplay():
    devices.ProjectorSerialPort.Send('PWR OFF\r')
    ui.displayGroup.SetCurrent(ui.displayOffBtn)
    

def screenUp():
    devices.ScreenDownRelay.SetState('Open')
    devices.ScreenUpRelay.SetState('Close')
    print("Relay 1 (Up) State: {0}", devices.ScreenUpRelay.State)
    print("Relay 2 (Down) State: {0}", devices.ScreenDownRelay.State)
    
    
def screenDown():
    devices.ScreenUpRelay.SetState('Open')
    devices.ScreenDownRelay.SetState('Close')
    print("{0} (Up) State: {1}", 
        devices.ScreenUpRelay.Port, devices.ScreenUpRelay.State)
    print("{0} 2 (Down) State: {1}",
        devices.ScreenDownRelay.Port, devices.ScreenDownRelay.State)
    
    
def confirmShutdown():
    print('shutting down...')
    ui.TLP_1022.HideAllPopups()
    ui.TLP_1022.ShowPopup('Shutting Down', 5)
    ui.TLP_1022.ShowPage('Start')
    powerOffDisplay()
    screenUp()
    
    
def volumeUp(btn, level, device, lvlRange, cmd):
    pass
    
    
def volumeDown(btn, level, device, lvlRange, cmd):
    pass
    
    
def volumeMute(btn, device, cmd):
    pass
    

def volumeUnmute(btn, device, cmd):
    pass
    
## Event Definitions -----------------------------------------------------------

##page flips
@event(ui.startBtn, 'Pressed')
def startBtnEvent(button, state):
    ui.TLP_1022.HideAllPopups()
    ui.TLP_1022.ShowPopup('Starting Up', 5)
    ui.TLP_1022.ShowPage('Main')


@event(ui.splashLightingControlBtn, 'Pressed')
def startLightingControlBtnEvent(button, state):
    ui.TLP_1022.ShowPopup('Start Lighting Control')   
  

@event(ui.closeLightingControlStartPopupBtn, 'Pressed')
def closeLightingControlStartPopupBtnEvent(button, state):
    ui.TLP_1022.HidePopup('Start Lighting Control')
    
    
@event(ui.splashAudioControlBtn, 'Pressed')
def splashAudioControlBtnEvent(button, state):
    ui.TLP_1022.ShowPopup('Start Audio Control') 
    
    
@event(ui.closeStartAudioControlPopupBtn, 'Pressed')
def closeStartAudioControlPopupBtnEvent(button, state):
    ui.TLP_1022.HidePopup('Start Audio Control')


@event(ui.systemOffBtn, 'Pressed')
def systemOffBtnEvent(button, state):
    ui.TLP_1022.ShowPopup('Confirmation')
    

@event(ui.confirmShutdownBtn, 'Pressed')
def confirmShutdownBtnEvent(button, state):
    confirmShutdown()
    

@event(ui.closeShutdownPopupBtn, 'Pressed')
def closeShutdownPopupEvent(button, state):
    ui.TLP_1022.HidePopup('Confirmation')
    
    
@event(ui.audioControlBtn, 'Pressed')
def audioControlBtnEvent(button, state):
    ui.TLP_1022.ShowPopup('Audio Control')
    

@event(ui.closeAudioControlPopupBtn, 'Pressed')
def closeAudioControlPopupBtnEvent(button, state):
    ui.TLP_1022.HidePopup('Audio Control')


@event(ui.lightingControlBtn, 'Pressed')
def lightingControlBtnEvent(button, state):
    pass
 
 
@event(ui.closeLightingControlPopupBtn, 'Pressed')
def closeLightingControlPopupBtnEvent(button, state):
    pass


@event(ui.helpBtn, 'Pressed')
def helpBtnEvent(button, state):
    pass
    
    
@event(ui.closeHelpPopupBtn, 'Pressed')
def closeHelpPopupEvent(button, state):
    pass
    

@event(ui.screenControlBtn, 'Pressed')
def screenControlBtnEvent(button, state):
    pass


@event(ui.closeScreenControlPopupBtn, 'Pressed')
def closeScreenControlPopupBtnEvent(button, state):
    pass


## source selection
@event(ui.sourceList, 'Pressed')
def sourceSelectedEvent(button, state):
    pass
    
 
##device control

#display
@event(ui.displayOnBtn, 'Pressed')
def displayOnBtnEvent(button, state):
    powerOnDisplay()
    
    
@event(ui.displayOffBtn, 'Pressed')
def displayOffBtnEvent(button, state):
    powerOffDisplay()
    
    
@event(ui.displayMuteBtn, 'Pressed')
def displayMuteBtnEvent(button, state):
    pass


@event(devices.ProjectorSerialPort, 'ReceiveData')
def MainFeedbackHandler(interface, rcvString):
    
    rxBuffer = rcvString.decode()
    print(rxBuffer)

#screen

#bluray

#smd

##audio control
    
## End Events Definitions-------------------------------------------------------

Initialize()
