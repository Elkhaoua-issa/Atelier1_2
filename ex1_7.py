#fonction inverse un chaine de caractere
def inverse(chaine):
    ch2 = ""  # chaine inversée

    for lettre in reversed(chaine):
        ch2 += lettre

    return ch2

# Programme principale pour tester les Fonction
chaine = str(input("Entrez votre chaine de caractere: "))
print(f"la chaine inverse est: {inverse(chaine)}")
