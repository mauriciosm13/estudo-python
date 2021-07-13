def calculate():
    operation = input('''
Digite a operação matemática que deseja:
+ for adição
- for subtração
* for multiplicação
/ for divisão
''')

    n1 = int(input('Por favor digite o primeiro número: '))
    n2 = int(input('Por favor digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('Tecla não foi valida')

    # Add again() function to calculate() function
    repetir()

def repetir():
    calc_again = input('''
Quer calcular de novo?
Please type S for SIM or N for NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Obrigado')
    else:
        repetir()

calculate()
