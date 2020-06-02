# O programa deve ler um numero de 0 a 9999 e mostre na tela as unidades: milhar, centena, dezena e unidade


n = int(input("Digite um numero de 0 9999: "))12

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f" Unidade: {u}")
print(f" Dezena:  {d}")
print(f" Centena: {c}")
print(f" Milhar:  {m}")
