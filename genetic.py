class Genetic:
    def __init__(self, bag, data):
        self.bag = bag
        self.data = data
        self.best_fitness = False

    def fitness(self, individ, data=[]):
        """
        Function, that we maximize
        """
        fitness = weight = volume = 0
        for i in range(len(individ)):
            weight += self.data[i][0] * individ[i]
            volume += self.data[i][1] * individ[i]
            fitness += self.data[i][2] * individ[i]
        
        if weight > self.bag[0] or volume > self.bag[1]:
            fitness = 0
        return fitness

    def solve(self, generations, population_size):
        """
        You should override this method when you subclass Genetic
        """
        raise NotImplementedError
