import random
from abc import ABC
class Airport:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.planes = []

    def __str__(self):
        return "Airport Code: " + self.code + ", Name: " + self.name

    def addPlane(self, plane):
        self.planes.append(plane)

    def removePlane(self, plane):
        self.planes.remove(plane)

    def getPlanes(self):
        for plane in self.planes:
            plane.getInfo()


class Airplane:
    def __init__(self, type, company):
        self.type = type
        self.company = company
        self.code = str(round(random.random() * 10000))
        self.pilot = None
        self.passenger = None

    def __str__(self):
        return self.company

    def assignPilot(self, pilot):
        self.pilot = pilot

    def assignPassenger(self, passenger):
        self.passenger = passenger

    def getInfo(self):
        print(self.company + " " + self.type + " Code: " + self.code)
        if self.pilot:
            print("Pilot: ", end="")
            self.pilot.getInfo()
        if self.passenger:
            print("Passenger: ", end="")
            self.passenger.getInfo()


class Clovek(ABC):
    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __str__(self):
        return self.name + " " + self.surname

    def getInfo(self):
        print(self.name + " " + self.surname + " " + self.birth_date)


class Pilot(Clovek):
    def __init__(self, name, surname, birth_date, planeType, isCaptain):
        super().__init__(name, surname, birth_date)
        self.planeType = planeType
        self.isCaptain = isCaptain

    def getInfo(self):
        role = "Captain" if self.isCaptain else "Co-Pilot"
        print(role + ": " + self.name + " " + self.surname + " " + self.birth_date + ", Qualified for: " + self.planeType)


class Passenger(Clovek):
    def __init__(self, name, surname, birth_date, seat_number):
        super().__init__(name, surname, birth_date)
        self.seat_number = seat_number

    def getInfo(self):
        print(self.name + " " + self.surname + " " + self.birth_date + " Seat: " + self.seat_number)


def flight_manager_fixed(airport1, airport2):
    if len(airport1.planes) > 1:
        plane_to_transfer = airport1.planes[1]
        airport1.removePlane(plane_to_transfer)
        airport2.addPlane(plane_to_transfer)


if __name__ == '__main__':
    letisko = Airport("18946132", "Toni")
    plane1 = Airplane("Krajta Královská", "Maďar Airlines")
    plane2 = Airplane("Krajta Tmavá", "Čobolák Airlines")

    letisko.addPlane(plane1)
    letisko.addPlane(plane2)

    letisko2 = Airport("684513", "Random Airlines")
    plane3 = Airplane("Heterodon Nasicus", "Marshmellow Airlines")
    plane4 = Airplane("Boa Constrictor", "Honzík Airlines")

    letisko2.addPlane(plane3)
    letisko2.addPlane(plane4)

    pilots = [
        Pilot("Jan", "Novák", "1985-03-14", "Krajta Královská", True),
        Pilot("Pavel", "Svoboda", "1990-06-20", "Krajta Tmavá", True),
        Pilot("Lucie", "Veselá", "1983-01-05", "Heterodon Nasicus", True),
        Pilot("Martin", "Horák", "1987-08-12", "Boa Constrictor", True)
    ]

    plane1.assignPilot(pilots[0])
    plane2.assignPilot(pilots[1])
    plane3.assignPilot(pilots[2])
    plane4.assignPilot(pilots[3])

    passengers = [
        Passenger("Anna", "Dvořáková", "1995-04-25", "12A"),
        Passenger("Karel", "Nový", "1988-11-10", "14C"),
        Passenger("Eva", "Malá", "2000-07-05", "15D"),
        Passenger("Tomáš", "Krátký", "1993-02-19", "16B")
    ]

    plane1.assignPassenger(passengers[0])
    plane2.assignPassenger(passengers[1])
    plane3.assignPassenger(passengers[2])
    plane4.assignPassenger(passengers[3])

    flight_manager_fixed(letisko, letisko2)

    letisko.getPlanes()
    letisko2.getPlanes()
