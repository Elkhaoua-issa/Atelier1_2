#Fontion calculer la somme des nombres de 1 à n avec récursivité
def somme(a):
    if a==0:
        return a
    else:
        return (a + somme(a-1))

# Programme principale pour tester les Fonction

x=int(input("n= "))
print(somme(x))
