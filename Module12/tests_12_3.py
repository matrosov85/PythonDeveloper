# Домашнее задание по теме "Систематизация и пропуск тестов"

import unittest
from module_12_2 import Runner, Tournament


def skip_test_if_frozen(func):
    def wrapper(self, *args):
        if not self.is_frozen:
            return func(self, *args)
        self.skipTest('Тесты в этом кейсе заморожены')
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_test_if_frozen
    def test_walk(self):
        runner = Runner('Forest')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_test_if_frozen
    def test_run(self):
        runner = Runner('Forest')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_test_if_frozen
    def test_challenge(self):
        runner1 = Runner('Forest')
        runner2 = Runner('Gump')
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @skip_test_if_frozen
    def test_tournament1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        self.all_results['test_tournament1'] = tournament1.start()
        self.assertTrue(list(list(self.all_results.values())[-1].values())[-1] == self.runner3)

    @skip_test_if_frozen
    def test_tournament2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        self.all_results['test_tournament2'] = tournament2.start()
        self.assertTrue(list(list(self.all_results.values())[-1].values())[-1] == self.runner3)

    @skip_test_if_frozen
    def test_tournament3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results['test_tournament3'] = tournament3.start()
        self.assertTrue(list(list(self.all_results.values())[-1].values())[-1] == self.runner3)
        self.shortDescription()
