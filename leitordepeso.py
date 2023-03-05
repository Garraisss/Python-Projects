maior = 0
menor = 0
for p in range(1, 6): #Para uma distancia de 1 a 5
    peso = float(input('Digite o peso da {} pessoa: '.format(p))) #Digite o Numero Flutuante
    if p == 1:
        maior = peso #classe que define a palavra maior pra ser igual o peso definido no input
        menor = peso #classe que define a palavra menor pra ser igual o peso definido no input
    else:
        if peso > maior: #Se o peso for maior
            maior = peso #Logo o peso é definido como maior
            if peso < menor: #Se o peso for menor
             menor = peso #Logo é definido como menor
print('O Maior peso lido foi de {}Kg'.format(maior))
print('O Menor peso lido foi de {}Kg'.format(menor))
