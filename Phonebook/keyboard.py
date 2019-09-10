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

    def __init__(self, button_list, keyboard_label, shift_btn=None, caps_lock_btn=None):
        
        self._keyboard_text = ''
        self._keyboard_label = keyboard_label
        self._key_map = {}
        keys = 'abcdefghijklmnopqrstuvwxyz0123456789-.*@#'
        self._key_map = dict(zip(button_list, keys))
        self._is_caps_locked = False
        self._is_shift_on = False
        self._shift_btn = shift_btn
        self._caps_lock_btn = caps_lock_btn


    def key_entered(button):

        if self._is_caps_locked or self._is_shift_on:
            self._keyboard_text = upper(self._key_map[button])
            self._is_shift_on = False
            if self._shift_btn != None:
                self._shift_btn.SetState(0)
        else:
            self._keyboard_text = self._key_map[button]
        self._keyboard_label = self._keyboard_text
        
        
    def clear():
    
        self._keyboard_text = ''
        self._keyboard_label = self._keyboard_text
        
        
    def backspace():
        
        if len(self._keyboard_text) > 0:
            self._keyboard_text = self._keyboard_text[:len(self._keyboard_text)-1]
            self._keyboard_label = self._keyboard_text
        
        
    def shift():
        
        self._is_shift_on = True
        if self._shift_btn != None:
            self._shift_btn.SetState(1)
        
        
    def caps_lock():
        
        self._is_caps_locked = not self._is_caps_locked
        if self._caps_lock_btn != None:
            self._caps_lock_btn.SetState(self._is_caps_locked)
        
    
    