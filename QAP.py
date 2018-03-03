import math
import random

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
        self.distance_matrix = None if file != None else np.array(
            [[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
        self.cost_matrix = None if file != None else np.array(
            [[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
        self.cur_pop = None
        self.evaluated_pop = None
        self.selected_pop = None
        self.min_fitness = None
        self.max_fitness = math.inf
        self.evaluation_sum = 0
        self.new_pop = np.array([])
        self.sum_of_probabilities = 0.0
        self.pop_probabilities = np.array([])
        pass

    def initialize(self):
        start_pop = np.array([np.array([1, 2, 3, 4, 5]) for i in range(100)])
        for i in start_pop:
            np.random.shuffle(i)
        self.cur_pop = start_pop
        # print(start_pop)

    def evaluate(self, chromosome):
        return sum(sum(self.distance_matrix[i] * self.cost_matrix[chromosome[i] - 1] for i in range(5)))

    def evaluation(self):
        self.evaluated_pop = np.array([self.evaluate(i) for i in self.cur_pop])
        self.max_fitness = np.amin(self.evaluated_pop) if np.amin(
            self.evaluated_pop) < self.max_fitness else self.max_fitness
        self.min_fitness = np.amax(self.evaluated_pop)
        self.evaluation_sum = sum(self.evaluated_pop)
        print("Najgorszy: " + str(self.min_fitness) + " Najlepszy: " + str(self.max_fitness))

    def roulette_prob(self, cur_fitness):
        return (self.min_fitness - cur_fitness) / self.evaluation_sum

    def selection(self, tour=False):
        self.new_pop = np.empty((0, 5), int)
        self.pop_probabilities = np.array([])
        self.sum_of_probabilities = 0.0
        for j in self.evaluated_pop:
            probability = self.sum_of_probabilities + self.roulette_prob(j)
            self.pop_probabilities = np.append(self.pop_probabilities, probability)
            self.sum_of_probabilities += probability
        print(self.pop_probabilities)
        if tour:
            # UZUPELNIC SELEKCJĘ TURNIEJOWĄ
            return
        else:
            print(self.evaluated_pop)
            # print(self.pop_probabilities)
            for k in range(100):
                r = random.uniform(self.pop_probabilities[0], self.pop_probabilities[99])
                for i, obj in enumerate(self.pop_probabilities):
                    if obj < r < self.pop_probabilities[i + 1] and i < 100:
                        self.new_pop = np.append(self.new_pop, np.array([self.cur_pop[i]]), axis=0)
                        break
            # print(self.new_pop)
            #TEST
            # self.evaluated_pop = np.array([self.evaluate(i) for i in self.new_pop])
            print(np.array([self.evaluate(i) for i in self.new_pop]))
            print("Najlepsi: " + str(sum(self.evaluate(i) == self.max_fitness for i in self.new_pop)) + "\nNajgorsi: " + str(sum(
                self.evaluate(i) == self.min_fitness for i in self.new_pop)) + "\nLiczba wartoścl: " + str(len(np.unique(self.new_pop))))

    # def ox_crossover(self):
    # OPERATOR KRZYZOWANIA OX
    # def crossover(self):

    # def mutation(self):
