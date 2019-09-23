## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait, File, ProgramLog

import csv

'''
class Contact:
    
    def __init__(self):
        pass
'''

class Phonebook:
    
    def __init__(self, file_name, contact_btns, selected_contact_label, display_size=10):
    
        self._first_names = []
        self._last_names = []
        self._phone_nums = []
        self._contacts = {}
        self._file_name = file_name
        self._csv_reader = None
        self._num_of_contacts = 0
        self._current_page = 1
        self._contact_btns = contact_btns
        self._contacts_on_display = []
        self._contact_selected = 0
        self._selected_contact_label = selected_contact_label
        self.read_file(self._file_name)
        self._total_pages = self._num_of_contacts // display_size + 1
        
    
    def build_contacts(self, contact_info):
    
        for i in range(len(contact_info)):
            self._first_names.append(contact_info[i]['first_name'])
            self._last_names.append(contact_info[i]['last_name'])
            self._phone_nums.append(contact_info[i]['phone_number'])
            self._num_of_contacts += 1
            contact = 'contact' + str(i+1)
            self._contacts[contact] = [self._first_names[i], self._last_names[i], self._phone_nums[i]]
            print(self._contacts[contact])
        self.display_contacts()
        
        
    def read_file(self, file_name):

        try:
            if File.Exists(file_name):
                with File(file_name, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    rows = list(csv_reader)
                if rows != []:
                    print('len of rows: {0}'.format(len(rows)))
                    self.build_contacts(rows)
            else:
                ProgramLog('File not found: {0}'.format(file_name))
        except Exception as e:
            ProgramLog('Error occured opening file: {0}\n{1}'.format(file_name, e))


    def write_file(self, file_name):
        
        data_to_write = 'first_name,last_name,phone_number\n'
        with File(file_name, 'w') as csv_file:
            for i in range(0, self._num_of_contacts):
                data_to_write += '{0},{1},{2}\n'.format(
                    self._first_names[i], 
                    self._last_names[i], 
                    self._phone_nums[i])
            csv_file.write(data_to_write)


    def add_contact(self, first_name, last_name, phone_number):
        
        self._first_names.append(first_name)
        self._last_names.append(last_name)
        self._phone_nums.append(phone_number)
        self._num_of_contacts += 1
        contact = 'contact'+ self._num_of_contacts
        self._contacts[contact] = [first_name, last_name, phone_number]
        write_file(self._file_name)
        read_file(self._file_name)
        

    def delete_contact(self, contact_selected):
        pass


    def edit_contact(self, contact_selected):
        pass


    def search_contact(self, keyword):
        pass


    def sort_contacts(self):
        pass


    def select_contact(self, contact_selected):
        
        self._contact_selected = self._contact_btns.index(contact_selected) \
            + 1 + ((self._current_page-1) * 10)
        contact = 'contact' + str(self._contact_selected)
        for btn in self._contact_btns:
            btn.SetState(0)
        self._contact_btns[self._contact_btns.index(contact_selected)].SetState(1)
        if contact in self._contacts:
            self._selected_contact_label.SetText(self._contacts[contact][0] \
                + ' ' + self._contacts[contact][1])
        else:
            self._selected_contact_label.SetText('')


    def dial_contact(self):
        
        if self._contact_selected > 0:
            contact = 'contact' + str(self._contact_selected)
            return self._contacts[contact][2]


    def display_contacts(self):

        max_contacts_on_display = 10
        start = (self._current_page - 1) * max_contacts_on_display
        end = start + max_contacts_on_display
        self._contacts_on_display = []
        
        try:
            for i in range(start, end):
                if i+1 > self._num_of_contacts:
                    break
                contact = 'contact' + str(i+1)
                self._contacts_on_display.append(self._contacts[contact])
                #print(self._contacts_on_display)
                
            for i in range(len(self._contact_btns)):
                if i < len(self._contacts_on_display):
                    self._contact_btns[i].SetText(self._contacts_on_display[i][0] \
                        + ' ' + self._contacts_on_display[i][1])
                else:
                    self._contact_btns[i].SetText('')
                
        except KeyError as e:
            ProgramLog('KeyError occured displaying contacts: {0}'.format(e))
        except Exception as e:
            ProgramLog('Error displaying contacts: {0}'.format(e))


    def clear_contacts(self):
    
        for btn in self._contact_btns:
            btn.SetState(0)
        self._contact_selected = 0
        self._selected_contact_label.SetText('')


    def page_up(self):
        
        if self._current_page < self._total_pages:
            self._current_page += 1
            self.clear_contacts()
            self.display_contacts()


    def page_down(self):

        if self._current_page > 1:
            self._current_page -= 1
            self.clear_contacts()
            self.display_contacts()


    def page_top(self):
        
        if self._current_page > 1:
            self._current_page = 1
            self.clear_contacts()
            self.display_contacts()

