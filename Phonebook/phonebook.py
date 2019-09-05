## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait


class Phonebook:
    
   def __init__(self):
    
        self._contacts = {} 
        
    
    def read_file(self, file_name):
        pass
        
        
    def write_file(self, file_name):
        pass
        
    
    def add_contact(self):
        pass
        
        
    def delete_contact(self):
        pass
        
        
    def save_contact(self):
        pass
        
        
    def edit_contact(self):
        pass
        
        
    def search_contact(self, keyword):
        pass
        
    
    def sort_contacts(self):
        pass
        
    
    def dial_contact(self, contact):
        pass
        
    
    def page_up(self):
        pass
        
        
    def page_down(self):
        pass
        
        
    def page_top(self):
        pass
    
    
