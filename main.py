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

    def build(self):
        """build app"""
        self.title="Travel Tracker"
        self.root=Builder.load_file("app.kv")
        return self.root

    def add_place(self):
        """add places"""
        add_name=self.root.ids.add_name.text
        add_country=self.root.ids.add_country.text
        add_priority=self.root.ids.add_priority.text

        if add_name.strip()== "" or add_country.strip()=="" or add_priority=="":
            end="Cannot be blank!"
        else:
            if int(add_priority)<=0:
                end="priority must greater than 0 !"
            else:
                end="{} ({}) with priority {}.".format(add_name,add_country,add_priority)
                self.place_collection.list_data.append([add_name,add_country,add_priority],"n")
        self.root.ids.end.text = end



if __name__ == '__main__':
    TravelTrackerApp().run()
