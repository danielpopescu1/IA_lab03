import time
import random
import matplotlib.pyplot as plt
from utils.backtracking import rezolva_tsp_backtracking
from hill_climbing_tsp import rezolva_tsp_hc

def genereaza_instanta(n, seed=42):
    random.seed(seed)
    matrice = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = random.randint(1, 100)
            matrice[i][j] = matrice[j][i] = dist
    return matrice

def ruleaza_experiment():
    ns_bt = [5, 7, 8, 10, 12]
    ns_hc = [5, 7, 8, 10, 12, 15, 20, 30, 50]
    
    timpi_bt = []
    timpi_hc = []

    print("Incepere experiment...")
    
    for n in ns_bt:
        m = genereaza_instanta(n)
        start = time.perf_counter()
        rezolva_tsp_backtracking(n, m)
        timpi_bt.append(time.perf_counter() - start)

    for n in ns_hc:
        m = genereaza_instanta(n)
        start = time.perf_counter()
        rezolva_tsp_hc(n, m)
        timpi_hc.append(time.perf_counter() - start)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.plot(ns_bt, timpi_bt, 'o-', label='Backtracking')
    ax1.plot(ns_hc, timpi_hc, 's-', label='Hill Climbing')
    ax1.set_title('Timp de executie (Liniar)')
    ax1.set_xlabel('Numar orase (N)')
    ax1.set_ylabel('Secunde')
    ax1.legend()

    ax2.semilogy(ns_bt, timpi_bt, 'o-', label='Backtracking')
    ax2.semilogy(ns_hc, timpi_hc, 's-', label='Hill Climbing')
    ax2.set_title('Timp de executie (Logaritmic)')
    ax2.set_xlabel('Numar orase (N)')
    ax2.legend()

    plt.tight_layout()
    plt.savefig('comparare_performanta.png')
    print("Graficul a fost salvat ca 'comparare_performanta.png'.")
