# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(*cls.all_results.values(), sep='\n')

    def test_tournament1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        self.all_results['test_tournament1'] = tournament1.start()
        self.assertTrue(list(list(self.all_results.values())[-1].values())[-1] == self.runner3)

    def test_tournament2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        self.all_results['test_tournament2'] = tournament2.start()
        self.assertTrue(list(list(self.all_results.values())[-1].values())[-1] == self.runner3)

    def test_tournament3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results['test_tournament3'] = tournament3.start()
        self.assertTrue(list(list(self.all_results.values())[-1].values())[-1] == self.runner3)
        self.shortDescription()


if __name__ == '__main__':
    unittest.main()
