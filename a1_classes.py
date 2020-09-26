"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class


from place import Place
from placecollection import PlaceCollection

def get_menu():
    """display menu"""
    choice = input("Menu\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\nYour choice:").upper()
    return choice

def mark_places(place_collection, list_data):
    """list with visited and unvisited places"""
    a = place_collection.count_n()
    if a == 0:
        print("No unvisited places")
    else:
        place_collection.list_data()
        print("Enter the number of a place to mark as visited")

        while True:
            m_place = input('Please enter the name of city which you want to mark:')
            if m_place.strip() == " ":
                print("Cannot be blank")
            elif m_place.isdigit() == "False":
                print("Invalid. Please enter a valid number:")
            elif int(m_place) < 0:
                print("Number must be > 0")
            elif int(m_place) > len(list_data):
                print("Invalid place number")
            elif list_data[int(m_place)-1][3] == "v":
                print("Place is already visited")
            else:
                list_data[int(m_place)-1][3] = "n"
                break
        return list_data

    def main():
        """Run the whole process"""
        print("Travel Tracker 1.0 - by Xin Liu")
        place_collection = PlaceCollection()
        listed_places = place_collection.read_places("places.csv")

        while True:
            choice = get_menu()
            if choice == "L":
                place_collection.list_data
            elif choice == "A":
                add_places = add_place()
                place_collection.add_place(Place(add_places[0], add_places[1], add_places[2], add_places[3]))
            elif choice == "M":
                mark_places(place_collection, listed_places)

            elif choice == "Q":
                print("{} places saved to places.csv".format(len(place_collection.list_data)))
                break
            else:
                print("Invalid menu choice")


    if __name__ == '__main__':
        main()