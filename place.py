"""..."""
from operator import itemgetter
# Create your Place class in this file


class Place:
    """initialise place"""
    def __int__(self,name="",country="",priority=0,visited_status=""):
        self.name=name
        self.country=country
        self.priority=priority
        self.visited_status=visited_status

    """return string of place object"""
    def __str__(self):
        return "{} ({}) with priority {} visited status: {}".format(self.name, self.country, self.priority,self.visited_status)

    """return visited places"""
    def mark_vplaces(self):
        self.visited_status="v"
        return self.visited_status

    """return unvisited places"""
    def mark_nplaces(self):
        self.visited_status="n"
        return self.visited_status

    """determine important places """
    def is_important(self):
        if self.priority <= 2:
            return True
        else:
            return False




