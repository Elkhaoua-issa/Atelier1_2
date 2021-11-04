#fonction compte les chiffre d"un nombre
def compter(a):
    i=1
    """explication:
    -le nombre entrant devise chaque fois en 10 
    -creer un variable qui compte combien de fois le nombre entrant doit etre divisable par 10"""
    if a//10==0:
        return 1

    else:
        a=a//10
        return i + compter(a-1) 


# Programme principale pour tester les Fonction
a=int(input("Entrez un nombre: "))
print(f"{a} comtient {compter(a)} nombre")