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

    def create_widgets(self,key="visited"):
        """add btn or other functions to app"""
        self.count_n()
        self.place_collection.s_places(key)

        for places in self.place_collection.list_data:
            if places[3]=="n":
                v=""
            else:
                v="(visited)"
            place_str="{} ({}) with priority {} {}".format(places[0],places[1],places[2],v)
            btn = Button(id=places[0], text=place_str)
            self.root.ids.places_listed.add_widget(btn)

    def on_stop(self):
        """save csv file"""
        self.place_collection.s_places("places.csv")

    def count_n(self):
        n_place=self.place_collection.count_n()
        self.root.ids.count_n.text="Places to visit: {}".format(n_place)

if __name__ == '__main__':
    TravelTrackerApp().run()
