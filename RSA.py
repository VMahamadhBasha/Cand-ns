p=3
q=11
e=3
n=p*q
m=8
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
print("Public key::",(e,n))
print("Private Key::",(d,n))
c=pow(m,e,n)
print("密文：",c)
c=pow(c,d,n)
print("明文：",c)
