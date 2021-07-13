valor_hora = float(input("Digite quanto você ganha por hora: "))
dias = int(input("Digite a quantidade de dias trabalhados: "))
hora_dia = 8

diario = valor_hora * hora_dia

salario = diario * dias

print("O valor do salário será de :", salario)