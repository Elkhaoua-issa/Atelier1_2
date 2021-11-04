#fonction de fibonacci
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        #la somme de deux derniers valeurs
        return(fibonacci(n-1) + fibonacci(n-2))

# Programme principale pour tester les Fonction

x=int(input("Entrez un nombre: "))
#Verifier si l'utilisateur entre un valeur strictement positif
while x<=0:
    x=int(input("ATTENTION! le nombre doit etre strictemnt positif: "))


print("la serie de fibonacci:")
for i in range(x):
     print(fibonacci(i))
