x=input()
xlist=x.split(" ")
y=len(xlist)
xlist=[int(xlist[i]) for i in range(y)]
a=xlist[y-2]
b=xlist[y-1]
xlist[a:b:1]
