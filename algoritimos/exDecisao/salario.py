salario = float(input("Digite o valor do seu salário: "))

if salario > 1.045 and salario < 5000:
    aumento = salario * 0.25
    salarioAumento = (salario * 0.25) + salario
    print("Seu aumento foi de: ", aumento, "novo salário será de: ", salarioAumento)
elif salario > 5000 and salario < 10000:
    aumento = salario * 0.2
    salarioAumento = (salario * 0.2) + salario
    print("Seu aumento foi de: ", aumento, "novo salário será de: ", salarioAumento)
else:
    aumento = salario * 0.15
    salarioAumento = (salario * 0.15) + salario
    print("Seu aumento foi de: ", aumento, "novo salário será de: ", salarioAumento)