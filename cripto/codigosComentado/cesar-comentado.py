#importa sys que recenbe o nome do arquivo que sera utilizado
import sys
#1 importa biblioteca de letras pequenas
from string import lowercase as  lc
#1 agurmento= nome do arquivo
file = open(sys.argv[1],'r').read().lower()
#2 argumento = numero da chave trasnformado em int
key = int(sys.argv[2])
#3 argumento = descriptografar ou criptografar
mode = sys.argv[3]
#result vazio para armazenar a cifra
result = ''
#lop para ler todo o arquivo escolhido
for lt in file:
	#se o arquivo lt(que tem o arquivo) as letras forem minusculas, ele joga para idx
	if lt in lc:
		idx=lc.find(lt)
		#criptografa se escolher op enc, usando base 26 
		if mode == 'enc':
			idx = ( idx + key) % 26
		#descriptografa se escolher op enc, usando base 26 
		elif mode == 'dec':
			idx = (idx - key) % 26
		#armazena o resultado
		result += lc[idx]
	else:
		result+=lt 
#imprime o resultado(ultimo else elimina os espacos)
print result,

