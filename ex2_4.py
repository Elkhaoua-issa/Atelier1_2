l1=[]
n = int(input("Entrez le nombre des element de set : "))
print("Entrez les elements de set:")
for i in range(0, n):
    ele = int(input())
    l1.append(ele)
l2=[]
n = int(input("Entrez le nombre des element de set : "))
print("Entrez les elements de set:")
for i in range(0, n):
    ele = int(input())
    l2.append(ele)
set1=set(l1)
set2=set(l2)
print(set1 & set2)
print(set1 - set2)
