#附加题
def index(version1,version2):
    v1=v2=''
    version1=version1.split('.')
    version2=version2.split('.')
    for ver1 in version1:v1+=str(int(ver1))
    for ver2 in version2:v2+=str(int(ver2))
    if len(v1)<len(v2):v1=v1.ljust(len(v2),'0')
    elif len(v1)>len(v2):v2=v2.ljust(len(v1),'0')
    if v1<v2:return -1
    elif v1>v2:return 1
    else:return 0
print(index(version1 = "0.1", version2 = "1.1"))
print(index( version1 = "1.0.1", version2 = "1"))
print(index(version1 = "7.5.2.4", version2 = "7.5.3"))
print(index(version1 = "1.01", version2 = "1.001"))
print(index(version1 = "1.0", version2 = "1.0.0"
))

