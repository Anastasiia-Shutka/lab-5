"""
module
"""


class RaceHorse:
    """
    class
    """
    def __init__(self, name, speed, age):
        self.name = name
        self.speed = speed
        self.age = age
        self.place_in_race = None

    def __str__(self):
        return f"{self.name}: Speed - {self.speed},\
         Age - {self.age}, Place in Race - {self.place_in_race}"


class Race:
    """
    class
    """
    def __init__(self):
        self.participants = []

    def add_horse(self, horse):
        """
        add horse
        """
        if 3 <= horse.age <= 7:
            self.participants.append(horse)

    def remove_horse(self, horse):
        """
        remove
        """
        if horse in self.participants:
            self.participants.remove(horse)

    def race(self):
        """
        race
        """
        if not self.participants:
            print("No horses in the race.")
            return

        sorted_horses = sorted(self.participants, key=lambda x: x.speed, reverse=True)

        total_age = sum(horse.age for horse in self.participants)
        average_age = total_age / len(self.participants)

        winner = max(sorted_horses, key=lambda x: x.speed + abs(x.age - average_age))

        places = [1, 2, 3]
        for i in range(3):
            sorted_horses[i].place_in_race = places[i]

        print("Race Results:")
        for horse in sorted_horses:
            print(horse)

        print(f"\nWinner: {winner.name}, Speed: {winner.speed}, Age: {winner.age}")


if __name__ == "__main__":
    horse1 = RaceHorse("Donny", 34, 7)
    horse2 = RaceHorse("Frank", 22, 5)
    horse3 = RaceHorse("Blaze", 31, 6)
    horse4 = RaceHorse("Swift", 27, 3)
    horse5 = RaceHorse("Flash", 38, 4)

    race = Race()
    race.add_horse(horse1)
    race.add_horse(horse2)
    race.add_horse(horse3)
    race.add_horse(horse4)
    race.add_horse(horse5)

    print("Initial Race Participants:")
    for horse in race.participants:
        print(horse)

    race.race()
