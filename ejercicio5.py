lista=[5, 6, 7, 8]
sum=0
max=lista[0]
min=lista[0]

for i in range(len(lista)):
  sum=sum+lista[i]
  if lista[i]>max:
    max=lista[i]
  if lista[i]<min:
    min=lista[i]

print("Maximo: ",max)
print("Minimo: ", min)
print("Sumatoria: ",sum)