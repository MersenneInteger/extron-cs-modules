## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait

from EventScheduler import *
## End ControlScript Import ----------------------------------------------------
##
## Begin User Import -----------------------------------------------------------
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
    pass
    
    
def shutdown():
    print('shutdown')


eventScheduler = EventScheduler()
shutdown_event_days = ['Monday','Tuesday','Wednesday','Thrusday','Friday', 'Sunday']

shutdown_event = eventScheduler.create_new_event('22', '00', shutdown_event_days, shutdown)
eventScheduler.add_event(shutdown_event)

for event in eventScheduler._events:
    print(event._hour, event._minute, event._days, event._function)
    
#eventScheduler.delete_event(shutdown_event)

#for event in eventScheduler._events:
#    print(event._hour, event._minute, event._days, event._function)

## Event Definitions -----------------------------------------------------------

## End Events Definitions-------------------------------------------------------

Initialize()
