"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    """Test empty PlaceCollection (defaults)"""
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.list_data  # an empty list is considered False

    """Test loading places"""
    print("Test loading places:")
    place_collection.read_places('places.csv')
    print(place_collection)
    assert place_collection.list_data  # assuming CSV file is non-empty, non-empty list is considered True

    """Test adding a new Place with values"""
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    """Test sorting - name:"""
    print("Test sorting - name:")
    place_collection.s_places("name")
    print(place_collection)

    """Test sorting - country:"""
    print("Test sorting - country:")
    place_collection.s_places("country")
    print(place_collection)

    """Test sorting places - priority"""
    print("Test sorting - priority:")
    place_collection.s_places("priority")
    print(place_collection)

    """Test sorting places - visited_status"""
    print("Test sorting - visited:")
    place_collection.s_places("visited")
    print(place_collection)

    """Test listing places"""
    print("Test listing:")
    place_collection.list_all_places()

run_tests()
