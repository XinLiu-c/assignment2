"""..."""


# Create your Place class in this file


class Place:
    """..."""
    def __int__(self,name="",country="",priority=0,visited_status=""):
        self.name=name
        self.country=country
        self.priority=priority
        self.visited_status=visited_status

    def __str__(self):
        return "{} ({}) with priority {} visited status: {}".format(self.name, self.country, self.priority,
                                                                    self.visited_status)



