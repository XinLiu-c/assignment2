"""..."""

from operator import itemgetter
import csv
# Create your PlaceCollection class in this file


class PlaceCollection:

    def __init__(self):
        self.list_data = []

    def __str__(self):
        after_place = ''
        for prev_place in self.list_data:
            for i in prev_place[:-1]:
                after_place += str(i) + ','
            after_place = after_place + '\n'

        return after_place


    def read_places(self, filename):
        """Return a list of unvisited and visited places"""
        """Read file, and add data"""
        try:
            with open(filename, 'r') as in_file:
                places_listed = in_file.readlines()
                for prev_place in places_listed:
                    prev_place=prev_place.strip().split(',')
                    self.list_data.append(prev_place)
                for i in self.list_data:
                    i[2] = int(i[2])
        except IOError:
            print('File is not be found.')

        return self.list_data

