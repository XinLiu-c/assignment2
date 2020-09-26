"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from placecollection import PlaceCollection
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.properties import StringProperty


states={"Name":0,"Country":1,"Priority":2,"Visited":3}
class TravelTrackerApp(App):
    states=ListProperty()
    current_state=StringProperty()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.read_places('places.csv')



if __name__ == '__main__':
    TravelTrackerApp().run()
