bruto = float(input("Digite o valor do seu salário bruto: "))

impostoRenda = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05

liquido = bruto - impostoRenda - inss - sindicato
print("O valor do seu salário liquido será de:", liquido)