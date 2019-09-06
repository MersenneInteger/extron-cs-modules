## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait

'''
    The keyboard class requires a list of button objects to be passed in this
    exact order:
        a-z,0-9,-,.,*,@,#
'''

class Keyboard:
    
    def __init__(self, button_list, keyboard_label):
        
        self._keyboard_text = ''
        self._keyboard_label = keyboard_label
        self._key_map = {}
        keys = 'abcdefghijklmnopqrstuvwxyz0123456789-.*@#'
        self._key_map = dict(zip(button_list, keys))
        self._is_caps_locked = False
    
    
    def key_entered():
        pass
        
        
    def enter():
        pass
        
        
    def clear():
        pass
        
        
    def backspace():
        pass
        
        
    def shift():
        pass
        
        
    def caps_lock():
        
        self._is_caps_locked = not self._is_caps_locked
        
    
    