from random import randint
def dele(n):
    fac=[]
    for i in range(50):
        if n[i]%2==0:
            fac.append(n[i])
    return fac
n=[randint(1,10000)for i in range(50)]
a=n[::-1]
dele(a)