from pyeasyga import pyeasyga
from genetic import Genetic

_POPULATION_SIZE = 200
_GENERATIONS = 5

class GenAlg(Genetic):
    def solve(self, generations = _GENERATIONS, population_size = _POPULATION_SIZE):
        """
        Solve backpack problem with pyeasyga genetic library
        https://github.com/remiomosowon/pyeasyga
        """
        ga = pyeasyga.GeneticAlgorithm(
            self.data,
            population_size = population_size,
            generations = generations,
            maximise_fitness = True)
        ga.fitness_function = self.fitness
        ga.run()
        return ga.best_individual()[1]
