from pyeasyga import pyeasyga

_POPULATION_SIZE = 200
_GENERATIONS = 500
global BAG

def fitness(individual, data):
    """
    Function, that we maximize
    """
    global BAG
    fitness = weight = volume = 0
    for i in range(len(individual)):
        weight += data[i][0] * individual[i]
        volume += data[i][1] * individual[i]
        fitness += data[i][2] * individual[i]
    
    if weight > BAG[0] or volume > BAG[1]:
        fitness = 0
    return fitness

def solve(bag, data):
    """
    Solve backpack problem with pyeasyga library
    https://github.com/remiomosowon/pyeasyga
    """
    global BAG 
    BAG = bag
    ga = pyeasyga.GeneticAlgorithm(
        data,
        population_size = _POPULATION_SIZE,
        generations = _GENERATIONS,
        maximise_fitness = True)
    ga.fitness_function = fitness
    ga.run()
    return ga.best_individual()[1]
