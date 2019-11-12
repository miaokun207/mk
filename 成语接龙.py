x=input('输入一个成语：')
s=x[-1]
count1=0
count2=0
with open('1.txt','r',encoding='UTF-8')as fp:
    for line in fp:
        if line[:4]==x or line[:5]==x or line[:6]==x or line[:7]==x or line[:8]==x or line[:9]==x:
            count1=1
            break
    if count1==0:
        print('输入不是成语，请重新输入')
    elif count1==1:
        for line in fp:
            if line[0]==s:
                print(line)
                count2=1
                break
        if count2==0:
            print('没有以‘{}’字开头的成语'.format(s))
