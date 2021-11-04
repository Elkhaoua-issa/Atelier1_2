#fonction calcule la frequence d'un lettre
def frequence(chaine,L):
    n=len(chaine) #calculer length de liste
    count=0
    for i in range(0,n):
        if L==chaine[i]:
            count+=1
    return count

# Programme principale pour tester les Fonction
chaine=str(input("Entrez un text: "))
L=str(input("Entrez le caractere: "))
print(f"Votre chaine contient {frequence(chaine,L)}",L )
