def rezolva_tsp_backtracking(n, matrice):
    """Punct de intrare pentru algoritmul Backtracking.
    
    Returns:
        tuple: (traseu_optim, cost_minim)
    """
    if n == 0: return [], 0
    
    # State object pentru a evita variabilele globale
    state = {
        'cost_minim': float('inf'),
        'traseu_optim': []
    }

    def backtrack(oras_curent, vizitat, traseu, cost_acumulat):
        if len(traseu) == n:
            cost_total = cost_acumulat + matrice[oras_curent][traseu[0]]
            if cost_total < state['cost_minim']:
                state['cost_minim'] = cost_total
                state['traseu_optim'] = traseu[:]
            return

        for urmator in range(n):
            if not vizitat[urmator]:
                nou_cost = cost_acumulat + matrice[oras_curent][urmator]
                # Prunere Branch and Bound
                if nou_cost < state['cost_minim']:
                    vizitat[urmator] = True
                    traseu.append(urmator)
                    backtrack(urmator, vizitat, traseu, nou_cost)
                    traseu.pop()
                    vizitat[urmator] = False

    vizitat = [False] * n
    vizitat[0] = True
    backtrack(0, vizitat, [0], 0)
    
    return state['traseu_optim'], state['cost_minim']
