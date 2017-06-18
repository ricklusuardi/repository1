
lista = ['Luigi', 'Giovanni' , 'Elena' , 'Maria', 'Elia' , 'Luisa' , 'Anna']

for persona in lista:
	print(persona)

lista.sort()

lunghezza=len(lista)

for i in range(lunghezza):
 	print(i+1, lista[i])


risposta = input("""per cercare un nome in elenco e farsi dare il corrispondente numero premere 1
 	  per sapere, inseriti numeri da 1 a 7, il nome corrispondente premere 2
 	  per estrarre due nomi di persona da visualizzare ed eliminare premere 3""")

if risposta == 1 :
	nome = input('scrivi il nome della persona di cui vuoi sapere il numero')
	numero = lista.index(nome)
	print('il numero corrispondente è' , numero)

elif risposta == 2:
	numero2= input('inserisci un numero da 1 a 7' )
	if 0<numero<7: 
		nome2 = [numero2]
		print('il nome corrispondente è' , nome2 )
	else:
	    print('il numero deve essere da 1 a 7, idiota')
elif risposta == 3:
	eliminando1= input('scrivi il primo nome da eliminare' )
	numero3 = lista.index(elimindando1)
	lista.pop(numero3)
	elimindando2= input('scrivi il secondo nome da eliminare')
	numero4 = lista.index(elimindando2)
	lista.pop(numero4)
else:
	print(' ho detto di digitare numero da 1 a 3, idiota')

print(lista)


