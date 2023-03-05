somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1,5):
    print('-----{}ª PESSOA -----'.format(p))
    nome =  str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade  += idade
    if p == 1 and sexo in 'Mm':
           maioridadehomem = idade
           nommevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
          totmulher20 += 1
médiaidade = somaidade / 4
resultadoidade = print(' A Média de idade do grupo é de {} anos'.format(médiaidade))
resultadohomem = print ('O homem mais velho tem {} anos, e se chama {}.'.format(maioridadehomem, nomevelho))
resultadomulher = print ('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))


