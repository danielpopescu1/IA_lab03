
"""Punctul de intrare in aplicatie."""

import sys
import time
from utils.io_utils import citeste_matrice, afiseaza_rezultat
from utils.backtracking import rezolva_tsp_backtracking
from hill_climbing_tsp import rezolva_tsp_hc
from utils.performance import ruleaza_experiment

def main():
    # Verificam daca user-ul a trimis suficiente argumente
    if len(sys.argv) < 2:
        print("Utilizare incorecta. Foloseste unul dintre formatele:")
        print("  python main.py <cale_fisier_intrare>")
        print("  python main.py experiment")
        sys.exit(1)

    comanda = sys.argv[1]

    # Rularea experimentului cu matplotlib (Sarcina C)
    if comanda == "experiment":
        ruleaza_experiment()
    
    # Rularea standard pe un fisier de input dat (ex: orase.txt)
    else:
        n, matrice = citeste_matrice(comanda)
        if n == 0:
            sys.exit(1)

        print(f"S-au citit cu succes {n} orase din '{comanda}'.\n")

        # --- Executie Backtracking ---
        start_bt = time.perf_counter()
        traseu_bt, cost_bt = rezolva_tsp_backtracking(n, matrice)
        durata_bt = time.perf_counter() - start_bt
        afiseaza_rezultat("Backtracking (solutie optima)", traseu_bt, cost_bt, durata_bt)

        # --- Executie Hill Climbing ---
        start_hc = time.perf_counter()
        # Setam un numar moderat de reporniri pentru a echilibra precizia cu viteza
        traseu_hc, cost_hc = rezolva_tsp_hc(n, matrice, reporniri=20) 
        durata_hc = time.perf_counter() - start_hc
        afiseaza_rezultat("Hill Climbing (aprox. 20 reporniri)", traseu_hc, cost_hc, durata_hc)

if __name__ == "__main__":
    main()