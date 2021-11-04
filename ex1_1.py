#fonction de facteur
def Qfacteur(a):
    f=1
    #calculer factoriel
    for i in range(1,a+1):
        f=f*i

    return f/a #deviser factoriel d'un nombre par le meme 



# Programme principale pour tester les Fonction
n=int(input("Entrez un nombre: "))
s=0
# faire la somme de quotient de facteur d'un nombre sur eux meme
for i in range(1,n+1):
    s= s + Qfacteur(i)
print(f"la somme de serie est {s}")
