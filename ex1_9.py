#fonction cherche la position d'un element dans un matrice
def chercher_element(M,R):
    #creer une liste pour stocker tout les position d'element dans la matrice
    liste=[]
    # le variable tmp est boolean sert a verifier si l'element qui va le donner l'utilisateur trouve dans matrice 
    tmp=False
    n=len(M)
    T=len(M[0])
    for i in range(0,n):
        for j in range(0,T):
            if M[i][j] == R:
                liste.append([i+1,j+1])
                tmp=True
    if tmp==True:
        print(f"la position de {R} dans la matrice est comme suit: {liste}")
    else:
        print(f"{R} ne trouve pas dans matrice")


# Programme principale pour tester les Fonction
# la saisie matricielle de l'utilisateur
  
L = int(input("Entrez le nombre de lignes:"))
C = int(input("Entrez le nombre de colonnes:"))
  
# Initialize Matrice
Matrice = []
print("Entrez les valeurs par ligne:")
  
# pour l'utilisateur
for i in range(L):          # Une boucle pour les entrées de ligne
    a =[]
    for j in range(C):      # Une boucle pour les entrées de colonnes
         a.append(int(input()))
    Matrice.append(a)
R=int(input("chercher: "))
chercher_element(Matrice,R)