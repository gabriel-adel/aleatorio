#importa biblioteca onde permite pegar o nome do arquivo
import sys
#importa letras minusculas armazenando no lc
from string import lowercase as  lc
#importa o arquivo como 1 argumento
file = open(sys.argv[1],'r').read().lower()


#gera um lop onde testa todas as possibilidades alfabeticas
for key in xrange(1,26):
	result = '' #resultado vazio sempre que começa um loop
	print 'key:',key #imprime a chave 	
	for lt in file: #loop para testar todo o arquivo guarda em lt
		if lt in lc:
			idx=lc.find(lt) #guarda as letras em um index
			idx = (idx - key) % 26 #subtrai o index - a chave do loop acima
			result += lc[idx] #guarda o resultado 
		else:
			result+=lt #ignora espaços vazio

	print result,#imprime resultado

