peso = float(input('Digite o valor do peixe: '))

if peso > 50:
    valor = peso - 50
    multa = valor * 4
    print("O peso excendente é de ", valor, " valor da multa é de R$", multa)

else:
    print("Valor dentro do permitido")