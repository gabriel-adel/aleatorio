#importa sys que permite argumento no cmd
import sys
#importa letras minusculas
from string import lowercase as lc

file= open(sys.argv[1],'r').read().lower() #1 argumento= nome do arquivo 
key = sys.argv[2].lower() #2 argumento = palavra chave tudo junto e misturado
mode= sys.argv[3] #modo encripta ou descripta

result = '' #resultado vazio
keyidx = 0 #lembra qual posicao a palavra esta. 
#ex1: 
#gabrielemuitolegalporquesim
#senhasenhasenhasenhasenhase
for lt in file: #ler todo o arquivo
	if lt in lc: #le todas as letras
		idx = lc.find(lt) #guarda as letras no lc
		if mode == 'enc':
			idx+=lc.find(key[keyidx%len(key)])# preenche a frase a ser criptografada com a chave, deixando a frase e a chave com o mesmo numero de palavras repetindo a chave sempre ate o final da frase. ex1 ali  em cima. 
		elif mode == 'dec':
			idx-=lc.find(key[keyidx%len(key)])#faz o inverso do texto ali em cima. 
		result +=lc[idx%26] #se o resultado for maior que 26, ele volta para zero e soma o que sobrou. ex: 32 = 26 + 6 result = 6.
	else:
		result +=lt #ignora espaços
print result, #print result.
