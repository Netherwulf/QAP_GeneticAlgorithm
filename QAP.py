import math
import random

import numpy as np


class QAP(object):

    def __init__(self, file=None, pop_size=100, gen=100, p_x=0.7, p_m=0.1, tour=5, use_tour=False):
        self.pop_size = pop_size
        self.gen = gen
        self.p_x = p_x
        self.p_m = p_m
        self.tour = tour
        self.use_tour = use_tour
        self.counter = 0
        self.best_fit = math.inf
        self.n = None if file is not None else 5
        self.distance_matrix = None if file is not None else np.array(
            [[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
        self.cost_matrix = None if file is not None else np.array(
            [[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
        self.cur_pop = None
        self.evaluated_pop = None
        self.selected_pop = None
        self.min_fitness = None
        self.max_fitness = math.inf
        self.evaluation_difference_sum = 0
        self.new_pop = None
        self.sum_of_probabilities = 0.0
        self.pop_probabilities = np.array([])
        pass

    def initialize(self):
        start_pop = np.array([np.array([1, 2, 3, 4, 5]) for i in range(self.pop_size)])
        for i in start_pop:
            np.random.shuffle(i)
        self.cur_pop = start_pop
        # print(start_pop)

    def evaluate(self, chromosome):
        return sum(sum(self.distance_matrix[i] * self.cost_matrix[chromosome[i] - 1] for i in range(self.n)))

    def evaluation(self):
        self.evaluated_pop = np.array([self.evaluate(i) for i in self.cur_pop])
        self.max_fitness = np.amin(self.evaluated_pop) if np.amin(
            self.evaluated_pop) < self.max_fitness else self.max_fitness
        self.min_fitness = np.amax(self.evaluated_pop)
        self.evaluation_difference_sum = sum(self.min_fitness - self.evaluated_pop)
        # print("Najgorszy: " + str(self.min_fitness) + " Najlepszy: " + str(self.max_fitness))

    def roulette_prob(self, cur_fitness):
        return (self.min_fitness - cur_fitness) / self.evaluation_difference_sum

    def selection(self):
        self.selected_pop = np.empty((0, self.n), int)
        if self.use_tour:
            # UZUPELNIC SELEKCJĘ TURNIEJOWĄ
            tour_members = np.empty((0, self.n), int)
            while len(tour_members) < self.tour:
                chromosome = self.cur_pop[random.randint(0, self.pop_size-1)]
                if chromosome not in tour_members:
                    tour_members = np.append(tour_members, np.array([chromosome]), axis=0)
            evaluated_tour_members = np.array([self.evaluate(i) for i in tour_members])
            print(tour_members)
            print(evaluated_tour_members)
            #TO NIE DZIALA
            print(np.argmin(evaluated_tour_members))
        else:
            # print(self.evaluated_pop)
            # print(self.pop_probabilities)
            self.pop_probabilities = np.array([])
            self.sum_of_probabilities = 0.0
            for j in self.evaluated_pop:
                probability = self.sum_of_probabilities + self.roulette_prob(j)
                self.pop_probabilities = np.append(self.pop_probabilities, probability)
                self.sum_of_probabilities += self.roulette_prob(j)
            for i, obj in enumerate(self.pop_probabilities):
                if obj >= random.random():
                    # print(i)
                    self.selected_pop = np.append(self.selected_pop, np.array([self.cur_pop[i]]), axis=0)
            # print(self.new_pop)
            # TEST
            # self.evaluated_pop = np.array([self.evaluate(i) for i in self.new_pop])
            print(np.array([self.evaluate(i) for i in self.selected_pop]))
            print("Najlepsi: " + str(
                sum(self.evaluate(i) == self.max_fitness for i in self.selected_pop)) + "\nNajgorsi: " + str(sum(
                self.evaluate(i) == self.min_fitness for i in self.selected_pop)) + "\nLiczba wartoścl: " + str(
                len(np.unique(np.array([self.evaluate(i) for i in self.selected_pop])))))

    def ox_crossover(self, parent_a, parent_b):
        a = random.randint(1, len(parent_a) - 3)
        b = random.randint(a + 1, len(parent_a) - 2)

        child_a = np.zeros(self.n, int)
        child_b = np.zeros(self.n, int)

        # wstrzyknięcie fragmentu genotypu drugiego rodzica
        for i in range(a, b + 1):
            np.put(np.asarray(child_a), i, parent_b[i])
            np.put(np.asarray(child_b), i, parent_a[i])

        # uzupełnienie genów
        for j in range(len(parent_a) - (b - a)):
            repairing_index = b + j + 1
            if repairing_index > (len(parent_a) - 1):
                repairing_index = (repairing_index % len(parent_a)) - 1

            # uzupełnianie genów child_a
            for k in range(len(parent_a)):
                parent_index = repairing_index + k
                if parent_index > (len(parent_a) - 1):
                    parent_index = (parent_index % len(parent_a))
                if not np.asarray(parent_a)[parent_index] in np.asarray(child_a):
                    np.put(child_a, repairing_index, parent_a[parent_index])
                    break

            # uzupełnianie genów child_b
            for l in range(len(parent_b)):
                parent_index = repairing_index + l
                if parent_index > (len(parent_b) - 1):
                    parent_index = (parent_index % len(parent_b))
                if not np.asarray(parent_b)[parent_index] in child_b:
                    np.put(child_b, repairing_index, parent_b[parent_index])
                    break
        # print(str(b-a) + " " + str(a) + " " + str(b))
        # print(np.array([child_a, child_b]))
        return child_a, child_b

    def crossover(self):
        self.new_pop = np.array([])
        parent_1 = None
        for i in self.selected_pop:
            if np.random.random() <= self.p_x:
                if parent_1 is not None:
                    child_1, child_2 = self.ox_crossover(parent_1, i)
                    self.new_pop = np.append(self.new_pop, child_1, axis=0)
                    self.new_pop = np.append(self.new_pop, child_2, axis=0)
                    parent_1 = None
                else:
                    parent_1 = i
        self.new_pop = np.reshape(self.new_pop, [int(len(self.new_pop) / self.n), self.n])
        # print("Ilość osobników: " + str(len(self.new_pop)))
        # print("Wymiary: " + str(self.new_pop.shape))
        # print(self.cur_pop)
        # uzupełnienie brakujących osobników w populacji
        while len(self.new_pop) < self.pop_size:
            self.new_pop = np.append(self.new_pop, np.array([self.cur_pop[np.random.randint(0, self.pop_size)]]),
                                     axis=0)

        # uznanie nowej generacji jako obecnej
        self.new_pop = self.new_pop.astype(int)
        self.cur_pop = np.copy(self.new_pop)
        self.new_pop = None

    def mutation(self):
        for chromosome in self.cur_pop:
            for i, gene in enumerate(chromosome):
                if np.random.rand() <= self.p_m:
                    chromosome[[i, np.random.randint(0, len(chromosome))]] = chromosome[
                        [np.random.randint(0, len(chromosome)), i]]
        print(self.cur_pop)
