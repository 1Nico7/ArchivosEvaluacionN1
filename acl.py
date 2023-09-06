acl = int(input("¿Cual es el numero de IPv4 ACL?:"))
if acl >= 1 and acl <= 99:
    print ("Esta es una ACL IPv4 estandar")
elif acl >= 100 and acl <= 199:
    print("Esta es una ACL IPv4 extendidad")
else:
    print("Esta ACL IPv4 no corrresponde a una estandar o extendida")