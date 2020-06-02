# o programa deve calcular o IMC


peso = float(input("Por favor, informe o seu peso: "))
altura = float(input("Por favor, informe o seu altura: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"Seu IMC é de {imc}%, Você esta abaixo do peso!")
elif imc > 18.5 and imc <= 25:
    print(f"Seu IMC é de {imc}%, Você esta com peso ideal!")
elif imc > 25 and imc <= 30:
    print(f"Seu IMC é de {imc}%, Você esta com sobre peso!")
else:
    print(f"Seu IMC é de {imc}%, Você esta com obesidade móbida!")
