nota1 = int(input('Digite a nota do 1º bimestre: '))
nota2 = int(input('Digite a nota do 2º bimestre: '))
nota3 = int(input('Digite a nota do 3º bimestre: '))
nota4 = int(input('Digite a nota do 4º bimestre: '))
media = (nota1+nota2+nota3+nota4)/4

print('A nota do 1º bimestre foi ', nota1, 'A nota do 2º bimestre foi ', nota2,'A nota do 3º bimestre foi ', nota3,'A nota do 4º bimestre foi ', nota4)
if media >= 6:
    print('O aluno está Aprovado!')
else :
    print('O aluno está Reprovado!')