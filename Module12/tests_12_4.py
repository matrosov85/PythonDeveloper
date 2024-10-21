# Домашнее задание по теме "Логирование"

import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Вася', -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(2)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    unittest.main()
