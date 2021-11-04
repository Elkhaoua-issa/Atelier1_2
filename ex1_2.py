#Fonction convertir le nombre décimal en nombre binaire
def binairy(a):
    B=0
    c=1
    """il suffit de faire des divisions entières successives par 2 ,
    jusqu'à ce que le quotient devienne nul. 
    Le résultat sera la juxtaposition des restes."""
    while a!=0 :
        l=a%2
        a=a//2
        # B prend le reste de division en 2 et multiplier le reste chaque fois car on prend la juxtapose
        B=B+l*c 
        c=c*10
    return B


# Programme principale pour tester les Fonction
D=int(input("Entrez votre nombre dicemal: "))
print(f"{D} ---binaire---> {binairy(D)}")
