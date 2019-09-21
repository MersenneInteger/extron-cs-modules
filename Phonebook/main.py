## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import *
from extronlib.ui import Button, Knob, Label, Level, Slider
from extronlib.system import Clock, MESet, Timer, Wait
from itertools import cycle
from time import sleep
## End ControlScript Import ----------------------------------------------------
##
## Begin User Import -----------------------------------------------------------
from phonebook import *
from keyboard import *
## End User Import -------------------------------------------------------------
##
## Begin Device/Processor Definition -------------------------------------------
Processor = ProcessorDevice('Processor')
TP = UIDevice('PanelAlias')
## End Device/Processor Definition ---------------------------------------------
##
## Begin Device/User Interface Definition --------------------------------------
kb_Q_btn = Button(TP, 34)
kb_W_btn = Button(TP, 35)
kb_E_btn = Button(TP, 36)
kb_R_btn = Button(TP, 37)
kb_T_btn = Button(TP, 38)
kb_Y_btn = Button(TP, 39)
kb_U_btn = Button(TP, 40)
kb_I_btn = Button(TP, 41)
kb_O_btn = Button(TP, 42)
kb_P_btn = Button(TP, 43)
kb_A_btn = Button(TP, 44)
kb_S_btn = Button(TP, 45)
kb_D_btn = Button(TP, 46)
kb_F_btn = Button(TP, 47)
kb_G_btn = Button(TP, 48)
kb_H_btn = Button(TP, 49)
kb_J_btn = Button(TP, 50)
kb_K_btn = Button(TP, 51)
kb_L_btn = Button(TP, 52)
kb_Z_btn = Button(TP, 53)
kb_X_btn = Button(TP, 54)
kb_C_btn = Button(TP, 55)
kb_V_btn = Button(TP, 56)
kb_B_btn = Button(TP, 57)
kb_N_btn = Button(TP, 58)
kb_M_btn = Button(TP, 59)
kb_1_btn = Button(TP, 24)
kb_2_btn = Button(TP, 25)
kb_3_btn = Button(TP, 26)
kb_4_btn = Button(TP, 27)
kb_5_btn = Button(TP, 29)
kb_6_btn = Button(TP, 60)
kb_7_btn = Button(TP, 63)
kb_8_btn = Button(TP, 64)
kb_9_btn = Button(TP, 65)
kb_0_btn = Button(TP, 66)
kb_shift_btn = Button(TP, 17)
kb_caps_btn = Button(TP, 18)
close_keyboard_btn = Button(TP, 19)
kb_star_btn = Button(TP, 20)
kb_dash_btn = Button(TP, 21)
kb_pound_btn = Button(TP, 22)
kb_atsign_btn = Button(TP, 23)
kb_space_btn = Button(TP, 28)
kb_comma_btn = Button(TP, 30)
kb_period_btn = Button(TP, 31)
search_keyword_btn = Button(TP, 33)
kb_backspace_btn = Button(TP, 118)
kb_text_label = Label(TP, 96)

kb_btn_list = [
    kb_A_btn,
    kb_B_btn,
    kb_C_btn,
    kb_D_btn,
    kb_E_btn,
    kb_F_btn,
    kb_G_btn,
    kb_H_btn,
    kb_I_btn,
    kb_J_btn,
    kb_K_btn,
    kb_L_btn,
    kb_M_btn,
    kb_N_btn,
    kb_O_btn,
    kb_P_btn,
    kb_Q_btn,
    kb_R_btn,
    kb_S_btn,
    kb_T_btn,
    kb_U_btn,
    kb_V_btn,
    kb_W_btn,
    kb_X_btn,
    kb_Y_btn,
    kb_Z_btn,
    kb_0_btn,
    kb_1_btn,
    kb_2_btn,
    kb_3_btn,
    kb_4_btn,
    kb_5_btn,
    kb_6_btn,
    kb_7_btn,
    kb_8_btn,
    kb_9_btn,
    kb_dash_btn,
    kb_period_btn,
    kb_star_btn,
    kb_atsign_btn,
    kb_pound_btn
]

contact_1_btn = Button(TP, 1)
contact_2_btn = Button(TP, 2)
contact_3_btn = Button(TP, 5)
contact_4_btn = Button(TP, 4)
contact_5_btn = Button(TP, 3)
contact_6_btn = Button(TP, 8)
contact_7_btn = Button(TP, 9)
contact_8_btn = Button(TP, 12)
contact_9_btn = Button(TP, 11)
contact_10_btn = Button(TP, 10)

contact_btn_list = [
    contact_1_btn,
    contact_2_btn,
    contact_3_btn,
    contact_4_btn,
    contact_5_btn,
    contact_6_btn,
    contact_7_btn,
    contact_8_btn,
    contact_9_btn,
    contact_10_btn
]

page_up_btn = Button(TP, 6)
page_down_btn = Button(TP, 7)
page_top_btn = Button(TP, 13)
dial_btn = Button(TP, 14)
search_popup_btn = Button(TP, 16)
selected_contact_label = Label(TP, 15)
loading_animation = Button(TP, 69)

kb = Keyboard(kb_btn_list, kb_text_label, kb_shift_btn, kb_caps_btn)
phonebook = Phonebook('contact_list.csv', contact_btn_list)
## End Device/User Interface Definition ----------------------------------------
##
## Begin Communication Interface Definition ------------------------------------

## End Communication Interface Definition --------------------------------------

def Initialize():
    
    TP.ShowPage('Page1')
    selected_contact_label.SetText('')
    
    @Wait(5)
    def init_phonebook_on_startup():
        #phonebook = Phonebook('contact_list.csv', contact_btn_list)
        show_loading()
        
        @Wait(1)
        def w0():
            print('first 10 contacts: ')
            phonebook.display_contacts()
            
            #@Wait(1)
            #def w1():
                #print('next page\n\n')
                #phonebook.page_up()
                #
                #@Wait(1)
                #def w2():
                    #print('last page\n\n')
                    #phonebook.page_up()
                    #
                    #@Wait(1)
                    #def w3():
                        #print('top page\n\n')
                        #phonebook.page_top()
                              
                              
def show_loading():
    
    TP.ShowPopup('Loading')
    animation_states = [0,1,2,3]
    for i,animatation in enumerate(cycle(animation_states)):
        loading_animation.SetState(animatation)
        if i > 12:
            break
        sleep(0.3)
    TP.HidePopup('Loading')

## Event Definitions -----------------------------------------------------------

@event(kb_btn_list, 'Pressed')
def kb_btn_listEvent(button, state):
    
    kb.key_entered(button)


@event(kb_backspace_btn, 'Pressed')
def kb_backspace_btn_event(button, state):
    
    kb.backspace()
    

@event(kb_shift_btn, 'Pressed')
def kb_shift_btn_event(button, state):
    
    kb.shift()
    

@event(kb_caps_btn, 'Pressed')
def kb_caps_btn_event(button, state):
    
    kb.caps_lock()
    
    
@event(kb_space_btn, 'Pressed')
def kb_space_btn_event(button, state):
    
    kb.space()


@event(contact_btn_list, 'Pressed')
def contact_btn_list_event(button, state):
    
    selected_contact_label.SetText(phonebook.select_contact(button))
    
    
@event(page_up_btn, 'Pressed')
def page_up_btn_event(button, state):
    
    phonebook.page_up()    
    
    
@event(page_down_btn, 'Pressed')
def page_down_btn_event(button, state):
    
    phonebook.page_down()   
    
    
@event(page_top_btn, 'Pressed')
def page_top_btn_event(button, state):
    
    phonebook.page_top()  
    
    
@event(dial_btn, 'Pressed')
def dial_btn_event(button, state):
    
    phonebook.dial_contact() 
    
    
@event(search_popup_btn, 'Pressed')
def search_popup_btn_event(button, state):
    
    TP.ShowPage('keyboard')   
    
    
@event(close_keyboard_btn, 'Pressed')
def close_keyboard_btn_event(button, state):
    
    TP.ShowPage('Page1')


## End Events Definitions-------------------------------------------------------

Initialize()
