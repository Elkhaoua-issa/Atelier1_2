#fonction pour deviser la liste en trois
def deviser(Liste):
    n=len(Liste)
    i=0
    LD=[]
    if n%3!=0:
        print("Erreur! impossible de diveser cette liste en trois ")
    else:
        while i<n:
            LD.append([Liste[i],Liste[i+1],Liste[i+2]])
            i+=3

    return LD

Liste=[]
n = int(input("Entrez le nombre des element de tableau : "))
print("Entrez les elements de tableau:")
for i in range(0, n):
    ele = int(input(f"Liste[{i}]: "))
    Liste.append(ele)
tmp=deviser(Liste)
#inverser le premiers et la dernier element de liste
for i in range(0,len(deviser(Liste))):
    tmp[i][0],tmp[i][2]=tmp[i][2],tmp[i][0]


print(tmp)
