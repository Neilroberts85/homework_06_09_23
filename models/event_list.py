from models.event import Event

event1 = Event("24/05/23", "Wedding", 5, "The Wedding Room", "Unpopular Nuptuals", False)
event2 = Event("25/05/23", "Community Pot-luck", 20, "Mess", "Food Poisoning", True)
event3 = Event("26/05/23", "Pub quiz", 43, "Pub", "Banter", True)
event4 = Event("27/05/23", "Council Meeting", 200, "Chambers", "Mass brawl", False)

events = [event1, event2, event3, event4]

def add_new_event(event):
    events.append(event)