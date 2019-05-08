class Hotel:
    distance_to_airport = 69.4

    def __init__(self, hotel_name="Name",
                 visitors_per_year=0,
                 number_of_rooms=0,
                 hotel_stars=0,
                 has_restaurant=False,
                 number_of_floors=0,
                 location="Adress"):
        self.hotel_name = hotel_name
        self.visitors_per_year = visitors_per_year
        self.number_of_rooms = number_of_rooms
        self.hotel_stars = hotel_stars
        self.has_restaurant = has_restaurant
        self.number_of_floors = number_of_floors
        self.location = location

    def __del__(self):
        print("Dracarys!  -->  ", self.hotel_name)

    def __str__(self):
        return self.hotel_name + ", " + str(self.visitors_per_year) + ", " \
               + str(self.number_of_rooms) + ", " + str(self.hotel_stars) + ", " \
               + str(self.has_restaurant) + ", " + str(self.number_of_floors) + ", " + str(self.location) + "."

    @staticmethod
    def distance_to_airport_func():
        return Hotel.distance_to_airport


def main():
    loombok_lodge_hotel = Hotel("The Loombok Longue", 7234, 200, 5, True, 5, "Tanjung")
    four_season_george_V_hotel = Hotel("Four Seasons Hotel George V Paris", 3356, 170, 5, True, 9, "Paris")
    brickell_key = Hotel("Brickell Key", 2345, 300, 5, True, 8, "Miami")

    print(loombok_lodge_hotel.__str__())
    print(four_season_george_V_hotel.__str__())
    print(brickell_key.__str__())
    print("Distance to airport: %s " % Hotel.distance_to_airport_func())


if __name__ == "__main__":
    main()
