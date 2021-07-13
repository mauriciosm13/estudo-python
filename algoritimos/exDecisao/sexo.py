sexo = str(input("Digite a inicial do seu sexo: (M para masculino ou F para feminino) "))

if sexo == 'M' or sexo == 'm':
    print("O sexo selecionado foi Masculino")
elif sexo == 'F' or sexo == 'f':
    print("O sexo selecionado foi Feminino")
else:
    print("Sexo Indefinido")