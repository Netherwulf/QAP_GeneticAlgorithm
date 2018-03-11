import numpy as np
import time


class RandomSearch(object):

    def __init__(self, file=None):
        if file is not None:
            with open(file) as fp:
                for i, line in enumerate(fp):
                    if i == 0:
                        self.n = int(line[2:])
                        self.cost_matrix = np.empty((0, self.n), int)
                        self.distance_matrix = np.empty((0, self.n), int)
                    elif 1 < i < self.n + 2:
                        # wczytanie macierzy przepływu
                        self.distance_matrix = np.append(self.distance_matrix, [list(map(int, line[2:].split('  ')))],
                                                         axis=0)
                    elif self.n + 2 < i < (2 * self.n) + 3:
                        # wczytanie macierzy odległości
                        self.cost_matrix = np.append(self.cost_matrix, [list(map(int, line[2:].split('  ')))], axis=0)
                    if i == (2 * self.n) + 3:
                        break
        if file is None:
            self.n = 5
            self.distance_matrix = np.array(
            [[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
            self.cost_matrix = np.array(
            [[0, 4, 5, 1, 4], [1, 0, 5, 6, 7], [4, 6, 0, 1, 5], [3, 6, 7, 0, 2], [4, 6, 2, 5, 0]])
        self.cur_configuration = None
        self.evaluated_configuration = None
        self.best_history = np.array([])
        pass

    def initialize(self):
        start_configuration = np.arange(1, self.n+1)
        np.random.shuffle(start_configuration)
        # print(start_configuration)
        self.cur_configuration = start_configuration

    def evaluate(self):
        self.evaluated_configuration = sum(sum(self.distance_matrix[i] * self.cost_matrix[self.cur_configuration[i] - 1] for i in range(self.n)))+70
        self.best_history = np.append(self.best_history, self.evaluated_configuration)

    def run(self):
        times = np.array([])
        for j in range(10):
            start_time = time.time()
            self.initialize()
            self.evaluate()
            times = np.append(times, time.time() - start_time)
        print("Średnie najlepsze przystosowanie: " + str(np.average(self.best_history)))
        print("Średni czas obliczeń: " + str(np.average(times)))
        return np.average(self.best_history)
