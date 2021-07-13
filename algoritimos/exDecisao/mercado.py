carne = int(input("Qual carne deseja? 1 - Filé Duplo; 2 - Alcatra; 3 - Picanha "))
if carne != 1 or  carne != 2 or carne != 3:
        print("Carne fora de estoque")
     
quantidade = float(input("Quantos Kg deseja? "))

if carne == 1:
    if quantidade > 5:
        valorCompra = quantidade * 5.8
    else:   
        valorCompra = quantidade * 4.9   
elif carne == 2:
    if quantidade > 5:
        valorCompra = quantidade * 6.8
    else:   
        valorCompra = quantidade * 5.9  
elif carne == 3:
    if quantidade > 5:
        valorCompra = quantidade * 7.8
    else:   
        valorCompra = quantidade * 6.9
formaPag = int(input("Formade pagamento:  1 - Cartão Tabajara; 2 - Outros "))
if formaPag == 1: 
       valorTotal = valorCompra / 1.05
else: 
  valorTotal = valorCompra


