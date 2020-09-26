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






