from extronlib.ui import Button, Label
from extronlib.system import Clock, MESet, Timer, Wait
import datetime


class Events:
    
    def __init__(self, hour, minute, days, function):
        
        self._hour = hour
        self._minute = minute
        self._days = days
        self._function = function
        
        
class EventScheduler:
    
    def __init__(self):
        
        self._events = []
        self.poll_events()
    
    
    def create_new_event(self, hour, minute, days, function):
    
        event = Events(hour, minute, days, function)
        return event
        
        
    def add_event(self, event):
        
        if event != None:
            self._events.append(event)
        
    
    def delete_event(self, event):
    
        if event in self._events:
            self._events.remove(event)
    
    
    #@staticmethod
    def poll_events(self):
        
        date = datetime.datetime.now()
        hour = date.strftime('%H')
        minute = date.strftime('%M')
        day = date.strftime('%A')
        
        for event in self._events:
            if event._hour == hour \
                and event._minute == minute \
                and day in event._days:
                event._function()
        
        Wait(31.0, self.poll_events)
        

