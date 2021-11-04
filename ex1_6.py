# fonction tri a bull
def Tri_a_bull(List, a):
    for i in range(a):
        for j in range(a-1-i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

# fonction tri par selection
def tri_par_selection(List, a):
    for i in range(a):
       # Trouver le min
        min = i
        for j in range(i+1, a):
            if List[min] > List[j]:
                min = j

        tmp = List[i]
        List[i] = List[min]
        List[min] = tmp
    return List
#fonction tri par insertion
def tri_par_insertion(List,a): 
    for i in range(1, a): 
        tmp = List[i] 
        j = i-1
        while j >= 0 and tmp < List[j] : 
                List[j + 1] = List[j] 
                j -= 1
        List[j + 1] = tmp
    return List

# Programme principale pour tester les Fonction
List = []
i = 0
n = int(input("Entrez la taille de votre tableau: "))
print("Entrez les valeurs de tableau!")
for i in range(0, n):
    ele = int(input(f"List({i}): "))
    List.append(ele)
#afficher tous les type de tri
print(f"Votre Tableau avec tri a bull est: {Tri_a_bull(List,n)}")
print(f"Votre Tableau avec tri par selection est: {tri_par_selection(List,n)}")
print(f"Votre Tableau avec tri par insertion est: {tri_par_insertion(List,n)}")
