from random import randint
def demo(n):
    for i in range(10):
        count=0
        for j in range(9):
            if n[count]<n[count+2]:
                n[count],n[count+2]=n[count+2],n[count]
            count+=2
    return n
n=[randint(1,100)for i in range(20)]
demo(n)