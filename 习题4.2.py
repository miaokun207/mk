x=int(input())
if (x%400==0)or((x%4==0)and(x%100!=0)):
    print('{}是闰年'.format(x))
else:
    print('{}不是闰年'.format(x))