x={'宋义显': 3,'李东尧':1,'高世玮':2}
a=input('请输入要查询的名字:')
if a in x :
    print(x[a])
else:
    print('您输入的键不存在')
