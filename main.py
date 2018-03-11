import QAP
import RandomSearch
import matplotlib.pyplot as plt
import numpy as np
# -------------------- BADANIE WPLYWU ROZMIARU POPULACJI -------------------------
# qap_pop10 = QAP.QAP(file="Had20.txt", use_tour=True, pop_size=10)
# avg_pop10 = qap_pop10.run()
#
# qap_pop200 = QAP.QAP(file="Had20.txt", use_tour=True, pop_size=200)
# avg_pop200 = qap_pop200.run()
#
# qap_pop1000 = QAP.QAP(file="Had20.txt", use_tour=True, pop_size=1000)
# avg_pop1000 = qap_pop1000.run()
#
# objects = ('10', '200', '1000')
# y_pos = np.arange(len(objects))
# performance = [avg_pop10, avg_pop200, avg_pop1000]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Wartość funkcji przystosowania')
# plt.xlabel('Rozmiar populacji')
# plt.title('Najlepsza wartość funkcji przystosowania względem rozmiaru populacji')
#
# plt.show()
# --------------------------------------------------------------------------------
# -------------------- BADANIE WPLYWU LICZBY POKOLEN -----------------------------
# qap_gen10 = QAP.QAP(file="Had20.txt", use_tour=True, gen=10)
# avg_gen10 = qap_gen10.run()
#
# qap_gen200 = QAP.QAP(file="Had20.txt", use_tour=True, gen=200)
# avg_gen200 = qap_gen200.run()
#
# qap_gen1000 = QAP.QAP(file="Had20.txt", use_tour=True, gen=1000)
# avg_gen1000 = qap_gen1000.run()
#
# objects = ('10', '200', '1000')
# y_pos = np.arange(len(objects))
# performance = [avg_gen10, avg_gen200, avg_gen1000]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Wartość funkcji przystosowania')
# plt.xlabel('Liczba pokoleń')
# plt.title('Najlepsza wartość funkcji przystosowania względem liczby pokoleń')
#
# plt.show()
# -----------------------------------------------------------------------------------
# -------------------- BADANIE WPLYWU ROZMIARU TURNIEJU -----------------------------
# qap_tour5 = QAP.QAP(file="Had20.txt", use_tour=True, tour=5)
# avg_tour5 = qap_tour5.run()
#
# qap_tour20 = QAP.QAP(file="Had20.txt", use_tour=True, tour=20)
# avg_tour20 = qap_tour20.run()
#
# qap_tour80 = QAP.QAP(file="Had20.txt", use_tour=True, tour=80)
# avg_tour80 = qap_tour80.run()
#
# objects = ('5', '20', '80')
# y_pos = np.arange(len(objects))
# performance = [avg_tour5, avg_tour20, avg_tour80]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Wartość funkcji przystosowania')
# plt.xlabel('Rozmiar turnieju')
# plt.title('Najlepsza wartość funkcji przystosowania względem rozmiaru turnieju')
#
# plt.show()
# -------------------------------------------------------------------------------------
# -------------------- BADANIE WPLYWU PRAWDPODOBIENSTWA KRZYŻOWANIA -------------------
# qap_cross01 = QAP.QAP(file="Had20.txt", use_tour=True, p_x=0.1)
# avg_cross01 = qap_cross01.run()
#
# qap_cross05 = QAP.QAP(file="Had20.txt", use_tour=True, p_x=0.5)
# avg_cross05 = qap_cross05.run()
#
# qap_cross09 = QAP.QAP(file="Had20.txt", use_tour=True, p_x=0.9)
# avg_cross09 = qap_cross09.run()
#
# objects = ('10%', '50%', '90%')
# y_pos = np.arange(len(objects))
# performance = [avg_cross01, avg_cross05, avg_cross09]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Wartość funkcji przystosowania')
# plt.xlabel('Prawdopodobieństwo krzyżowania')
# plt.title('Najlepsza wartość funkcji przystosowania względem prawdopodobieństwa krzyżowania')
#
# plt.show()
# -------------------------------------------------------------------------------------
# -------------------- BADANIE WPLYWU PRAWDPODOBIENSTWA MUTACJI -----------------------
# qap_mut001 = QAP.QAP(file="Had20.txt", use_tour=True, p_m=0.01)
# avg_mut001 = qap_mut001.run()
#
# qap_mut01 = QAP.QAP(file="Had20.txt", use_tour=True, p_m=0.1)
# avg_mut01 = qap_mut01.run()
#
# qap_mut08 = QAP.QAP(file="Had20.txt", use_tour=True, p_m=0.8)
# avg_mut08 = qap_mut08.run()
#
# objects = ('1%', '10%', '80%')
# y_pos = np.arange(len(objects))
# performance = [avg_mut001, avg_mut01, avg_mut08]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Wartość funkcji przystosowania')
# plt.xlabel('Prawdopodobieństwo mutacji')
# plt.title('Najlepsza wartość funkcji przystosowania względem prawdopodobieństwa mutacji')
#
# plt.show()
# -------------------------------------------------------------------------------------
# -------------------- PORÓWNANIE METODY RULETKI Z METODĄ TURNIEJU --------------------
# -------------------- Wykres dla metody ruletki --------------------------------------
# qap_roulette = QAP.QAP(file="Had20.txt")
# roulette_worst_history, roulette_avg_history, roulette_best_history, roulette_generations = qap_roulette.run_line_chart()
#
# builds = roulette_generations
# y_stack = np.row_stack((roulette_worst_history, roulette_avg_history, roulette_best_history))
#
# fig = plt.figure(figsize=(11, 8))
# ax1 = fig.add_subplot(111)
#
# ax1.plot(builds, y_stack[0,:], label='Najgorszy', color='c', marker='o')
# ax1.plot(builds, y_stack[1,:], label='Średni', color='g', marker='o')
# ax1.plot(builds, y_stack[2,:], label='Najlepszy', color='r', marker='o')
#
# plt.xticks(builds)
# plt.xlabel('Pokolenia')
# plt.ylabel('Wartość funkcji przystosowania')
# plt.title('Przebieg funkcji przystosowania przy selekcji metodą ruletki')
#
# handles, labels = ax1.get_legend_handles_labels()
# lgd = ax1.legend(handles, labels, loc='upper center', bbox_to_anchor=(1.15, 1))
# ax1.grid('on')
#
# plt.show()
# -------------------- Wykres dla metody turnieju --------------------------------------
# qap_tour = QAP.QAP(file="Had20.txt", use_tour=True, tour=80, p_m=0.1)
# tour_worst_history, tour_avg_history, tour_best_history, tour_generations = qap_tour.run_line_chart()
#
# builds = tour_generations
# y_stack = np.row_stack((tour_worst_history, tour_avg_history, tour_best_history))
#
# fig2 = plt.figure(figsize=(11, 8))
# ax2 = fig2.add_subplot(111)
#
# ax2.plot(builds, y_stack[0,:], label='Najgorszy', color='c', marker='o')
# ax2.plot(builds, y_stack[1,:], label='Średni', color='g', marker='o')
# ax2.plot(builds, y_stack[2,:], label='Najlepszy', color='r', marker='o')
#
# plt.xticks(builds)
# plt.xlabel('Pokolenia')
# plt.ylabel('Wartość funkcji przystosowania')
# plt.title('Przebieg funkcji przystosowania przy selekcji metodą turniejową')
#
# handles, labels = ax2.get_legend_handles_labels()
# lgd2 = ax2.legend(handles, labels, loc='upper center', bbox_to_anchor=(1.15, 1))
# ax2.grid('on')
#
# plt.show()
# --------------------------------------------------------------------------------------
# -------------------- BADANIE WPLYWU PRAWDPODOBIENSTWA MUTACJI -----------------------
# random_search = RandomSearch.RandomSearch(file="Had20.txt")
# avg_random_search = random_search.run()
#
# qap = QAP.QAP(file="Had20.txt", pop_size=200, gen=200, use_tour=True, tour=80, p_x=0.9, p_m=0.01)
# avg_qap = qap.run()
#
# objects = ('Random Search', 'Algorytm Genetyczny')
# y_pos = np.arange(len(objects))
# performance = [avg_random_search, avg_qap]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Wartość funkcji przystosowania')
# plt.xlabel('Algorytm')
# plt.title('Porównanie Algorytmu Genetycznego z Metodą Nieewolucyjną')
#
# plt.show()
# -------------------------------------------------------------------------------------

