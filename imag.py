x=3+4j
n=0
for i in range(1,100):
  mod=abs(x**i)
  if i==1:
     n=mod
     e=i
  if mod>=100:
     e=i
     break
print('El n más pequeño es:',e)