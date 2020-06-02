# Faça um algoritimo que leia um salario de um funcionario e mostre o novo falario com 15% de aumento

salario = float(input("Digite o salrio atual: "))
reajuste = 15/100
novo_salario = salario + (salario * reajuste)
print(
    f"O salrio atual é de {salario}, hoje é possivel um reajuste de {reajuste}, desta forma o novo salario e {novo_salario}")

