morango = float(input("Quantos Kg de morango foram comprados? "))
maca = float(input("Quantos Kg de maça foram comprados? "))

kgTotal = morango + maca

if morango <= 5:
    valorMorango = morango * 2.5
else: 
     valorMorango = morango * 2.2

if maca <= 5:
    valorMaca = maca * 1.8
else:
    valorMaca = maca * 1.5

kgTotal = morango + maca
valorTotal = valorMaca + valorMorango

if valorTotal > 25 or kgTotal > 8:
    valorTotal = valorTotal * 1.01

print("Valor total da compra foi: ",valorTotal)