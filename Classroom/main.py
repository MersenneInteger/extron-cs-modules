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
    
    ui.logoText.SetText('Conference Room')
    ui.roomText.SetText('Room 1025')
    ui.TLP_1022.ShowPage('Start')
    #connectSMD202()
    
    @Wait(10)
    def PrintHardwareInfo():
        print('{0}\n{1}\n{2}\n{3}'.format(
            devices.IPCP_555_Pro.DeviceAlias,
            devices.IPCP_555_Pro.FirmwareVersion,
            devices.IPCP_555_Pro.Hostname,
            devices.IPCP_555_Pro.IPAddress))
            
        print('{0}\n{1}\n{2}\n{3}'.format(
            ui.TLP_1022.DeviceAlias,
            ui.TLP_1022.FirmwareVersion,
            ui.TLP_1022.Hostname,
            ui.TLP_1022.IPAddress))
        
    ui.TLP_1022.SetWakeOnMotion('On')
    print('initialized...')
    
   
def connectSMD202():
    
    connectionStatus = ''
    try:
        connectionStatus = devices.SMD202EthernetClient.Connect(5)
    except:
        print('Error occured connecting to SMD202 [{0}]'.format( 
            devices.SMD202EthernetClient.IPAddress))
            
    print(connectionStatus)
    if connectionStatus == 'Connected':
        print('SMD202 connected')
    else:
        print('SMD202 connection failed...retrying')
        Wait(30, connectSMD202)


def confirmShutdown():
    
    print('shutting down...')
    ui.TLP_1022.HideAllPopups()
    ui.TLP_1022.ShowPopup('Shutting Down', 5)
    ui.TLP_1022.ShowPage('Start')
    powerOffDisplay()
    screenUp()
    
    
def volumeUp(btn, level, device, lvlRange, cmd):
    
    btn.SetState(1)
    device.Send(cmd)
    level.SetRange(lvlRange[0],lvlRange[1],lvlRange[2])
    level.Inc()
    btn.SetState(0)
    
    
def volumeDown(btn, level, device, lvlRange, cmd):
    
    btn.SetState(1)
    device.Send(cmd)
    level.SetRange(lvlRange[0],lvlRange[1],lvlRange[2])
    level.Dec()
    btn.SetState(0)
    
    
def volumeMute(btn, device, cmd):
    
    devices.DMP44SerialPort.Send('WM30100*1AU\r')
    @Wait(0.5)
    def GetMuteStatus():
        muteState = devices.DMP44SerialPort.SendAndWait('WM30100AU\r', 1)
        print(muteState)
        if muteState:
            muteState = muteState.decode()
            if btn == ui.afvVolMuteBtn:
                if 'DsM30100*1' in muteState:
                    ui.afvIsMuted = True
                    ui.afvVolMuteBtn.SetState(1)
            elif btn == ui.mic1VolMuteBtn:
                if 'DsM30101*1' in muteState:
                    ui.mic1IsMuted = True
                    ui.mic1VolMuteBtn.SetState(1)
            elif btn == ui.mic2VolMuteBtn:
                if 'DsM30102*1' in muteState:
                    ui.mic2IsMuted = True
                    ui.mic2VolMuteBtn.SetState(1)


def volumeUnmute(btn, device, cmd):
    
    devices.DMP44SerialPort.Send('WM30100*0AU\r')
    @Wait(0.5)
    def GetUmuteStatus():
        muteState = devices.DMP44SerialPort.SendAndWait('WM30100AU\r', 1)
        print(muteState)
        if muteState:
            muteState = muteState.decode()
            if btn == ui.afvVolMuteBtn:
                if 'DsM30100*0' in muteState:
                    ui.afvIsMuted = False
                    ui.afvVolMuteBtn.SetState(0)
            elif btn == ui.mic1VolMuteBtn:
                if 'DsM30101*0' in muteState:
                    ui.mic1IsMuted = False
                    ui.mic1VolMuteBtn.SetState(0)
            elif btn == ui.mic2VolMuteBtn:
                if 'DsM30102*0' in muteState:
                    ui.mic2IsMuted = False
                    ui.mic2VolMuteBtn.SetState(0)


def powerOnDisplay():
    
    devices.ProjectorSerialPort.Send('PWR ON\r')
    ui.displayGroup.SetCurrent(ui.displayOnBtn)
    
    
def powerOffDisplay():
    
    devices.ProjectorSerialPort.Send('PWR OFF\r')
    ui.displayGroup.SetCurrent(ui.displayOffBtn)
    

def screenUp():
    
    devices.ScreenDownRelay.SetState('Open')
    devices.ScreenUpRelay.SetState('Close')
    print("Relay 1 (Up) State: {0}".format(devices.ScreenUpRelay.State))
    print("Relay 2 (Down) State: {0}".format(devices.ScreenDownRelay.State))
    @Wait(3)
    def screenUpOpenRelayWait():
        devices.ScreenUpRelay.SetState('Open')
    
    
def screenDown():
    
    devices.ScreenUpRelay.SetState('Open')
    devices.ScreenDownRelay.SetState('Close')
    print("{0} (Up) State: {1}".format(
        devices.ScreenUpRelay.Port, devices.ScreenUpRelay.State))
    print("{0} 2 (Down) State: {1}".format(
        devices.ScreenDownRelay.Port, devices.ScreenDownRelay.State))
    @Wait(3)
    def screenUpOpenRelayWait():
        devices.ScreenDownRelay.SetState('Open')
 
def autoShutdown():
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
        ui.TLP_1022.ShowPopup('Start Lighting Control', 20)
    elif button == ui.closeLightingControlStartPopupBtn:
        ui.TLP_1022.HidePopup('Start Lighting Control')


@event(ui.startAudioControlPopupBtns, 'Pressed')
def startAudioControlPopupBtnEvent(button, state):
    
    if button == ui.splashAudioControlBtn:
        ui.TLP_1022.ShowPopup('Start Audio Control', 20)
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
    
    devices.MPS602SerialPort.Send(ui.sourceCmdMap[button])
    ui.TLP_1022.ShowPopup(ui.sourcePageFlipMap[button])


@event(devices.MPS602SerialPort, 'ReceiveData')
def MPS602SerialPortFeedbackHandler(interface, rcvString):

    rxBuffer = rcvString.decode()
    print(rxBuffer)
    if rxBuffer:
        rxBuffer = rxBuffer.decode()
        
        if 'In1 All' in rxBuffer:
            ui.sourcesGroup.SetCurrent(ui.sourceLaptopBtn)
        elif 'In2 All' in rxBuffer:
            ui.sourcesGroup.SetCurrent(ui.sourcePCBtn)
        elif 'In3 All' in rxBuffer:
            ui.sourcesGroup.SetCurrent(ui.sourceBlurayBtn)
        elif 'In4 All' in rxBuffer:
            ui.sourcesGroup.SetCurrent(ui.sourceSmdBtn)
        elif 'In5 All' in rxBuffer:
            ui.sourcesGroup.SetCurrent(ui.sourceAuxBtn)


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
def ProjectorSerialPortFeedbackHandler(interface, rcvString):

    rxBuffer = rcvString.decode()
    print(rxBuffer)


#screen
@event(ui.screenBtns, 'Pressed')
def screenBtnEvent(button, state):
    
    ui.screenGroup.SetCurrent(button)
    if button == ui.screenUpBtn:
        screenUp()
    elif button == ui.screenDownBtn:
        screenDown()
    elif button == ui.screenStopBtn:
        devices.ScreenDownRelay.Pulse(2)
        devices.ScreenUpRelay.Pulse(2)
        print("Relay 1 (Up) State: {0}".format(devices.ScreenUpRelay.State))
        print("Relay 2 (Down) State: {0}".format(devices.ScreenDownRelay.State))


#bluray
@event(ui.blurayBtns, 'Pressed')
def blurayBtnEvent(button, state):
    
    button.SetState(1)
    devices.BlurayIRPort.PlayContinuous(ui.blurayCmdMap[button])
    button.SetState(0)


#smd
@event(ui.smd202Btns, 'Pressed')
def smd202BtnEvent(button, state):
    
    devices.SMD202EthernetClient.Send(ui.smd202CmdMap[button])
    @Wait(0.5)
    def pollSMDPlaybackStatus():
        devices.SMD202EthernetClient.Send('WY1PLYR\r')


@event(devices.SMD202EthernetClient, 'ReceiveData')
def MainFeedbackHandler(interface, rcvString):

    rxBuffer = rcvString.decode()
    print(rxBuffer)
    if 'PlyrY1*0' in rxBuffer: #stop
        ui.smdPlaybackFb.SetCurrent(ui.smdStopBtn)
    elif 'PlyrY1*1' in rxBuffer: #play
        ui.smdPlaybackFb.SetCurrent(ui.smdPlayBtn)
    elif 'PlyrY1*2' in rxBuffer: #pause
        ui.smdPlaybackFb.SetCurrent(ui.smdPauseBtn)
    elif 'In1All' in rxBuffer:
        ui.smdHDMIBtn.SetState(0)
        ui.smdDecoderBtn.SetState(1)
    elif 'In2All' in rxBuffer:
        ui.smdDecoderBtn.SetState(0)
        ui.smdHDMIBtn.SetState(1)
    

@event(devices.SMD202EthernetClient, ui.connectionEvents)
def connectionEvent(interface, state):
    
    print('SMD 202 [{0}] {1}'.format(devices.SMD202EthernetClient.IPAddress, state))
    if state == 'Connected':
        devices.SMD202EthernetClient.StartKeepAlive(60, 'Q')
        devices.SMD202EthernetClient.Send('W3CV\r')
    elif state == 'Disconnected':
        devices.SMD202EthernetClient.StopKeepAlive()
    

##audio control
@event(ui.afvBtns, 'Pressed')
def afvBtnEvent(button, state):
    
    if button == ui.afvVolUpBtn:
        volumeUp(button, ui.afvLevel, devices.DMP44SerialPort, [-1000,0,100], '')
    elif button == ui.afvVolDownBtn:
        volumeDown(button, ui.afvLevel, devices.DMP44SerialPort, [-1000,0,100], '')
    elif button == ui.afvVolMuteBtn:
        if not ui.afvIsMuted:
            volumeMute(button, devices.DMP44SerialPort, 'WM30100*1AU\r')
        else:
            volumeUnmute(button, devices.DMP44SerialPort, 'WM30100*0AU\r')


#mic 1
@event(ui.mic1Btns, 'Pressed')
def mic1BtnEvent(button, state):
    
    if button == ui.mic1VolUpBtn:
        volumeUp(button, ui.mic1Level, devices.DMP44SerialPort, [-1000,0,100], '')
    elif button == ui.mic1VolDownBtn:
        volumeDown(button, ui.mic1Level, devices.DMP44SerialPort, [-1000,0,100], '')
    elif button == ui.mic1VolMuteBtn:
        if not ui.mic1IsMuted:
            volumeMute(button, devices.DMP44SerialPort, 'WM30101*1AU\r')
        else:
            volumeUnmute(button, devices.DMP44SerialPort, 'WM30101*0AU\r')


#mic 2
@event(ui.mic2Btns, 'Pressed')
def mic2BtnEvent(button, state):
    
    if button == ui.mic2VolUpBtn:
        volumeUp(button, ui.mic2Level, devices.DMP44SerialPort, [-1000,0,100], '')
    elif button == ui.mic2VolDownBtn:
        volumeDown(button, ui.mic2Level, devices.DMP44SerialPort, [-1000,0,100], '')
    elif button == ui.mic2VolMuteBtn:
        if not ui.mic2IsMuted:
            volumeMute(button, devices.DMP44SerialPort, 'WM30102*1AU\r')
        else:
            volumeUnmute(button, devices.DMP44SerialPort, 'WM30102*0AU\r')


## End Events Definitions-------------------------------------------------------

Initialize()
