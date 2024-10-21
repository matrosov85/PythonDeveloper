# Домашнее задание по теме "Систематизация и пропуск тестов"

import unittest
from tests_12_3 import RunnerTest, TournamentTest


runnersTS = unittest.TestSuite()
runnersTS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnersTS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnersTS)
