Liste= []
n = int(input("Entrez le nombre des element de tableau : "))
print("Entrez les elements de tableau:")
for i in range(0, n):
    ele = int(input(f"Liste[{i}]: "))
    Liste.append(ele)
LC={}
for i in range(0,len(Liste)):
    LC[Liste[i]]=Liste.count(Liste[i])

print(LC)


