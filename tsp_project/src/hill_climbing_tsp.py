"""Modul pentru rezolvarea TSP folosind Hill Climbing (simpleai)."""

import random
from simpleai.search import SearchProblem, hill_climbing_random_restarts

class TSPHillClimbing(SearchProblem):
    """Clasa care modeleaza problema TSP pentru simpleai folosind vecinatatea 2-opt."""

    def __init__(self, n, matrice):
        """Initializare problema.
        
        Args:
            n (int): Numarul de orase.
            matrice (list[list[int]]): Matricea de distante.
        """
        self.n = n
        self.matrice = matrice
        
        # Starea initiala: o permutare aleatoare a oraselor.
        # Se foloseste tuple deoarece simpleai necesita stari imutabile (hashable).
        stare_initiala = list(range(n))
        random.shuffle(stare_initiala)
        super().__init__(initial_state=tuple(stare_initiala))

    def generate_random_state(self):
        """Genereaza o stare aleatoare pentru repornirile algoritmului."""
        stare = list(range(self.n))
        random.shuffle(stare)
        return tuple(stare)
    
    def actions(self, state):
        """Genereaza vecinii folosind vecinatatea 2-opt.
        
        O actiune este definita de indicii (i, j) ai segmentului ce va fi inversat.
        
        Args:
            state (tuple): Starea curenta (traseul).
            
        Returns:
            list[tuple]: Lista de actiuni posibile (perechi de indici).
        """
        actiuni = []
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                # Evitam inversarea intregului tur (care da acelasi tur, doar parcurs invers)
                if i == 0 and j == self.n - 1:
                    continue
                actiuni.append((i, j))
        return actiuni

    def result(self, state, action):
        """Aplica actiunea 2-opt pe starea curenta.
        
        Args:
            state (tuple): Starea curenta.
            action (tuple): Actiunea de aplicat (i, j).
            
        Returns:
            tuple: Noua stare generata dupa inversarea segmentului.
        """
        i, j = action
        # Inversam secventa de la indicele i la j inclusiv
        noua_stare = state[:i] + state[i:j+1][::-1] + state[j+1:]
        return tuple(noua_stare)

    def value(self, state):
        """Evalueaza starea curenta.
        
        Deoarece simpleai maximizeaza functia value, iar noi vrem sa minimizam 
        costul traseului, vom returna valoarea negativa a costului.
        
        Args:
            state (tuple): Traseul curent.
            
        Returns:
            int: Valoarea starii (-costul total).
        """
        cost = 0
        for i in range(self.n - 1):
            cost += self.matrice[state[i]][state[i+1]]
        # Adaugam si costul de intoarcere la orasul de start
        cost += self.matrice[state[-1]][state[0]]
        return -cost

def rezolva_tsp_hc(n, matrice, reporniri=15):
    """Punct de intrare pentru rezolvarea TSP cu Hill Climbing Random Restarts.

    Args:
        n (int): Numarul de orase.
        matrice (list[list[int]]): Matricea de distante.
        reporniri (int): De cate ori va reporni algoritmul pentru a evita optimii locali.

    Returns:
        tuple: (traseu_optim, cost_minim)
    """
    if n <= 1:
        return [0] if n == 1 else [], 0

    problema = TSPHillClimbing(n, matrice)
    rezultat = hill_climbing_random_restarts(problema, restarts_limit=reporniri)

    # Convertim costul negativ inapoi in valoare pozitiva
    cost_minim = -problema.value(rezultat.state)
    traseu_opt = list(rezultat.state)

    # Optimizare: Aliniem traseul ca sa inceapa mereu de la orasul 0 
    # pentru a fi usor comparabil cu rezultatul de la Backtracking.
    idx_zero = traseu_opt.index(0)
    traseu_opt = traseu_opt[idx_zero:] + traseu_opt[:idx_zero]

    return traseu_opt, cost_minim