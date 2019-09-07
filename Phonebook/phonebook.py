## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait, File, ProgramLog

import csv

class Phonebook:
    
    def __init__(self, file_name):
    
        self._first_names = []
        self._last_names = []
        self._phone_nums = []
        self._contacts = {}
        self._file_name = '/user/' + file_name
        self._csv_reader = None
        self.read_file(self._file_name)
        
    
    def build_contacts(self, contact_info):
    
        for i in range(len(contact_info)):
            self._first_names.append(contact_info[i]['first_name'])
            self._last_names.append(contact_info[i]['last_name'])
            self._phone_nums.append(contact_info[i]['phone_number'])
            
        for i in range(len(contact_info)):
            contact = 'contact' + str(i+1)
            self._contacts[contact] = [self._first_names[i], self._last_names[i], self._phone_nums[i]]
    
    
    def read_file(self, file_name):

        try:
            with File(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                rows = list(csv_reader)
            if rows != []:
                build_contacts(rows)
        except Exception as e:
            ProgramLog('File not found: {0}\n{1}'.format(file_name, e))
        

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
    
    