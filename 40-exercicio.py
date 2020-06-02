# O programa deve ler duas notas, calcular a média e informar se esta reprovado de recuperação ou foi aprovado


nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))


media = (nota1 + nota2) / 2


if media < 5.0:
    print(f"Sua nota foi de {media}, assim sendo, esta REPROVADO")
elif media >= 5.0 and media <= 6.9:
    print(f"Sua nota foi de {media}, assim sendo, esta em RECUPERAÇÃO")
else:
    print(f"Sua nota foi de {media}, assim sendo, esta APROVADO")
