import QAP
import numpy as np
qap = QAP.QAP()
qap.initialize()
# qap.evaluate([3, 5, 2, 1, 4])
qap.evaluation()
qap.selection()
qap.crossover()
qap.mutation()
