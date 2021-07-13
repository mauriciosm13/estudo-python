altura = float(input("Digite sua altura: "))
sexo = str(input("Digite a inicial do seu sexo: "))

if sexo == 'M':
    pesoIdeal = (72.7 * altura) - 58
elif sexo == 'F':
     pesoIdeal = (62.1 * altura) - 44.7
else: 
    print('ERRO')


print("Seu peso ideal é: ", pesoIdeal)