frase = str(input('Digite uma Frase: ')).strip().upper()  #Li a frase e Splitei ela
palavras = frase.split() #Separei numa lista
junto = ''.join(palavras) #Juntei tudo
inverso = '' #Troquei
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')

