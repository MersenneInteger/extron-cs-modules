## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait

## End ControlScript Import ----------------------------------------------------
##
## Begin User Import -----------------------------------------------------------

## End User Import -------------------------------------------------------------
##f
## Begin Device/Processor Definition -------------------------------------------

## End Device/Processor Definition ---------------------------------------------
##
## Begin Device/User Interface Definition --------------------------------------

TLP_1022 = UIDevice('TLP_1022_TP')

##definitions
startBtn = Button(TLP_1022, 8000)
systemOffBtn = Button(TLP_1022, 8022)
confirmShutdownBtn = Button(TLP_1022, 9028)
closeShutdownPopupBtn = Button(TLP_1022, 9029)
logoText = Label(TLP_1022, 7001)
roomText = Label(TLP_1022, 10000)

#popups
audioControlBtn = Button(TLP_1022, 8020)
closeAudioControlPopupBtn = Button(TLP_1022, 9027)
audioControlPopupBtns = [audioControlBtn, closeAudioControlPopupBtn]

lightingControlBtn = Button(TLP_1022, 8116)
closeLightingControlPopupBtn = Button(TLP_1022, 8238)
lightingControlPopupBtns = [lightingControlBtn, closeLightingControlPopupBtn]

helpBtn = Button(TLP_1022, 8117)
closeHelpPopupBtn = Button(TLP_1022, 9057)
helpPopupBtns = [helpBtn, closeHelpPopupBtn]

screenControlBtn = Button(TLP_1022, 8115)
closeScreenControlPopupBtn = Button(TLP_1022, 8253)
screenControlPopupBtns = [screenControlBtn, closeScreenControlPopupBtn]

splashLightingControlBtn = Button(TLP_1022, 8230)
closeLightingControlStartPopupBtn = Button(TLP_1022, 8237)
startLightingControlPopupBtns = [splashLightingControlBtn, closeLightingControlStartPopupBtn]

splashAudioControlBtn = Button(TLP_1022, 8260)
closeStartAudioControlPopupBtn = Button(TLP_1022, 8272)
startAudioControlPopupBtns = [splashAudioControlBtn, closeStartAudioControlPopupBtn]

#sources
sourceLaptopBtn = Button(TLP_1022, 8050)
sourcePCBtn = Button(TLP_1022, 8052)
sourceBlurayBtn = Button(TLP_1022, 8054)
sourceSmdBtn = Button(TLP_1022, 8058)
sourceAuxBtn = Button(TLP_1022, 8062)
displayOnBtn = Button(TLP_1022, 8112)
displayOffBtn = Button(TLP_1022, 8113)
displayMuteBtn = Button(TLP_1022, 8114)

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

lightingPreset1Btn = Button(TLP_1022, 8231)
lightingPreset2Btn = Button(TLP_1022, 8232)
lightingPreset3Btn = Button(TLP_1022, 8233)
lightingPreset4Btn = Button(TLP_1022, 8234)

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
afvLevel = Level(TLP_1022, 8023)
mic1Level = Level(TLP_1022, 9018)
mic2Level = Level(TLP_1022, 9022)

#button events
buttonEventList = ['Pressed', 'Released', 'Held', 'Repeated', 'Tapped']

##btn lists and dictionaries
#sources
sourceList = [
    sourceLaptopBtn,
    sourcePCBtn,
    sourceBlurayBtn,
    sourceSmdBtn,
    sourceAuxBtn
]

sourcesGroup = MESet(sourceList)

sourcePageFlipMap = {
    sourceLaptopBtn: 'Laptop',
    sourcePCBtn: 'PC',
    sourceBlurayBtn: 'Blu-ray',
    sourceSmdBtn: 'SMD 202',
    sourceAuxBtn: 'AUX'
}

sourceCmdMap = {
    sourceLaptopBtn: '1!',
    sourcePCBtn: '2!,
    sourceBlurayBtn: '3!',
    sourceSmdBtn: '4!',
    sourceAuxBtn: '5!'
}

##device btns

#display btns
displayBtns = [
    displayOnBtn,
    displayOffBtn,
    displayMuteBtn
]

displayGroup = MESet(displayBtns)

videoIsMuted = False

screenBtns = [
    screenUpBtn,
    screenDownBtn,
    screenStopBtn
]

screenGroup = MESet(screenBtns)

#bluray btns
blurayBtns = [
    blurayYellowBtn,
    blurayGreenBtn,
    blurayRedBtn,
    blurayBlueBtn,
    blurayPlayBtn,
    blurayStopBtn,
    blurayPauseBtn,
    blurayFastForwardBtn,
    blurayRewindBtn,
    blurayNextBtn,
    blurayPreviousBtn,
    blurayUpBtn,
    blurayDownBtn,
    blurayLeftBtn,
    blurayRightBtn,
    blurayEnterBtn,
    blurayMenuBtn,
    blurayTitleBtn
]

blurayCmdMap = {
    blurayYellowBtn: 'YELLOW',
    blurayGreenBtn: 'GREEN',
    blurayRedBtn: 'RED',
    blurayBlueBtn: 'BLUE',
    blurayPlayBtn: 'PLAY',
    blurayStopBtn: 'STOP',
    blurayPauseBtn: 'PAUSE',
    blurayFastForwardBtn: 'FFWD',
    blurayRewindBtn: 'REW',
    blurayNextBtn: 'FSTEP',
    blurayPreviousBtn: 'RSTEP',
    blurayUpBtn: 'UP',
    blurayDownBtn: 'DOWN',
    blurayLeftBtn: 'LEFT',
    blurayRightBtn: 'RIGHT',
    blurayEnterBtn: 'ENTER',
    blurayMenuBtn: 'MENU',
    blurayTitleBtn: 'TOP_MENU'
}

#lighting btns
lightingBtns = [
    lightingPreset1Btn,
    lightingPreset2Btn,
    lightingPreset3Btn,
    lightingPreset4Btn
]

lightingCmdMap = {
    lightingPreset1Btn: 'PRST01\r',
    lightingPreset2Btn: 'PRST02\r',
    lightingPreset3Btn: 'PRST03\r',
    lightingPreset4Btn: 'PRST04\r'
}

#SMD202 btns
smd202Btns = [
    smdPlayBtn,
    smdHDMIBtn,
    smdDecoderBtn,
    smdPauseBtn,
    smdStopBtn
]

smd202CmdMap = {
    smdPlayBtn: 'wS1*1PLYR\r',
    smdHDMIBtn: '2!',
    smdDecoderBtn: '1!',
    smdPauseBtn: 'wE1PLYR\r',
    smdStopBtn: 'wO1PLYR\r'
}

smdPlaybackFb = MESet([smdPlayBtn, smdPauseBtn, smdStopBtn])

##volume btns

#afv btns
afvBtns = [
    afvVolMuteBtn,
    afvVolUpBtn,
    afvVolDownBtn
]

#mic 1 btns
mic1Btns = [
    mic1VolUpBtn,
    mic1VolDownBtn,
    mic1VolMuteBtn
]

#mic 2 btns
mic2Btns = [
    mic2VolUpBtn,
    mic2VolDownBtn,
    mic2VolMuteBtn
]

afvIsMuted = False
mic1IsMuted = False
mic2IsMuted = False

## End Device/User Interface Definition ----------------------------------------
##
## Begin Communication Interface Definition ------------------------------------

## End Communication Interface Definition --------------------------------------

def Initialize():
    pass

## Event Definitions -----------------------------------------------------------

## End Events Definitions-------------------------------------------------------

Initialize()
