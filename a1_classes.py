"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class


from place import Place
from placecollection import PlaceCollection

def get_menu():
    """display menu"""
    choice = input("Menu\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\nYour choice:").upper()
    return choice

