x=input('输入一个成语：')
x=x[-1]
count=0
with open('成语.txt','r',encoding='UTF-8')as fp:
    for line in fp:
        if line[0]==x:
            print(line)
            count=1
            break
    if count==0:
        print('没有以{}字开头的成语'.format(x))
