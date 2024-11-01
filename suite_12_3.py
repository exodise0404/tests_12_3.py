import unittest
import tests_12_3

run_tour = unittest.TestSuite()
run_tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test = unittest.TextTestRunner(verbosity=2)
test.run(run_tour)
