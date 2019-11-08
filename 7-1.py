def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result
source='shandong university of science and technology'
key='Miaokun'
print('Before Encrypted:'+source)
crypted=crypt(source,key)
print('After Encrypted:'+crypted)
encrypted=crypt(crypted,key)
print('After Entrypted:'+encrypted)