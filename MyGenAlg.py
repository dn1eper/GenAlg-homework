from random import randint
from genetic import Genetic

_POPULATION_SIZE = 200
_GENERATIONS = 500
_CROSS  = 0.2
_MUTATE = 0.05
_CONVERGENCE = 0.1

class MyGenAlg(Genetic):
    def solve(self, 
        generations = _GENERATIONS, 
        population_size = _POPULATION_SIZE, 
        cross = _CROSS, 
        mutate = _MUTATE, 
        convergence = _CONVERGENCE):
        """
        Solve backpack problem with my genetic algorithm
        """
        p = self._population(len(self.data), population_size)
        for generation in range(generations):
            p = self._evolve(population = p, mutate = mutate, cross = cross)
            if self._isconvergence(p[0], convergence):
                break
            self.best_fitness = self.fitness(p[0])
        return p[0]
    
    def _evolve(self, population, mutate, cross):
        """
        Create new generation based on previous
        """
        # compute fitness function for each individ
        graded = [ (self.fitness(individ), individ) for individ in population]
        # sort individ by fitness function result
        graded = [ individ[1] for individ in sorted(graded, reverse=True)]
        # crossing best % of individuals
        new_generation = self._cross(graded[:int(len(population)*cross)])
        # adding best % of individuals from prev population
        new_generation =  graded[:(len(population)-len(new_generation))] + new_generation
        # mutate some of individuals
        new_generation = self._mutate(new_generation, mutate)
        return new_generation

    def _individual(self, length):
        """
        Create a random member of the population
        """
        return [ randint(0, 1) for i in range(length) ]

    def _population(self, length, size):
        """
        Create a number of individuals
        """
        return [ self._individual(length) for i in range(size) ]

    def _cross(self, p):
        """
        Crossing individuals in :p, every two individuals spawn the other two.
        Method - multipoint crossover (3 points)
        """
        for i in range(0, len(p), 2):
            # find random points for crossover
            points = []
            while len(points) < 3:
                point = randint(0, len(p[0])-1)
                if point not in points:
                    points.append(point)
            # crossing
            tmp1, tmp2 = p[i][:points[0]], p[i][points[1]:points[2]]
            p[i][:points[0]], p[i][points[1]:points[2]] = p[i+1][:points[0]], p[i+1][points[1]:points[2]]
            p[i+1][:points[0]], p[i+1][points[1]:points[2]] = tmp1, tmp2
        return p

    def _mutate(self, p, percent, bit = 3):
        """
        Mutate :percent of individuals in :p (random change :bit of bits) 
        """
        individuals = [randint(0, len(p)-1) for i in range(int(len(p) * percent))]
        bits = [randint(0, len(p[0])-1) for i in range(bit)]
        for i in individuals:
            for j in bits:
                p[i][j] = 1 - p[i][j]
        return p

    def _isconvergence(self, individ, percent):
        """
        Check if convergence has come
        """
        fitness = self.fitness(individ)
        return percent and self.best_fitness and fitness and 1 - fitness / self.best_fitness < percent
            
