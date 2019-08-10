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
from main import TLP_1022
## End User Import -------------------------------------------------------------
##f
## Begin Device/Processor Definition -------------------------------------------

## End Device/Processor Definition ---------------------------------------------
##
## Begin Device/User Interface Definition --------------------------------------
startBtn = Button(TLP_1022, 8000)

splashLightingControlBtn = Button(TLP_1022, 8230)
splashAudioControlBtn = Button(TLP_1022, 8260)
logoText = Label(TLP_1022, 7001)
roomText = Label(TLP_1022, 10000)
audioControlBtn = Button(TLP_1022, 8020)
systemOffBtn = Button(TLP_1022, 8022)
lightingControlBtn = Button(TLP_1022, 8116)
helpBtn = Button(TLP_1022, 8117)
closeHelpPopup = Button(TLP_1022, 9057)
confirmShutdownBtn = Button(TLP_1022, 9028)
closeShutdownPopup = Button(TLP_1022, 9029)

sourceLaptopBtn = Button(TLP_1022, 8050)
sourcePCBtn = Button(TLP_1022, 8052)
sourceBlurayBtn = Button(TLP_1022, 8054)
sourceSmdBtn = Button(TLP_1022, 8058)
sourceAuxBtn = Button(TLP_1022, 8062)
displayOnBtn = Button(TLP_1022, 8112)
displayOffBtn = Button(TLP_1022, 8113)
displayMuteBtn = Button(TLP_1022, 8114)
screenControlBtn = Button(TLP_1022, 8115)

blurayYellowBtn = Button(TLP_1022, 20)
blurayGreenBtn = Button(TLP_1022, 21)
blurayRedBtn = Button(TLP_1022, 22)
blurayBlueBtn = Button(TLP_1022, 23)
blurayPlayBtn = Button(TLP_1022, 5000)
blurayStopBtn = Button(TLP_1022, 5001)
blurayPauseBtn = Button(TLP_1022, 5002)
blurayFastForwardBtn = Button(TLP_1022, 5003)
blurayRewindBtn = Button(TLP_1022, 5004)
blurayNextBtn = Button(TLP_1022, 5005)
blurayPreviousBtn = Button(TLP_1022, 5006)
blurayUpBtn = Button(TLP_1022, 5007)
blurayDownBtn = Button(TLP_1022, 5008)
blurayLeftBtn = Button(TLP_1022, 5009)
blurayRightBtn = Button(TLP_1022, 5010)
blurayEnterBtn = Button(TLP_1022, 5011)
blurayMenuBtn = Button(TLP_1022, 5012)
blurayTitleBtn = Button(TLP_1022, 5013)

screenUpBtn = Button(TLP_1022, 8241)
screenDownBtn = Button(TLP_1022, 8242)
screenStopBtn = Button(TLP_1022, 8243)
closeScreenControlPopup = Button(TLP_1022, 8253)

lightingPreset1Btn = Button(TLP_1022, 8231)
lightingPreset2Btn = Button(TLP_1022, 8232)
lightingPreset3Btn = Button(TLP_1022, 8233)
lightingPreset4Btn = Button(TLP_1022, 8234)
closeLightingControlPopup = Button(TLP_1022, 8238)
closeLightingControlStartPopup = Button(TLP_1022, 8237)

smdPlayBtn = Button(TLP_1022, 2)
smdHDMIBtn = Button(TLP_1022, 3)
smdDecoderBtn = Button(TLP_1022, 4)
smdPauseBtn = Button(TLP_1022, 5)
smdStopBtn = Button(TLP_1022, 7)
smdTimeText = Label(TLP_1022, 6)
smdPlayerStateText = Label(TLP_1022, 8)

afvVolMuteBtn = Button(TLP_1022, 8021)
afvVolUpBtn = Button(TLP_1022, 8120)
afvVolDownBtn = Button(TLP_1022, 8121)
mic1VolUpBtn = Button(TLP_1022, 9015)
mic1VolDownBtn = Button(TLP_1022, 9016)
mic1VolMuteBtn = Button(TLP_1022, 9017)
mic2VolUpBtn = Button(TLP_1022, 9019)
mic2VolDownBtn = Button(TLP_1022, 9020)
mic2VolMuteBtn = Button(TLP_1022, 9021)
closeAudioControlPopup = Button(TLP_1022, 9027)
afvLevel = Level(TLP_1022, 8023)
mic1Level = Level(TLP_1022, 9018)
mic2Level = Level(TLP_1022, 9022)


## End Device/User Interface Definition ----------------------------------------
##
## Begin Communication Interface Definition ------------------------------------

## End Communication Interface Definition --------------------------------------

def Initialize():
    pass

## Event Definitions -----------------------------------------------------------

## End Events Definitions-------------------------------------------------------

Initialize()
