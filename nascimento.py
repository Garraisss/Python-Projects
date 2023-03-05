from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8): #Esse codigo seleciona numeros de 0 a infinito, é possivel criar algoritmos que usam numerações ou posiçoes numéricas.
    nasc = int(input('Em que ano a pessoa {} nasceu: '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior +=1
    else:
        print('essa pessoa é menor de idade')
        totmenor +=1
        print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
        print('e Também tivemos {} pessoas menores de idade'.format(totmenor))
