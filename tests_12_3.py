import unittest

class Runner1:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 10

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тест пройден")
    def test_walk(self):
        obj1 = Runner1('Объект1')
        for i in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 100)

    @unittest.skipIf(is_frozen, "Тест пройден")
    def test_run(self):
        obj2 = Runner1('Объект2')
        for i in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    @unittest.skipIf(is_frozen, "Тест пройден")
    def test_challenge(self):
        obj3 = Runner1('Объект3')
        obj4 = Runner1('Объект4')
        for i in range(10):
            obj3.run()
            obj4.walk()
        self.assertEqual(obj3.distance, obj4.distance)

if __name__ == "__main__":
    unittest.main()

class Runner2:
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

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner2):
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
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.obj1 = Runner2('Усэйн', 10)
        self.obj2 = Runner2('Андрей', 9)
        self.obj3 = Runner2('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run1(self):
        dist1 = Tournament(90, self.obj1, self.obj3)
        results = dist1.start()
        self.all_results[max(results.keys())] = results
        self.assertEqual(results[2], self.obj3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run2(self):
        dist2 = Tournament(90, self.obj2, self.obj3)
        results = dist2.start()
        self.all_results[max(results.keys())] = results
        self.assertEqual(results[2], self.obj3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run3(self):
        dist3 = Tournament(90, self.obj1, self.obj2, self.obj3)
        results = dist3.start()
        self.all_results[max(results.keys())] = results
        self.assertEqual(results[3], self.obj3)


if __name__ == "__main__":
    unittest.main()