## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait

## Begin Communication Interface Definition ------------------------------------
IPCP_555_Pro = ProcessorDevice('IPCP_555_Processor')
    
#serial devices
DMP44SerialPort = SerialInterface(IPCP_555_Pro, 'COM1', Baud=9600)
ProjectorSerialPort = SerialInterface(IPCP_555_Pro, 'COM2', Baud=9600)
MPS602SerialPort = SerialInterface(IPCP_555_Pro, 'COM3', Baud=9600)

#ir devices
BlurayIRPort = IRInterface(IPCP_555_Pro, 'IRS1', 'sony_3_6638_1_eap.eir')
LightingIRPort = SerialInterface(IPCP_555_Pro, 'IRS2', Baud=9600)

#ethernet devices
SMD202EthernetClient = EthernetClientInterface('0.0.0.0', 23)

#relays
ScreenUpRelay = RelayInterface(IPCP_555_Pro, 'RLY1')
ScreenDownRelay = RelayInterface(IPCP_555_Pro, 'RLY2')
ScreenStopRelay = RelayInterface(IPCP_555_Pro, 'RLY3')
   
## End Communication Interface Definition --------------------------------------

def Initialize():
    pass

## Event Definitions -----------------------------------------------------------
## End Events Definitions-------------------------------------------------------

Initialize()
