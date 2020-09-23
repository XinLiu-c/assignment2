"""..."""
from operator import itemgetter
import csv
# Create your Place class in this file


class Place:
    """..."""
    def __int__(self,name="",country="",priority=0,visited_status=""):
        self.name=name
        self.country=country
        self.priority=priority
        self.visited_status=visited_status

    def __str__(self):
        return "{} ({}) with priority {} visited status: {}".format(self.name, self.country, self.priority,self.visited_status)

    def mark_places(self):
        list_data = []  # empty list
        filename = "places.csv"
        input_file = open(filename, 'r')
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            list_data.append(parts)
        input_file.close()
        list_data.sort(key=itemgetter(3))  # sort data according to "n" and "v"
        list_data.sort(key=itemgetter(2), reverse=True)  # sort data according to the priority number
        count = 1
        for list in list_data:
            if list[3] == "n":
                print("*{}. {:9} in {:12} priority {:2}".format(count, list[0], list[1], list[2]))
                count += 1
            else:
                print(" {}. {:9} in {:12} priority {:2}".format(count, list[0], list[1], list[2]))
                count += 1
        return list_data





