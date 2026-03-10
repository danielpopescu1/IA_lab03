import sys

def citeste_matrice(cale_fisier):
    """Citeste matricea de distante dintr-un fisier text.

    Args:
        cale_fisier: Calea catre fisierul .txt.

    Returns:
        tuple: (n, matrice) unde n este int si matrice este list[list[int]].
    """
    try:
        with open(cale_fisier, 'r') as f:
            linii = [linie.strip() for linie in f if linie.strip()]
        if not linii:
            return 0, []
        n = int(linii[0])
        matrice = [[int(x) for x in linii[i + 1].split()] for i in range(n)]
        return n, matrice
    except (FileNotFoundError, ValueError, IndexError) as e:
        print(f"Eroare la citirea fisierului: {e}")
        return 0, []

def afiseaza_rezultat(metoda, traseu, cost, durata):
    """Afiseaza formatat rezultatul unui algoritm."""
    print(f"\n--- Rezultat {metoda} ---")
    if traseu:
        sir_traseu = " -> ".join(map(str, traseu)) + f" -> {traseu[0]}"
        print(f"Traseu: {sir_traseu}")
        print(f"Cost:   {cost}")
    print(f"Timp:   {durata:.6f} secunde")
