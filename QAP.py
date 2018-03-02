import math
import numpy as np


class QAP(object):

    def __init__(self, file=None, pop_size=100, gen=100, p_x=0.7, p_m=0.01, tour=5):
        self.pop_size = pop_size
        self.gen = gen
        self.p_x = p_x
        self.p_m = p_m
        self.tour = tour
        self.counter = 0
        self.best_fit = math.inf
        self.n = None if file != None else 5
        self.distance_matrix = None if file != None else np.array([[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
        self.cost_matrix = None if file != None else np.array([[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
        self.cur_pop = None
        self.evaluated_pop = None
        self.selected_pop = None
        # self.old_pop
        pass

    def initialize(self):
        start_pop = np.array([np.array([1, 2, 3, 4, 5]) for i in range(100)])
        for i in start_pop:
            np.random.shuffle(i)
        self.cur_pop = start_pop
        # print(start_pop)

    def evaluate(self, chromosome):
        return sum(sum(self.distance_matrix[i] * self.cost_matrix[chromosome[i]-1] for i in range(5)))

    def evaluation(self):
        self.evaluated_pop = np.array([self.evaluate(i) for i in self.cur_pop])

    def roulette_prob(self):
        return # UZUPELNIC OBLICZANIE PRAWDOPODOBIENSTWA RULETKA

    def selection(self, tour = False):
        if tour:
            # UZUPELNIC SELEKCJĘ TURNIEJOWĄ
            return
        else:
            return # UZUPELLNIC WYKORZYSTUJAC roulette_prob dla każdego

    #def ox_crossover(self):
        #OPERATOR KRZYZOWANIA OX
    #def crossover(self):

    #def mutation(self):



