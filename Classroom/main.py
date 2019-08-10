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
import gui
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
    
    #ui.TLP_1022.ShowPage('Start')
    @Wait(15)
    def PrintHardwareInfo():
        print("{0}\n{1}\n{2}\n{3}",
            devices.IPCP_555_Pro.DeviceAlias,
            devices.IPCP_555_Pro.FirmwareVersion,
            devices.IPCP_555_Pro.Hostname,
            devices.IPCP_555_Pro.IPAddress)
            
        #print("{0}\n{1}\n{2}\n{3}", 
        #    ui.TLP_1022.DeviceAlias,
        #    ui.TLP_1022.FirmwareVersion,
        #    ui.TLP_1022.Hostname,
        #    ui.TLP_1022.IPAddress)
        
    #TLP_1022.SetWakeOnMotion('On')
    
    
def powerOnDisplay():
    pass
    
    
def powerOffDisplay():
    pass
    

def confirmShutdown():
    pass
    
    
def volumeUp(btn, level, device, lvlRange, cmd):
    pass
    
    
def volumeDown(btn, level, device, lvlRange, cmd):
    pass
    
    
def volumeMute(btn, device, cmd):
    pass
    

def volumeUnmute(btn, device, cmd):
    pass
    
## Event Definitions -----------------------------------------------------------

@event(gui.startBtn, 'Pressed')
def startBtnEvent(button, state):
    
    ui.TLP_1022.ShowPopup('Starting Up', 5)
    ui.TLP_1022.ShowPage('Main')
    
    
    
## End Events Definitions-------------------------------------------------------

Initialize()
