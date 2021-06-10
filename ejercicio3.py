n=0
acum=0
while(n<5):
  numero=float(input("Ingresa calificacion: "))
  acum=acum+numero
  n+=1

print("El promedio es: ",acum/5)