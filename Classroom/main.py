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
        
    ui.TLP_1022.SetWakeOnMotion('On')
    print('initialized...')
    
    
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


@event(ui.systemOffBtn, 'Pressed')
def systemOffBtnEvent(button, state):
    ui.TLP_1022.ShowPopup('Confirmation')


@event(ui.confirmShutdownBtn, 'Pressed')
def confirmShutdownBtnEvent(button, state):
    confirmShutdown()


@event(ui.closeShutdownPopupBtn, 'Pressed')
def closeShutdownPopupEvent(button, state):
    ui.TLP_1022.HidePopup('Confirmation')


@event(ui.startLightingControlPopupBtns, 'Pressed')
def startLightingControlPopupBtnEvent(button, state):
    if button == ui.splashLightingControlBtn:
        ui.TLP_1022.ShowPopup('Start Lighting Control')
    elif button == ui.closeLightingControlStartPopupBtn:
        ui.TLP_1022.HidePopup('Start Lighting Control')


@event(ui.startAudioControlPopupBtns, 'Pressed')
def startAudioControlPopupBtnEvent(button, state):
    if button == ui.splashAudioControlBtn:
        ui.TLP_1022.ShowPopup('Start Audio Control')
    elif button == ui.closeStartAudioControlPopupBtn:
        ui.TLP_1022.HidePopup('Start Audio Control')


@event(ui.audioControlPopupBtns, 'Pressed')
def audioControlPopupBtnEvent(button, state):
    if button == ui.audioControlBtn:
        ui.TLP_1022.ShowPopup('Audio Control')
    elif button == ui.closeAudioControlPopupBtn:
        ui.TLP_1022.HidePopup('Audio Control')


@event(ui.lightingControlPopupBtns, 'Pressed')
def lightingControlPopupBtnEvent(button, state):
    if button == ui.lightingControlBtn:
        ui.TLP_1022.ShowPopup('Lighting Control')
    elif button == ui.closeLightingControlPopupBtn:
        ui.TLP_1022.HidePopup('Lighting Control')


@event(ui.helpPopupBtns, 'Pressed')
def helpPopupBtnEvent(button, state):
    if button == ui.helpBtn:
        ui.TLP_1022.ShowPopup('Help')
    elif button == ui.closeHelpPopupBtn:
        ui.TLP_1022.HidePopup('Help')


@event(ui.screenControlPopupBtns, 'Pressed')
def screenControlPopupBtnEvent(button, state):
    if button == ui.screenControlBtn:
        ui.TLP_1022.ShowPopup('Screen Control')
    elif button == ui.closeScreenControlPopupBtn:
        ui.TLP_1022.HidePopup('Screen Control')


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

    ui.videoIsMuted = not ui.videoIsMuted
    if ui.videoIsMuted:
        ui.displayMuteBtn.SetState(1)
        devices.ProjectorSerialPort.Send('VMUTE ON\r')
    else:
        ui.displayMuteBtn.SetState(0)
        devices.ProjectorSerialPort.Send('VMUTE OFF\r')


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
