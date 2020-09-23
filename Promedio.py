codigo = str(input("Digite codigo del estudiante: "))
nota1 = int(input("Digite primera nota: "))
nota2 = int(input("Digite segunda nota: "))
nota3 = int(input("Digite tercera nota: "))
nota4 = int(input("Digite cuarta nota: "))
nota5 = int(input("Digite quinta nota: "))
promedio = (nota1+nota2+nota3+nota4+nota5-min(nota1,nota2,nota3,nota4,nota5))/80

print("El promedio ajustado del estudiante ",codigo," es: ",str(round(promedio,2)))
