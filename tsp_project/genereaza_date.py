import random

def genereaza_fisier_tsp(n, nume_fisier):
    random.seed(42) # Seed fix pentru ca matricea sa fie la fel de fiecare data
    matrice = [[0]*n for _ in range(n)]
    
    # Generam o matrice simetrica cu diagonala 0
    for i in range(n):
        for j in range(i+1, n):
            dist = random.randint(1, 100)
            matrice[i][j] = matrice[j][i] = dist
            
    # Scriem in fisier conform formatului cerut
    with open(nume_fisier, 'w') as f:
        f.write(f"{n}\n")
        for rand in matrice:
            f.write(" ".join(str(x) for x in rand) + "\n")
            
    print(f"Fisierul '{nume_fisier}' cu N={n} orase a fost generat cu succes!")

if __name__ == "__main__":
    # Poti schimba numerele de aici pentru a testa diverse limite
    genereaza_fisier_tsp(13, "orase_13.txt")
    genereaza_fisier_tsp(14, "orase_14.txt")
    genereaza_fisier_tsp(15, "orase_15.txt")