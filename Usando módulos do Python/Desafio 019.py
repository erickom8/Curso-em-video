import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
n5 = str(input('Quinto aluno:'))
n6 = str(input('Sexto aluno:'))
n7 = str(input('Sétimo aluno:'))
n8 = str(input('Oitavo aluno:'))
n9 = str(input('Nono aluno:'))

lista = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
escolhido = random.choice(lista)

print('O aluno escolhido foi o {}'.format(escolhido))

