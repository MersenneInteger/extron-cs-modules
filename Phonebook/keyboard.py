## Begin ControlScript Import --------------------------------------------------
from extronlib.system import Wait, ProgramLog
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
        print(self._key_map)
        self._is_caps_locked = False
        self._is_shift_on = False
        self._shift_btn = shift_btn
        self._caps_lock_btn = caps_lock_btn


    def key_entered(self, btn):

        try:
            if self._is_caps_locked or self._is_shift_on:
                self._keyboard_text += self._key_map[btn].upper()
                self._is_shift_on = False
                if self._shift_btn != None:
                    self._shift_btn.SetState(0)
            else:
                self._keyboard_text += self._key_map[btn]
            self._keyboard_label.SetText(self._keyboard_text)
        except Exception as e:
            ProgramLog('Error occured entering key in Keyboard: {0}'.format(e))
        
        
    def clear(self):
    
        self._keyboard_text = ''
        self._keyboard_label.SetText(self._keyboard_text)
        
        
    def backspace(self):
        
        if len(self._keyboard_text) > 0:
            self._keyboard_text = self._keyboard_text[:len(self._keyboard_text)-1]
            self._keyboard_label.SetText(self._keyboard_text)
        
        
    def shift(self):
        
        self._is_shift_on = True
        if self._shift_btn != None:
            self._shift_btn.SetState(1)
        
        
    def caps_lock(self):
        
        self._is_caps_locked = not self._is_caps_locked
        if self._caps_lock_btn != None:
            self._caps_lock_btn.SetState(self._is_caps_locked)
        
        
    def space(self):
    
        self._keyboard_text += ' '
        self._keyboard_label.SetText(self._keyboard_text)
    
    